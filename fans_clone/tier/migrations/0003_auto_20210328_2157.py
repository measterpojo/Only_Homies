# Generated by Django 3.1.7 on 2021-03-29 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tier', '0002_auto_20210326_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscribed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]