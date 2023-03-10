# Generated by Django 3.2.16 on 2023-03-12 19:58

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_books_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Readers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Username')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя читателя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия читателя')),
                ('email', models.EmailField(max_length=254, verbose_name='email читателя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
                'ordering': ('username',),
            },
        ),
        migrations.CreateModel(
            name='ReaderReputation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='Ретинг Читателя')),
                ('reader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reputation', to='book.readers', verbose_name='Репутация')),
            ],
        ),
        migrations.CreateModel(
            name='BooksRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rented_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи книги')),
                ('returned_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата книги')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.books', verbose_name='Книга')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.readers', verbose_name='Читатель')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='rented_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rented_books', to='book.readers', verbose_name='На руках у ...'),
        ),
    ]
