# Generated by Django 4.0.5 on 2022-06-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_useruploadfile_file_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploadfile',
            name='file_post_name',
            field=models.CharField(help_text='upload_post_name', max_length=200, null=True),
        ),
    ]
