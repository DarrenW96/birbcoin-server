# Generated by Django 2.0.3 on 2018-03-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=64)),
            ],
        ),
    ]
