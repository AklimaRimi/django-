# Generated by Django 4.0.3 on 2022-03-23 15:20

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='detail',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
