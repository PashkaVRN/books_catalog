# Generated by Django 3.2.16 on 2023-04-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksrent',
            name='rented_at',
            field=models.DateField(help_text='Укажите дату выдачи книги читателю', verbose_name='Дата выдачи книги'),
        ),
    ]
