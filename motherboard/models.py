from django.db import models
from django.utils.translation import gettext_lazy as _


class Motherboard(models.Model):
    manufacturer = models.ForeignKey(
        to='general.Manufacturer',
        verbose_name=_('Manufacturer'),
        related_name='motherboards',
        on_delete=models.PROTECT
    )
    socket = models.ForeignKey(
        to='general.Socket',
        verbose_name=_('Socket'),
        related_name='motherboards',
        on_delete=models.PROTECT
    )
    form_factor = models.ForeignKey(
        to='general.FormFactor',
        verbose_name=_('Form Factor'),
        related_name='motherboards',
        on_delete=models.PROTECT
    )
    memory_type = models.ForeignKey(
        to='general.MemoryType',
        verbose_name=_('Memory Type'),
        related_name='motherboards',
        on_delete=models.PROTECT
    )
    chipset = models.ForeignKey(
        to='motherboard.Chipset',
        verbose_name=_('Chipset'),
        related_name='motherboards',
        on_delete=models.PROTECT
    )
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    memory_slots = models.PositiveIntegerField(verbose_name=_('Memory Slots'))
    max_memory = models.PositiveIntegerField(verbose_name=_('Max Memory'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Motherboard')
        verbose_name_plural = _('Motherboards')


class Chipset(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Chipset')
        verbose_name_plural = _('Chipsets')
