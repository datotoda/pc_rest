from django.contrib import admin
from motherboard.models import Motherboard, Chipset


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'socket', 'form_factor', 'memory_type')
    list_filter = ('manufacturer', 'socket', 'form_factor', 'memory_type', 'chipset')
    search_fields = ('title', 'manufacturer__title', 'socket__title', 'form_factor__title',
                     'memory_type__title', 'chipset__title')


@admin.register(Chipset)
class ChipsetAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)
