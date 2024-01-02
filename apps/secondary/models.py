from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Contact(models.Model):
    description = RichTextField(
        verbose_name = 'Описание'
    )
    phone = models.CharField(
        verbose_name = 'Телефонный номер',
        max_length = 255
    )
    email = models.EmailField(
        verbose_name = 'email: '
    )
    adres = models.CharField(
        verbose_name = 'Адрес',
        max_length = 255
    )
    
    def __str__(self):
        return f'{self.description} - {self.phone}'
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

class Photo(models.Model):
    image_1 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_1'
    )
    image_2 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_2'
    )
    image_3 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_3'
    )
    image_4 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_4'
    )
    image_5 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_5'
    )
    image_6 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_6'
    )
    image_7 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_7'
    )
    image_8 = models.ImageField(
        verbose_name = 'Фотография',
        upload_to = 'Photo_image_8'
    )

    
    class Meta:
        verbose_name = 'Фотография к голерее'
        verbose_name_plural = 'Фотографии к голерее'

class Reservation(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.CharField(
        max_length = 255,
        verbose_name = 'Описание'
    )
    logo = models.ImageField(
        upload_to='Reservation_logo',
        verbose_name='Логотип'
    )
    image_one = models.ImageField(
        upload_to='Reservation_image_one',
        verbose_name='Фотография'
    )
    image_two = models.ImageField(
        upload_to='Reservation_image_two',
        verbose_name='Фотография'
    )

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'