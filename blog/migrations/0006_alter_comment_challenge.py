# Generated by Django 4.2.8 on 2024-01-18 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='challenge',
            field=models.FloatField(default=3.0),
        ),
    ]
