# Generated by Django 4.0.5 on 2022-06-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_useruploadfile_download_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequestaudit',
            name='User_audit_request_status',
            field=models.CharField(help_text='User_audit_request_status', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userrequestaudit',
            name='cloud_audit_request_status',
            field=models.CharField(help_text='cloud_audit_request_status', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userrequestaudit',
            name='tpa_audit_request_status',
            field=models.CharField(help_text='tpa_audit_request_status', max_length=200, null=True),
        ),
    ]
