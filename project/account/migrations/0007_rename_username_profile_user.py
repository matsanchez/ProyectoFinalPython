# Generated by Django 5.0 on 2023-12-16 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
    ]
