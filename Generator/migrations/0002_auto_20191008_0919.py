# Generated by Django 2.2.6 on 2019-10-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronjob',
            name='exec_interval',
        ),
        migrations.RemoveField(
            model_name='cronjob',
            name='exec_time',
        ),
        migrations.RemoveField(
            model_name='cronjob',
            name='password',
        ),
        migrations.RemoveField(
            model_name='cronjob',
            name='user',
        ),
        migrations.AddField(
            model_name='cronjob',
            name='allert_type',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='auth_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='auth_pw',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='auth_user',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='exec_day',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='exec_hour',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='exec_minute',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='exec_month',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='exec_weekday',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='save_response',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='url',
            field=models.URLField(default='', max_length=255),
        ),
    ]