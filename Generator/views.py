from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CronJob


def index(request):
    return render(request, 'generator/base.html')


def process_form(request):
    if request.method == "POST":
        minute = '*'
        hour = '*'
        day_month = '*'
        month = '*'
        weekday = '*'
        title = request.POST['title']
        url = request.POST['url']
        auth_enable = request.POST.get('auth_enable', False)
        auth_user = request.POST.get('auth_user', 'empty')
        auth_password = request.POST.get('auth_password', 'empty')
        execute = request.POST['execute']
        if execute == 'minutely':
            minute = request.POST['minutely_minutes']
        elif execute == 'daily':
            minute = request.POST['daily_minutes']
            hour = request.POST['daily_hour']
        elif execute == 'monthly':
            minute = request.POST['monthly_minutes']
            hour = request.POST['monthly_hour']
            day_month = request.POST['monthly_day']
        elif execute == 'custom':
            custom_input = request.POST['custom_input'].split(' ')
            minute = custom_input[0]
            hour = custom_input[1]
            day_month = custom_input[2]
            month = custom_input[3]
            weekday = custom_input[4]

        alert_failed = request.POST.get('alert_failed', 0)
        alert_success_after_failed = request.POST.get('alert_success_after_failed', 0)
        alert_too_much_fails = request.POST.get('alert_too_much_fails', 0)
        save_response = request.POST.get('save_response', 0)

        cronjob = CronJob()
        cronjob.title = title
        cronjob.url = url
        cronjob.auth_enabled = auth_enable
        cronjob.auth_user = auth_user
        cronjob.auth_pw = auth_password
        cronjob.exec_minute = minute
        cronjob.exec_hour = hour
        cronjob.exec_day = day_month
        cronjob.exec_month = month
        cronjob.exec_weekday = weekday
        cronjob.allert_failed = alert_failed
        cronjob.allert_success_after_failed = alert_success_after_failed
        cronjob.allert_too_much_fails = alert_too_much_fails
        cronjob.save_response = save_response

        try:
            cronjob.save()
            return HttpResponse('Success')

        except:
            return HttpResponse('Fail')
    else:
        return HttpResponse('Fail')
