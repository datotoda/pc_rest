from django.contrib import admin
from cpu.models import Cpu, Series


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'socket', 'cores', 'threads')
    list_filter = ('manufacturer', 'series', 'socket', 'cores', 'threads')
    search_fields = ('version', 'manufacturer__title', 'series__title', 'socket__title', 'cores', 'threads')


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)
