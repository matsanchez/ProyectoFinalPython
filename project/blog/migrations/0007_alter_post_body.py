# Generated by Django 5.0 on 2023-12-13 21:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(max_length=500, verbose_name='Experiencia'),
        ),
    ]