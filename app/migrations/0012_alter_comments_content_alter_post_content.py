# Generated by Django 4.2.3 on 2023-10-26 19:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_comments_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
