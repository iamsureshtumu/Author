# Generated by Django 2.2.9 on 2019-12-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotepage',
            name='quote1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quotepage',
            name='quote2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quotepage',
            name='quote3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
