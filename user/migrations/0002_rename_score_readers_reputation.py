# Generated by Django 3.2.16 on 2023-04-15 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readers',
            old_name='score',
            new_name='reputation',
        ),
    ]
