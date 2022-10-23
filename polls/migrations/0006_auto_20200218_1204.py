# Generated by Django 3.0.2 on 2020-02-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200217_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citizen',
            old_name='user_name',
            new_name='voter_id',
        ),
        migrations.AlterField(
            model_name='choice',
            name='amharic_choice_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='oromic_choice_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='voted_questions',
            field=models.ManyToManyField(blank=True, to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='amharic_question_text',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='oromic_question_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
