# Generated by Django 4.2.3 on 2024-01-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('code', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
