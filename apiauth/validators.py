
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


class PasswordMatchValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, attrs):
        if attrs['password1'] != attrs['password2']:
            field_names = ', '.join(self.fields)
            message = _('The fields {field_names} must match.').format(field_names=field_names)
            raise ValidationError(message, code='password_match')
