# Generated by Django 3.2.16 on 2022-12-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_doublevideo_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doublevideo',
            name='upload_time',
            field=models.DateTimeField(verbose_name='uploading time'),
        ),
    ]