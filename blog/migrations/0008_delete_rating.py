# Generated by Django 3.2.23 on 2023-12-27 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_recipe_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
