# Generated by Django 2.2.1 on 2019-05-27 13:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
