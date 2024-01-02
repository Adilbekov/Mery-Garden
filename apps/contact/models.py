from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'ФИО'
    )
    email = models.EmailField(
        verbose_name = 'Email: '
    )
    phone = models.CharField(
        verbose_name = 'Телефонный номер',
        max_length = 255
    )
    date = models.CharField(
        verbose_name = 'Дата',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.phone}'
    
    class Meta:
        verbose_name='Заявка на бронь'
        verbose_name_plural='Заявки на брони'
