# Generated by Django 2.1.7 on 2019-06-14 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_auto_20190608_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('requesting_user', models.CharField(default='initial', max_length=50)),
                ('first', models.CharField(default='initial', max_length=50)),
                ('last', models.CharField(default='initial', max_length=50)),
                ('amount', models.IntegerField(default=1, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='request_item',
            name='amount',
            field=models.IntegerField(default=1, max_length=20),
        ),
    ]
