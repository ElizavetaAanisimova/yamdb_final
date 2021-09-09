# Generated by Django 3.0.5 on 2021-06-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(
                blank=True, related_name='titles', to='api.Genre'),
        ),
    ]
