# Generated by Django 3.1.4 on 2022-02-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20220213_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='max_member',
            field=models.IntegerField(null=True),
        ),
    ]
