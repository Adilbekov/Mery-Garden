# Generated by Django 5.0 on 2023-12-30 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_slide_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='phone',
        ),
    ]
