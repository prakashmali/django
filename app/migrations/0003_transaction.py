# Generated by Django 3.0.3 on 2020-08-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_dises'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_id', models.CharField(max_length=10)),
                ('Dises', models.CharField(max_length=20)),
                ('datetime', models.FloatField()),
            ],
        ),
    ]
