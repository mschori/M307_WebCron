# Generated by Django 2.2.6 on 2019-10-10 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Generator', '0005_auto_20191010_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='CronJobResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cronjob_title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('response', models.CharField(max_length=255)),
                ('cronjob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Generator.CronJob')),
            ],
        ),
    ]
