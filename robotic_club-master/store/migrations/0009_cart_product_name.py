# Generated by Django 2.1.7 on 2019-06-21 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20190621_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_name',
            field=models.CharField(default='initial', max_length=40),
        ),
    ]
