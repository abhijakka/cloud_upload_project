# Generated by Django 4.0.5 on 2022-06-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0012_useruploadfile_download_genrate_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploadfile',
            name='user_download_status',
            field=models.CharField(default=0, help_text='user_download_status', max_length=200),
        ),
    ]
