# Generated by Django 4.0.4 on 2023-07-18 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pulications',
            new_name='publications',
        ),
    ]
