from django.contrib import admin
from cpu.models import Cpu, Manufacturer, Series, Socket, SocketType


@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Socket)
class SocketAdmin(admin.ModelAdmin):
    pass


@admin.register(SocketType)
class SocketTypeAdmin(admin.ModelAdmin):
    pass
