# Generated by Django 4.1.3 on 2022-12-07 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiauth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActivationToken',
        ),
    ]
