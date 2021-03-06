# Generated by Django 3.2.6 on 2021-08-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_url',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_url',
            field=models.SlugField(unique=True),
        ),
    ]
