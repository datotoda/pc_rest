from django.db import models
from django.utils.translation import gettext_lazy as _


class Cpu(models.Model):
    manufacturer = models.ForeignKey(
        to='cpu.Manufacturer',
        verbose_name=_('Manufacturer'),
        related_name='cpus',
        on_delete=models.PROTECT
    )
    series = models.ForeignKey(
        to='cpu.Series',
        verbose_name=_('Series'),
        related_name='cpus',
        on_delete=models.PROTECT
    )
    socket = models.ForeignKey(
        to='cpu.Socket',
        verbose_name=_('Socket'),
        related_name='cpus',
        on_delete=models.PROTECT
    )
    version = models.CharField(verbose_name=_('Version'), max_length=255)
    cores = models.PositiveIntegerField(verbose_name=_('Cores'))
    threads = models.PositiveIntegerField(verbose_name=_('Threads'))

    def __str__(self):
        return f'{self.manufacturer.title} {self.series.title} {self.version}'

    class Meta:
        verbose_name = _('CPU')
        verbose_name_plural = _('CPUs')


class Manufacturer(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    link = models.URLField(verbose_name=_('Link'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')


class Series(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Serieses')


class Socket(models.Model):
    socket_type = models.ForeignKey(
        to='cpu.SocketType',
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
