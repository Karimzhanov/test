from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Загаловок"
    )

    name1 = models.CharField(
        max_length=255,
        verbose_name="имя"
    )

    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    photo = models.ImageField(
        upload_to='logo/image',
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.name

    class Meta:
            verbose_name = "Настройки"
            verbose_name_plural = "Настройки сайта"

class Servise(models.Model):
    name = models.CharField(
          max_length=255,
          verbose_name="описания сервиса"
    )
    des = models.TextField(
         verbose_name= "Описание"
    )
    image = models.ImageField(
         verbose_name="Логотип"
    )

    def __str__(self):
        return self.name

    class Meta:
            verbose_name = "Сервисы"
            verbose_name_plural = "Сервис"



class About(models.Model):
    des = models.CharField(
          verbose_name="Имя пользователя",
          max_length=255
    )

    photo = models.ImageField(
         verbose_name="Фото"
    )

    def __str__(self):
         return self.des
    
    class Meta:
         verbose_name = "Обо мне"
         verbose_name_plural = "Обо мне"
