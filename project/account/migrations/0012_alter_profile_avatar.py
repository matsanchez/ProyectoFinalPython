# Generated by Django 5.0 on 2023-12-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/users/default_avatar.jpeg', upload_to='avatars/'),
        ),
    ]
