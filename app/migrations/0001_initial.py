# Generated by Django 2.2.9 on 2019-12-24 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
                ('quote1', models.CharField(blank=True, max_length=100, null=True)),
                ('quote2', models.CharField(blank=True, max_length=100, null=True)),
                ('quote3', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Quote Page',
                'verbose_name_plural': 'Quote Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]