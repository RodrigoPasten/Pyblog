# Generated by Django 4.2.3 on 2023-10-26 19:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_comments_content_alter_comments_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
