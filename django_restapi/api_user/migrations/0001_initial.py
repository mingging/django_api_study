# Generated by Django 2.2.5 on 2021-10-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]