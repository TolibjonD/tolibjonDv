# Generated by Django 4.0 on 2023-03-28 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitorsinformation',
            old_name='subdivisions',
            new_name='region',
        ),
    ]
