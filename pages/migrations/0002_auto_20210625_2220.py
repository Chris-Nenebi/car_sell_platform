# Generated by Django 2.0.7 on 2021-06-25 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='current_date',
            new_name='created_date',
        ),
    ]
