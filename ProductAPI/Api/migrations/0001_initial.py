# Generated by Django 3.2 on 2021-08-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('Color', models.CharField(max_length=500)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=100)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
    ]