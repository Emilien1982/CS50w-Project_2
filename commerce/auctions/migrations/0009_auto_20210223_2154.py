# Generated by Django 3.1.6 on 2021-02-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210223_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]