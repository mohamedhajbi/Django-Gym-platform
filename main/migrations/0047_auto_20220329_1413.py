# Generated by Django 3.1.4 on 2022-03-29 13:13

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20220329_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainertask',
            name='task',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
