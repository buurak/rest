# Generated by Django 3.1.7 on 2021-02-26 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='games',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.game'),
        ),
    ]
