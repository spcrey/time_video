# Generated by Django 4.1 on 2024-04-11 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_doublevideo_upload_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='doublevideo',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doublevideo',
            name='lr_video_path',
            field=models.CharField(max_length=150),
        ),
    ]