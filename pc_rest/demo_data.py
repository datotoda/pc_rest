from cpu.models import Cpu, Series
from general.models import Manufacturer, Socket, SocketType


def add_manufacturers():
    def _add_manufacturers(title, link):
        if not Manufacturer.objects.filter(title=title).exists():
            Manufacturer(title=title, link=link).save()

    _add_manufacturers(title='Intel', link='https://www.intel.com')
    _add_manufacturers(title='Amd', link='https://www.amd.com/en')


def add_series():
    def _add_series(title):
        if not Series.objects.filter(title=title).exists():
            Series(title=title).save()

    _add_series(title='Ryzen 3')
    _add_series(title='Ryzen 5')
    _add_series(title='Ryzen 7')
    _add_series(title='Core i5')
    _add_series(title='Core i7')
    _add_series(title='Core i9')


def add_socket_type():
    def _add_socket_type(title):
        if not SocketType.objects.filter(title=title).exists():
            SocketType(title=title).save()

    _add_socket_type(title='PGA')
    _add_socket_type(title='LGA')
    _add_socket_type(title='BGA')


def add_socket():
    def _add_socket(title, socket_type, pins):
        if not Socket.objects.filter(title=title).exists():
            socket_type_obj, _ = SocketType.objects.get_or_create(title=socket_type)
            Socket(title=title, socket_type=socket_type_obj, pins=pins).save()

    _add_socket(title='AM4', socket_type='PGA', pins=1331)
    _add_socket(title='AM5', socket_type='PGA', pins=1718)
    _add_socket(title='LGA1151', socket_type='LGA', pins=1151)
    _add_socket(title='LGA1200', socket_type='LGA', pins=1200)
    _add_socket(title='LGA1700', socket_type='LGA', pins=1700)


def add_cpu():
    def _add_cpu(manufacturer, series, socket, version, cores, threads):
        if not Cpu.objects.filter(manufacturer__title=manufacturer, series__title=series, version=version).exists():
            manufacturer_obj, _ = Manufacturer.objects.get_or_create(title=manufacturer)
            series_obj, _ = Series.objects.get_or_create(title=series)
            socket_obj, _ = Socket.objects.get_or_create(title=socket)

            Cpu(manufacturer=manufacturer_obj,
                series=series_obj,
                socket=socket_obj,
                version=version,
                cores=cores,
                threads=threads).save()

    _add_cpu(manufacturer='Amd', series='Ryzen 5', socket='AM4', version='5600X', cores=6, threads=12)
    _add_cpu(manufacturer='Amd', series='Ryzen 7', socket='AM5', version='7700X', cores=8, threads=16)
    _add_cpu(manufacturer='Amd', series='Ryzen 7', socket='AM4', version='5800X3D', cores=8, threads=16)

    _add_cpu(manufacturer='Intel', series='Core i5', socket='LGA1700', version='12400', cores=6, threads=12)
    _add_cpu(manufacturer='Intel', series='Core i5', socket='LGA1700', version='13600K', cores=14, threads=20)
    _add_cpu(manufacturer='Intel', series='Core i7', socket='LGA1700', version='12700K', cores=12, threads=20)
    _add_cpu(manufacturer='Intel', series='Core i9', socket='LGA1200', version='11900K', cores=8, threads=16)
    _add_cpu(manufacturer='Intel', series='Core i9', socket='LGA1700', version='13900K', cores=24, threads=32)


def main():
    add_manufacturers()
    add_series()
    add_socket_type()
    add_socket()
    add_cpu()
