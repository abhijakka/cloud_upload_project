# Generated by Django 4.0.5 on 2022-06-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0007_useruploadfile_update_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploadfile',
            name='download_rank',
            field=models.CharField(default=0, help_text='view_rank', max_length=200),
        ),
    ]
