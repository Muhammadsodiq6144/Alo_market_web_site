# Generated by Django 3.2.16 on 2023-01-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('url', models.URLField()),
                ('malumot', models.TextField()),
                ('rasm1', models.ImageField(upload_to='media')),
                ('rasm2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('rasm3', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=40)),
            ],
        ),
    ]
