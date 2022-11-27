from django.db import models
from django.utils.translation import gettext_lazy as _


class Cpu(models.Model):
    manufacturer = models.ForeignKey(
        to='general.Manufacturer',
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
        to='general.Socket',
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


class Series(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Series')
        verbose_name_plural = _('Serieses')
