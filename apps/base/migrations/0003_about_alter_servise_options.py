# Generated by Django 5.0.4 on 2024-04-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_servise'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
        migrations.AlterModelOptions(
            name='servise',
            options={'verbose_name': 'Сервисы', 'verbose_name_plural': 'Сервис'},
        ),
    ]
