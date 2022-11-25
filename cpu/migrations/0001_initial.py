# Generated by Django 4.1.3 on 2022-11-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Serieses',
            },
        ),
        migrations.CreateModel(
            name='SocketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Socket Type',
                'verbose_name_plural': 'Socket Types',
            },
        ),
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('pins', models.PositiveIntegerField(verbose_name='Pins')),
                ('socket_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sockets', to='cpu.sockettype', verbose_name='Socket Type')),
            ],
            options={
                'verbose_name': 'Socket',
                'verbose_name_plural': 'Socket',
            },
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=255, verbose_name='Version')),
                ('cores', models.PositiveIntegerField(verbose_name='Cores')),
                ('threads', models.PositiveIntegerField(verbose_name='Threads')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cpus', to='cpu.manufacturer', verbose_name='Manufacturer')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cpus', to='cpu.series', verbose_name='Series')),
                ('socket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cpus', to='cpu.socket', verbose_name='Socket')),
            ],
            options={
                'verbose_name': 'CPU',
                'verbose_name_plural': 'CPUs',
            },
        ),
    ]
