from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import JsonResponse
from .models import CronJob


def index(request):
    return render(request, 'generator/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('CreateCronJob')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required()
def cronjob(request):
    jobs = CronJob.objects.filter().only("title")
    return render(request, 'generator/cronjob.html', {'jobs': jobs})


@login_required()
def load_cronjob(request):
    if request.method == "POST":
        entry_id = request.POST['job_select']
        entry = CronJob.objects.filter(pk=entry_id)
        job = serializers.serialize('json', entry)
        return HttpResponse(job, content_type="text/json-comment-filtered")
    else:
        return HttpResponse('Fail')


@login_required()
def process_form(request):
    if request.method == "POST":
        job_id = request.POST['job_id']
        user_id = request.user
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

        cronjob_entry = CronJob()

        if job_id != 'none':
            cronjob_entry.id = job_id

        cronjob_entry.creater = user_id
        cronjob_entry.title = title
        cronjob_entry.url = url
        cronjob_entry.auth_enabled = auth_enable
        cronjob_entry.auth_user = auth_user
        cronjob_entry.auth_pw = auth_password
        cronjob_entry.exec_minute = minute
        cronjob_entry.exec_hour = hour
        cronjob_entry.exec_day = day_month
        cronjob_entry.exec_month = month
        cronjob_entry.exec_weekday = weekday
        cronjob_entry.allert_failed = alert_failed
        cronjob_entry.allert_success_after_failed = alert_success_after_failed
        cronjob_entry.allert_too_much_fails = alert_too_much_fails
        cronjob_entry.save_response = save_response

        try:
            cronjob_entry.save()
            return HttpResponse('Success')

        except:
            return HttpResponse('Fail')
    else:
        return HttpResponse('Fail')
