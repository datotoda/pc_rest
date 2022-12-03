from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from apiauth.models import ActivationToken
from apiauth.tasks import send_mail


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        label=_('Username'),
        write_only=True
    )
    email = serializers.CharField(
        label=_('Email'),
        write_only=True
    )
    password1 = serializers.CharField(
        label=_('Password'),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    password2 = serializers.CharField(
        label=_('Confirm Password'),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    info = serializers.ReadOnlyField(default='You have successfully registered, check email for activation')

    def validate(self, attrs):
        password_1 = attrs.get('password1')
        password_2 = attrs.pop('password2')

        if password_1 != password_2:
            raise serializers.ValidationError({'error': 'passwords dont match'})

        return super().validate(attrs)

    def create(self, validated_data):
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'username already exists'})

        password = validated_data.pop('password1')
        user = User(is_active=False, **validated_data)
        user.set_password(password)
        user.save()

        activation_token = ActivationToken(user=user)
        activation_token.save()

        url = self.context['request'].build_absolute_uri(reverse('activate', kwargs={'token': activation_token.key}))

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

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'info']
