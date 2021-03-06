# Generated by Django 3.1.7 on 2021-03-16 14:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wikisite', '0006_auto_20210316_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='number',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='article',
            name='version',
            field=models.IntegerField(default=1),
        ),
    ]
