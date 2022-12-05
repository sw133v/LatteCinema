# Generated by Django 3.2.12 on 2022-05-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_review'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liked_Movie_review',
            field=models.ManyToManyField(related_name='user_review_liked', to='movies.Movie'),
        ),
    ]