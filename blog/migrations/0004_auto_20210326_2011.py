# Generated by Django 3.1.7 on 2021-03-26 20:11

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0003_auto_20210326_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auruthor',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
