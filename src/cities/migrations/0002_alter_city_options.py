# Generated by Django 3.2.7 on 2021-09-27 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Города', 'verbose_name_plural': 'Города'},
        ),
    ]