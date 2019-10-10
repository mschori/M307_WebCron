from django.contrib.auth.models import User
from django.db import models


class CronJob(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False, default='')
    url = models.URLField(max_length=255, null=False, default='')
    auth_enabled = models.BooleanField(default=False)
    auth_user = models.CharField(max_length=255, null=True)
    auth_pw = models.CharField(max_length=255, null=True)
    execute_interval = models.CharField(max_length=255, null=False, default='* * * * *')
    allert_failed = models.BooleanField(default=False)
    allert_success_after_failed = models.BooleanField(default=False)
    allert_too_much_fails = models.BooleanField(default=False)
    save_response = models.BooleanField(default=True)


class CronJobResponses(models.Model):
    cronjob = models.ForeignKey(CronJob, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now=True)
    cronjob_title = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=255, null=False)
    response = models.CharField(max_length=255, null=False)


