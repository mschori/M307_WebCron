# Generated by Django 2.2.6 on 2019-10-10 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0014_auto_20191010_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronjobresponses',
            name='date',
        ),
    ]
