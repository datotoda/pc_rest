from cpu.models import Cpu, Series
from general.models import Manufacturer, Socket, SocketType, FormFactor, MemoryType
from motherboard.models import Motherboard, Chipset


def add_manufacturers():
    def _add_manufacturers(title, link):
        if not Manufacturer.objects.filter(title=title).exists():
            Manufacturer(title=title, link=link).save()

    _add_manufacturers(title='Intel', link='https://www.intel.com')
    _add_manufacturers(title='Amd', link='https://www.amd.com/en')
    _add_manufacturers(title='Asus', link='https://www.asus.com')
    _add_manufacturers(title='Msi', link='https://www.msi.com')
    _add_manufacturers(title='Gigabyte', link='https://www.gigabyte.com/')


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


def add_form_factor():
    def _add_form_factor(title):
        if not FormFactor.objects.filter(title=title).exists():
            FormFactor(title=title).save()

    _add_form_factor(title='ATX')
    _add_form_factor(title='EATX')
    _add_form_factor(title='Micro ATX')
    _add_form_factor(title='Mini ITX')


def add_memory_type():
    def _add_memory_type(title):
        if not MemoryType.objects.filter(title=title).exists():
            MemoryType(title=title).save()

    _add_memory_type(title='DDR3')
    _add_memory_type(title='DDR4')
    _add_memory_type(title='DDR5')


def add_chipset():
    def _add_chipset(title):
        if not Chipset.objects.filter(title=title).exists():
            Chipset(title=title).save()

    _add_chipset(title='AMD X570')
    _add_chipset(title='AMD B650')
    _add_chipset(title='Intel Z390')
    _add_chipset(title='Intel Z490')
    _add_chipset(title='Intel B660')
    _add_chipset(title='Intel B660')


def add_motherboard():
    def _add_motherboard(manufacturer, socket, form_factor, memory_type, chipset, title, memory_slots, max_memory):
        if not Motherboard.objects.filter(manufacturer__title=manufacturer, title=title).exists():
            manufacturer_obj, _ = Manufacturer.objects.get_or_create(title=manufacturer)
            socket_obj, _ = Socket.objects.get_or_create(title=socket)
            form_factor_obj, _ = FormFactor.objects.get_or_create(title=form_factor)
            memory_type_obj, _ = MemoryType.objects.get_or_create(title=memory_type)
            chipset_obj, _ = Chipset.objects.get_or_create(title=chipset)

            Motherboard(manufacturer=manufacturer_obj,
                        socket=socket_obj,
                        form_factor=form_factor_obj,
                        memory_type=memory_type_obj,
                        chipset=chipset_obj,
                        title=title,
                        memory_slots=memory_slots,
                        max_memory=max_memory).save()

    _add_motherboard(manufacturer='Asus', socket='AM4', form_factor='ATX', memory_type='DDR4',
                     chipset='AMD X570', title='TUF GAMING X570-PLUS (WI-FI)', memory_slots=4, max_memory=128)
    _add_motherboard(manufacturer='Gigabyte', socket='AM5', form_factor='Micro ATX', memory_type='DDR5',
                     chipset='AMD B650', title='B650M AORUS ELITE AX', memory_slots=4, max_memory=128)
    _add_motherboard(manufacturer='Asus', socket='LGA1151', form_factor='ATX', memory_type='DDR4',
                     chipset='Intel Z390', title='PRIME Z390-A', memory_slots=4, max_memory=128)
    _add_motherboard(manufacturer='Msi', socket='LGA1200', form_factor='ATX', memory_type='DDR4',
                     chipset='Intel Z490', title='MPG Z490 GAMING EDGE WIFI', memory_slots=4, max_memory=128)
    _add_motherboard(manufacturer='Asus', socket='LGA1700', form_factor='Mini ITX', memory_type='DDR5',
                     chipset='Intel B660', title='ROG STRIX B660-I GAMING WIFI', memory_slots=2, max_memory=64)
    _add_motherboard(manufacturer='Gigabyte', socket='LGA1700', form_factor='Micro ATX', memory_type='DDR4',
                     chipset='Intel B660', title='B660M DS3H', memory_slots=4, max_memory=128)


def general_app():
    add_manufacturers()
    add_socket_type()
    add_socket()
    add_form_factor()
    add_memory_type()


def cpu_app():
    add_series()
    add_cpu()


def motherboard_app():
    add_chipset()
    add_motherboard()


def main():
    general_app()
    cpu_app()
    motherboard_app()
