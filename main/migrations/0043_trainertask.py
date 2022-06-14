# Generated by Django 3.1.4 on 2022-03-29 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0042_alter_assignsubscriber_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', froala_editor.fields.FroalaField()),
                ('trainer_ts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer_ts', to='main.trainer')),
                ('user_ts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_ts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]