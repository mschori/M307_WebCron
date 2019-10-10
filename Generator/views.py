from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from .models import CronJob
from .models import CronJobResponses
from passlib.hash import pbkdf2_sha256
import requests


def index(request):
    return render(request, 'generator/home.html')


def error_404(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'generator/error404.html', data)


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
        job_id = request.POST.get('job_id', 0)
        user_id = request.user
        execute_interval = '* * * * *'
        title = request.POST['title']
        url = request.POST['url']
        auth_enable = request.POST.get('auth_enable', False)
        auth_user = request.POST.get('auth_user', 'empty')
        auth_password = request.POST.get('auth_password', 'empty')
        # if auth_password != 'empty':
        # auth_password = pbkdf2_sha256.encrypt(auth_password, rounds=200000, salt_size=16)
        execute = request.POST['execute']
        if execute == 'minutely':
            minute = request.POST['minutely_minutes']
            execute_interval = minute + ' * * * *'
        elif execute == 'daily':
            minute = request.POST['daily_minutes']
            hour = request.POST['daily_hour']
            execute_interval = minute + ' ' + hour + ' * * *'
        elif execute == 'monthly':
            minute = request.POST['monthly_minutes']
            hour = request.POST['monthly_hour']
            day_month = request.POST['monthly_day']
            execute_interval = minute + ' ' + hour + ' ' + day_month + ' * *'
        elif execute == 'custom':
            execute_interval = request.POST['custom_input']

        alert_failed = request.POST.get('alert_failed', False)
        alert_success_after_failed = request.POST.get('alert_success_after_failed', False)
        alert_too_much_fails = request.POST.get('alert_too_much_fails', False)
        save_response = request.POST.get('save_response', False)

        cronjob_entry = CronJob()

        if int(job_id) > 0:
            cronjob_entry.id = job_id

        cronjob_entry.creater = user_id
        cronjob_entry.title = title
        cronjob_entry.url = url
        cronjob_entry.auth_enabled = auth_enable
        cronjob_entry.auth_user = auth_user
        cronjob_entry.auth_pw = auth_password
        cronjob_entry.execute_interval = execute_interval
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


@login_required()
def execute_cronjobs(request):
    return render(request, 'generator/executecronjobs.html')


@login_required()
def testing(request):
    entrys = CronJob.objects.all()

    try:
        for entry in entrys:
            url = entry.url
            headers = {'content-type': 'text/html'}
            response = requests.get(url, headers=headers).content

            if entry.save_response:
                response_entry = CronJobResponses()
                cronjob_object = CronJob.objects.get(id=entry.id)
                response_entry.cronjob = cronjob_object
                response_entry.cronjob_title = entry.title
                response_entry.url = entry.url
                response_entry.response = response
                response_entry.save()
        return HttpResponse('Success')

    except:
        return HttpResponse('Fail')


def test01(request):
    return render(request, 'generator/test01.html')


def test02(request):
    return render(request, 'generator/test02.html')


def test03(request):
    return render(request, 'generator/test03.html')
