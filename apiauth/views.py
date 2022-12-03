from rest_framework import viewsets, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from apiauth.models import ActivationToken
from apiauth.serializers import RegistrationSerializer


class LoginAPIView(ObtainAuthToken):
    authentication_classes = ()


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


class ActivateAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, token, *args, **kwargs):
        activation_tokens = ActivationToken.objects.filter(key=token).select_related('user')
        if activation_tokens.exists():
            activation_token = activation_tokens[0]
            user = activation_token.user
            user.is_active = True
            user.save()
            activation_token.delete()
            return Response({'success': 'account is activated'})
        return Response({'error': 'Token is invalid'})
