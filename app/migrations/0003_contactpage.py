# Generated by Django 2.2.9 on 2019-12-24 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('app', '0002_auto_20191224_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('call', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Contact Page',
                'verbose_name_plural': 'Contact Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
