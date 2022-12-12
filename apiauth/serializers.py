from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from apiauth.tasks import send_mail
from apiauth.tokens import AccountActivationTokenGenerator
from apiauth.validators import PasswordMatchValidator


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        label=_('Password'),
        style={'input_type': 'password'},
        validators=[validate_password],
        trim_whitespace=False,
        write_only=True
    )
    password2 = serializers.CharField(
        label=_('Confirm Password'),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def create(self, validated_data):
        validated_data.pop('password2')

        password = validated_data.pop('password1')
        user = User(is_active=False, **validated_data)
        user.set_password(password)
        user.save()

        activation_token_generator = AccountActivationTokenGenerator()
        activation_token = activation_token_generator.make_token(user=user)

        url = self.context['request'].build_absolute_uri(
            reverse('activate', kwargs={'uid': user.id, 'token': activation_token})
        )

        context = {
            'name': user.username,
            'url': url
        }

        send_mail.delay(
            subject='Activate pc_rest.com account',
            body=render_to_string('apiauth/activation_mail.html', context=context),
            to=[user.email]
        )

        return user

    def to_representation(self, instance):
        return {'info': 'You have successfully registered, check email for activation'}

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        validators = [
            PasswordMatchValidator(
                fields=['password1', 'password2']
            )
        ]


class PasswordResetLinkSendSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    email = serializers.CharField(required=True, allow_blank=False)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')

        if username and email:
            user_qs = User.objects.filter(username=username, email=email)

            if not user_qs.exists():
                msg = _('Username or email are invalid.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "email".')
            raise serializers.ValidationError(msg)

        user = user_qs.first()

        password_reset_token_generator = PasswordResetTokenGenerator()
        activation_token = password_reset_token_generator.make_token(user=user)

        url = self.context['request'].build_absolute_uri(
            reverse('password_reset', kwargs={'uid': user.id, 'token': activation_token})
        )

        context = {
            'name': username,
            'url': url
        }

        send_mail.delay(
            subject='Password Reset in pc_rest.com',
            body=render_to_string('apiauth/activation_mail.html', context=context),
            to=[email]
        )

        return attrs

    def to_representation(self, instance):
        return {'info': 'Password reset link successfully send, check email for link'}


class PasswordResetSerializer(serializers.Serializer):
    password1 = serializers.CharField(
        label=_('Password'),
        style={'input_type': 'password'},
        validators=[validate_password],
        trim_whitespace=False,
        write_only=True
    )
    password2 = serializers.CharField(
        label=_('Confirm Password'),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def set_password(self, user):
        user.set_password(self.validated_data['password1'])
        user.save()

    def to_representation(self, instance):
        return {'success': 'Password Reset successfuly'}

    class Meta:
        validators = [
            PasswordMatchValidator(
                fields=['password1', 'password2']
            )
        ]
