# Generated by Django 3.0.3 on 2020-08-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='datetime',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.FloatField(null=True),
        ),
    ]
