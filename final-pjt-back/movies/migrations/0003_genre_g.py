# Generated by Django 3.2.12 on 2022-05-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220519_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='G',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
