# Generated by Django 3.2.13 on 2022-07-20 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_content',
            new_name='content',
        ),
    ]
