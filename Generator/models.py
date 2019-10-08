from django.contrib.auth.models import User
from django.db import models


class CronJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, defaults='')
    url = models.URLField(max_length=255, null=False, default='')
    auth_enabled = models.BooleanField(default=False)
    auth_user = models.CharField(max_length=255, null=True, defaults='')
    auth_pw = models.CharField(max_length=255, null=True, default='')
    exec_interval = models.CharField(max_length=255)
    exec_offset = models.IntegerField(0)
    exec_time = models.CharField(max_length=200)
    allert_type = models.CharField(max_length=255, default=True)
    save_response = models.BooleanField(default=True)


