# Generated by Django 4.0 on 2023-04-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0006_alter_visitorsinformation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorsinformation',
            name='image',
            field=models.ImageField(default='visitors/default.png', upload_to='visitors/'),
        ),
    ]