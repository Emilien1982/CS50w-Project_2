# Generated by Django 3.1.6 on 2021-02-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
