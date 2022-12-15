from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import viewsets, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from apiauth.serializers import RegistrationSerializer, PasswordResetLinkSendSerializer, PasswordResetSerializer
from apiauth.tokens import AccountActivationTokenGenerator


class LoginAPIView(ObtainAuthToken):
    authentication_classes = ()
    renderer_classes = viewsets.GenericViewSet.renderer_classes


class RegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegistrationSerializer


class TokenResetAPIView(ObtainAuthToken):
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class ActivateAccountAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, uid, token, *args, **kwargs):
        user_qs = User.objects.filter(id=uid)
        token_generator = AccountActivationTokenGenerator()
        if user_qs.exists() and token_generator.check_token(user_qs.first(), token):
            user = user_qs.first()
            user.is_active = True
            user.save()
            return Response({'success': 'account is activated'})
        return Response({'error': 'Token is invalid'})


class PasswordResetAPIView(viewsets.GenericViewSet):
    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        if self.action == 'send_link':
            return PasswordResetLinkSendSerializer
        if self.action == 'password_reset':
            return PasswordResetSerializer
        return super().get_serializer_class()

    def send_link(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def password_reset(self, request, uid, token, *args, **kwargs):
        user_qs = User.objects.filter(id=uid)
        token_generator = PasswordResetTokenGenerator()
        if user_qs.exists() and token_generator.check_token(user_qs.first(), token):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.set_password(user=user_qs.first())
            return Response(serializer.data)
        return Response({'error': 'Token is invalid'})
