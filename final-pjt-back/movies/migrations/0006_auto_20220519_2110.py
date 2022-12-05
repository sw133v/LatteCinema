# Generated by Django 3.2.12 on 2022-05-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_backdrop_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='adult',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_language',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='overview',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='vote_average',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='vote_count',
            field=models.IntegerField(null=True),
        ),
    ]
