# Generated by Django 3.1.7 on 2021-03-31 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_bookmark'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]