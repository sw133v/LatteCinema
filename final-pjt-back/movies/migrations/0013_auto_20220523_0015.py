# Generated by Django 3.2.12 on 2022-05-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_movie_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Movie_rate',
        ),
    ]