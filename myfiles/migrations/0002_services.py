# Generated by Django 3.2.16 on 2023-01-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=40)),
                ('malumot', models.TextField()),
                ('rasm', models.ImageField(upload_to='media')),
            ],
        ),
    ]
