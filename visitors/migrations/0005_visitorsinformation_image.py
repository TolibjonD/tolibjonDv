# Generated by Django 4.0 on 2023-04-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_visitorsinformation_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorsinformation',
            name='image',
            field=models.ImageField(default='visitors/default.jpg', upload_to='visitors/'),
        ),
    ]
