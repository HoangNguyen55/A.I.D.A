# Generated by Django 4.1.6 on 2023-09-30 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aida_admin_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendinguser',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='pendinguser',
            name='last_login',
        ),
    ]
