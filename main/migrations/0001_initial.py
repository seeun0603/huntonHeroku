# Generated by Django 2.2.1 on 2019-07-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('theme', models.CharField(max_length=30)),
                ('kdc', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
