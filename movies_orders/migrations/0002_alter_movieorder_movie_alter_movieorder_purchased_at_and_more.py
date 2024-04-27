# Generated by Django 5.0.4 on 2024-04-26 00:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_movie_by'),
        ('movies_orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieorder',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_orders', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='movieorder',
            name='purchased_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movieorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
