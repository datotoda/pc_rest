import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class ActivationToken(models.Model):
    key = models.CharField(verbose_name=_('Key'), max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='activation_token',
        on_delete=models.CASCADE, verbose_name=_('User')
    )
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)

    class Meta:
        verbose_name = _('Activation Token')
        verbose_name_plural = _('Activation Tokens')

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
