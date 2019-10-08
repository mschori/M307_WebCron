from django.db import models


class CronJob(models.Model):
    title = models.CharField(max_length=255, null=False, default='')
    url = models.URLField(max_length=255, null=False, default='')
    auth_enabled = models.BooleanField(default=False)
    auth_user = models.CharField(max_length=255, null=True)
    auth_pw = models.CharField(max_length=255, null=True)
    exec_minute = models.CharField(max_length=255, null=False, default='')
    exec_hour = models.CharField(max_length=255, null=False, default='')
    exec_day = models.CharField(max_length=255, null=False, default='')
    exec_month = models.CharField(max_length=255, null=False, default='')
    exec_weekday = models.CharField(max_length=255, null=False, default='')
    allert_type = models.CharField(max_length=255, default=True)
    save_response = models.BooleanField(default=True)


