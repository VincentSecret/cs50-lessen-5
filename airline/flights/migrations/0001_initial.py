# Generated by Django 3.2.23 on 2023-12-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orign', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]