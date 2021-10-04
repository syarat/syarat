# Generated by Django 3.2.6 on 2021-08-06 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_url', models.URLField(unique=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_url', models.URLField(unique=True)),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True, auto_now=True)),
                ('url', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=150)),
                ('thumbnail', models.ImageField(blank=True, upload_to='media/thumbnails/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('tag', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]