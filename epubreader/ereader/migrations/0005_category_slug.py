# Generated by Django 3.0.3 on 2020-02-16 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0004_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]