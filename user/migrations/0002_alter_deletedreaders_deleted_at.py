# Generated by Django 3.2.16 on 2023-04-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletedreaders',
            name='deleted_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата удаления профиля.'),
        ),
    ]
