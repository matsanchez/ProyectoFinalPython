# Generated by Django 5.0 on 2023-12-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/users/default_avatar.jpeg', null=True, upload_to='media/avatars/'),
        ),
    ]
