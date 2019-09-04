# Generated by Django 2.1.7 on 2019-06-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(default='old', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_mentor',
            field=models.BooleanField(default=True),
        ),
    ]