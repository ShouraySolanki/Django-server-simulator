# Generated by Django 3.2.2 on 2021-05-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_server', '0006_podcast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]