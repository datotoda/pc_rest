from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from apiauth.serializers import RegistrationSerializer
from apiauth.tokens import AccountActivationTokenGenerator


class LoginAPIView(ObtainAuthToken):
    authentication_classes = ()


class RegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'info': 'You have successfully registered, check email for activation'},
                        status=response.status_code, headers=response.headers)


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
        user = User.objects.filter(id=uid)
        token_generator = AccountActivationTokenGenerator()
        if user.exists() and token_generator.check_token(user, token):
            user = user[0]
            user.is_active = True
            user.save()
            return Response({'success': 'account is activated'})
        return Response({'error': 'Token is invalid'})
