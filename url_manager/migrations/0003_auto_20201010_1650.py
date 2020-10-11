# Generated by Django 3.1.2 on 2020-10-10 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('url_manager', '0002_auto_20201010_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]