# Generated by Django 3.1.4 on 2022-03-08 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20220308_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainermsg',
            name='user_type',
        ),
    ]