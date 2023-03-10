# Generated by Django 3.2.16 on 2023-03-06 11:22

from django.db import migrations, models


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
        ),
    ]
