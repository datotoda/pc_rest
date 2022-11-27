from django.db import models
from django.utils.translation import gettext_lazy as _


class Manufacturer(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    link = models.URLField(verbose_name=_('Link'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')


class Socket(models.Model):
    socket_type = models.ForeignKey(
        to='general.SocketType',
        verbose_name=_('Socket Type'),
        related_name='sockets',
        on_delete=models.PROTECT
    )
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    pins = models.PositiveIntegerField(verbose_name=_('Pins'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Socket')
        verbose_name_plural = _('Socket')


class SocketType(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Socket Type')
        verbose_name_plural = _('Socket Types')


class FormFactor(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Form Factor')
        verbose_name_plural = _('Form Factors')


class MemoryType(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Memory Type')
        verbose_name_plural = _('Memory Types')
