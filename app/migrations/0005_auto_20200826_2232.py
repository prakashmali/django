# Generated by Django 3.0.3 on 2020-08-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200826_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
