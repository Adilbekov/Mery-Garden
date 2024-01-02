from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Slide(models.Model):
    title=models.CharField(
        max_length=255,
        verbose_name='Название баннера'
    )
    description=models.TextField(
        verbose_name='Описание'
    )
    prise=models.CharField(
        max_length=255,
        verbose_name='Цена'
    )
    

    def __str__(self):
        return f'{self.title} - {self.description}'
    
    class Meta:
        verbose_name='Слайд'
        verbose_name_plural='Слайды'

class Condition(models.Model):
    image2=models.ImageField(
        upload_to='image2_Condition',
        verbose_name='Фотография'
    )
    image1=models.ImageField(
        upload_to='image1_Condition',
        verbose_name='Фотография'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    phone=models.CharField(
        max_length=255,
        verbose_name='Телефонный номер'
    )

    def __str__(self):
        return f'{self.descriptions} - {self.phone}'
    
    class Meta:
        verbose_name='Комфортные условия'
        verbose_name_plural='Комфортные условия'

class News(models.Model):
    image_1 = models.ImageField(
        upload_to = 'News_image1',
        verbose_name = 'Фотография'
    )
    image_2 = models.ImageField(
        upload_to = 'News_image2',
        verbose_name = 'Фотография'
    )
    image_3 = models.ImageField(
        upload_to = 'News_image3',
        verbose_name = 'Фотография'
    )
    image_4 = models.ImageField(
        upload_to = 'News_image4',
        verbose_name = 'Фотография'
    )
    image_5 = models.ImageField(
        upload_to = 'News_image5',
        verbose_name = 'Фотография'
    )

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'


class Service(models.Model):
    description_1 = RichTextField(
        verbose_name='Услуга номер -1'
    )
    image_1=models.ImageField(
        upload_to='Serevise_image',
        verbose_name='Фотография - 1'
    )
    
    description_2 = RichTextField(
        verbose_name='Услуга номер -2'
    )
    image_2=models.ImageField(
        upload_to='Serevise_image',
        verbose_name='Фотография - 2'
    )

    description_3 = RichTextField(
        verbose_name='Услуга номер -3'
    )
    image_3=models.ImageField(
        upload_to='Serevise_image',
        verbose_name='Фотография - 3'
    )

    def __str__(self):
        return self.description_1
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Boss(models.Model):
    image = models.ImageField(
        verbose_name='Фотогрфия',
        upload_to='Boss_image'
    )
    title=models.CharField(
        max_length=255,
        verbose_name='Должность'
    )
    description=RichTextField(
        verbose_name='Описание'
    )
    

class Comands(models.Model):
    photo = models.ImageField(
        upload_to=255,
        verbose_name='Фотграфия'
    )
    name = models.CharField(
        verbose_name = 'Имя',
        max_length = 255
    )
    profession = models.CharField(
        verbose_name = 'Должность',
        max_length = 255
    )
    email = models.EmailField(
        verbose_name = 'email.com:'
    )
    instagram = models.URLField(
        verbose_name = 'URL - Instagram'
    )
    twitter = models.URLField(
        verbose_name = 'URL - Twitter'
    )
    facebook = models.URLField(
        verbose_name = 'URL - Facebook'
    )
    pinterest = models.URLField(
        verbose_name = 'URL - Pinterest'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Наша команда'
        verbose_name_plural = 'Наши команды'
    
class Ass(models.Model):
    logo = models.ImageField(
        upload_to='logo',
        verbose_name='Логотип'
    )
    phone_2 = models.CharField(
        verbose_name = 'Телефонный номер для брони баннера',
        max_length = 255
    )
    phone_3 = models.CharField(
        verbose_name = 'Телефонный номер для брони',
        max_length = 255

    )
    description = RichTextField(
        verbose_name = 'Описание к "О нас"'
    )
    adres = models.CharField(
        max_length = 255,
        verbose_name = 'Адрес'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефонный номер'
    )
    email = models.EmailField(
        verbose_name = 'Ваш: email.com'
    )
    admin = models.CharField(
        verbose_name = 'Авторские права принадлежат',
        max_length = 255
    )
    admin_url = models.URLField(
        verbose_name = 'URL - Разработчика'
    )
    instagram = models.URLField(
        verbose_name = 'Ваш: Instagram'
    )
    twitter = models.URLField(
        verbose_name = 'Ваш: Twitter'
    )
    you_tube = models.URLField(
        verbose_name = 'Ваш:You Tube'
    )
    facebook = models.URLField(
        verbose_name = 'Ваш: Facebook'
    )


    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основный настройки'


class Video(models.Model):
    video_url = models.URLField(
        verbose_name = 'URL - Видео о MerriGarden'
    )

    class Meta:
        verbose_name = 'Видео о MerriGarden'
        verbose_name_plural = 'Видео о MerriGarden'