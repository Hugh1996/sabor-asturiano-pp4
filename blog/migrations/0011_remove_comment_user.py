# Generated by Django 3.2.23 on 2023-12-28 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]