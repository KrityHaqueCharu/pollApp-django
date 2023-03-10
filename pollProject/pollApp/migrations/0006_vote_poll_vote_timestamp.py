# Generated by Django 4.1.5 on 2023-02-12 05:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollApp', '0005_rename_choice_vote_option_remove_vote_voted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='poll',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pollApp.question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
