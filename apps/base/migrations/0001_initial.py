# Generated by Django 5.0.4 on 2024-04-26 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Загаловок')),
                ('descriptions', models.TextField(verbose_name='Описание сайта')),
                ('photo', models.ImageField(upload_to='logo/image', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
