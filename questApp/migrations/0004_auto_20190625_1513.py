# Generated by Django 2.1.5 on 2019-06-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questApp', '0003_auto_20190614_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['text'], 'verbose_name': 'Вариант ответа', 'verbose_name_plural': 'Варианты ответов'},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['description'], 'verbose_name': 'Шаг', 'verbose_name_plural': 'Шаги'},
        ),
    ]