# Generated by Django 4.1.5 on 2023-02-07 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0002_uservote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserVote',
        ),
    ]