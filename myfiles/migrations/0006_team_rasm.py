# Generated by Django 3.2.16 on 2023-02-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_portfolio_tur'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='rasm',
            field=models.ImageField(default=0, upload_to='media'),
            preserve_default=False,
        ),
    ]
