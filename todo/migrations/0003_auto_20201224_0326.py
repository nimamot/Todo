# Generated by Django 3.1.4 on 2020-12-24 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201224_0030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='datecomplited',
            new_name='datecompleted',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='Title',
            new_name='title',
        ),
    ]