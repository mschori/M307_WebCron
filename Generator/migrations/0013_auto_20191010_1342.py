# Generated by Django 2.2.6 on 2019-10-10 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0012_auto_20191010_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjobresponses',
            name='date',
            field=models.DateField(),
        ),
    ]
