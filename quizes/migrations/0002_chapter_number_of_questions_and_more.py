# Generated by Django 5.0.1 on 2024-03-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='number_of_questions',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='chapter',
            name='required_score_to_pass',
            field=models.IntegerField(default=0, help_text='score in %'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='time',
            field=models.IntegerField(default=3, help_text='time in minutes'),
        ),
    ]
