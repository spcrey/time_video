# Generated by Django 4.1 on 2024-04-11 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]