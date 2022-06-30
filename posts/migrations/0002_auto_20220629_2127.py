# Generated by Django 3.2.13 on 2022-06-29 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('spanish', 'Spanish'), ('polish', 'Polish'), ('greek', 'Greek'), ('italian', 'Italian'), ('turkish', 'Turkish'), ('french', 'French'), ('moroccan', 'Moroccan'), ('british', 'British'), ('german', 'German'), ('austrian', 'Austrian'), ('lebanese', 'Lebanese'), ('caribbean', 'Caribbean'), ('indian', 'Indian'), ('thai', 'Thai'), ('japanese', 'Japanese'), ('chinese', 'Chinese'), ('mexican', 'Mexican'), ('american', 'American'), ('other', 'Other')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]