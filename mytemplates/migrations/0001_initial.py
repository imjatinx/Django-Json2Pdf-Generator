# Generated by Django 4.2.5 on 2023-10-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Template Name')),
                ('templatePath', models.CharField(blank=True, max_length=50, null=True, verbose_name='Path')),
            ],
        ),
    ]
