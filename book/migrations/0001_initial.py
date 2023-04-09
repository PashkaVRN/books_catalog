# Generated by Django 3.2.16 on 2023-04-06 17:14


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, unique=True, verbose_name='Название книги')),
                ('author', models.CharField(max_length=300, verbose_name='Автор книги')),
                ('description', models.CharField(max_length=3000, verbose_name='Краткое описание книги')),
                ('genre', models.CharField(max_length=50, verbose_name='Жанр книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='BooksRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rented_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи книги')),
                ('returned_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата книги')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.books', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Книга в аренде',
                'verbose_name_plural': 'Книги в аренде',
            },
        ),
    ]
