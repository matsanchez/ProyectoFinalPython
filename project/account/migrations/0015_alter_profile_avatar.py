# Generated by Django 5.0 on 2023-12-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_remove_profile_country_delete_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/users/default_avatar.jpeg', null=True, upload_to='avatars/'),
        ),
    ]
