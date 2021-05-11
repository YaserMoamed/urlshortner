# Generated by Django 3.2.2 on 2021-05-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='short_urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=20)),
                ('long_url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]