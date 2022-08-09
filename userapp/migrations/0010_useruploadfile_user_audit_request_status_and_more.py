# Generated by Django 4.0.5 on 2022-06-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_userrequestaudit_user_audit_request_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploadfile',
            name='User_audit_request_status',
            field=models.CharField(help_text='User_audit_request_status', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='useruploadfile',
            name='cloud_audit_request_status',
            field=models.CharField(help_text='cloud_audit_request_status', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='useruploadfile',
            name='tpa_audit_request_status',
            field=models.CharField(help_text='tpa_audit_request_status', max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='UserRequestAudit',
        ),
    ]