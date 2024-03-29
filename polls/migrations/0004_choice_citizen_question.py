# Generated by Django 3.0.2 on 2020-02-17 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0003_auto_20200217_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_question_text', models.CharField(max_length=200)),
                ('amharic_question_text', models.CharField(max_length=200)),
                ('oromic_question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('dead_line', models.DateTimeField(verbose_name='deadline')),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('user_name', models.CharField(help_text='Provide a unique username to use each time you vote. Keep it in secret and do not forget the username!', max_length=20, unique=True)),
                ('voted_questions', models.ManyToManyField(to='polls.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('english_choice_text', models.CharField(max_length=200)),
                ('amharic_choice_text', models.CharField(max_length=200)),
                ('oromic_choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]
