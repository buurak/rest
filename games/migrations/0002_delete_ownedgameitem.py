# Generated by Django 3.1.7 on 2021-02-27 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OwnedGameItem',
        ),
    ]
