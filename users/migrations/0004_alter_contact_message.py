# Generated by Django 4.2.3 on 2023-08-16 22:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
