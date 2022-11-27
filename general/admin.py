from django.contrib import admin
from general.models import Manufacturer, Socket, SocketType


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'link')
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
