# Generated by Django 2.2.5 on 2021-10-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
            ],
        ),
    ]
