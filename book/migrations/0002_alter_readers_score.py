# Generated by Django 3.2.16 on 2023-04-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readers',
            name='score',
            field=models.IntegerField(default=10, verbose_name='Рейтинг Читателя'),
        ),
    ]