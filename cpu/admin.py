from django.contrib import admin
from cpu.models import Cpu, Manufacturer, Series, Socket, SocketType


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'socket', 'cores', 'threads')
    list_filter = ('manufacturer', 'series', 'socket', 'cores', 'threads')
    search_fields = ('version', 'manufacturer__title', 'series__title', 'socket__title', 'cores', 'threads')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'link')
    search_fields = ('title',)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)


@admin.register(Socket)
class SocketAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'socket_type', 'pins')
    list_filter = ('socket_type',)
    search_fields = ('title', 'socket_type__title', 'pins')


@admin.register(SocketType)
class SocketTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('title',)
