# Generated by Django 3.2.16 on 2023-04-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20230417_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksrent',
            name='rented_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Укажите дату выдачи книги читателю', verbose_name='Дата выдачи книги'),
        ),
        migrations.AlterField(
            model_name='booksrent',
            name='returned_at',
            field=models.DateTimeField(blank=True, help_text='Укажите дату возврата книги читателем', null=True, verbose_name='Дата возврата книги'),
        ),
    ]
