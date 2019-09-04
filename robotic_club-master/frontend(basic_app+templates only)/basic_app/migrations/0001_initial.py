# Generated by Django 2.1.7 on 2019-06-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_code', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('roll_no', models.CharField(max_length=10)),
                ('mobile_no', models.CharField(max_length=10)),
                ('is_mentor', models.BooleanField(default=False)),
                ('token_got', models.CharField(help_text='Will be provided by club mentors', max_length=7)),
            ],
        ),
    ]
