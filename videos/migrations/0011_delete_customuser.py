# Generated by Django 4.1 on 2024-04-11 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]