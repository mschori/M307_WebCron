"""WebCron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Generator import views as generator_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', generator_views.signup, name="signup"),
    path('', generator_views.index, name="home"),
    path('createcronjob', generator_views.cronjob, name="CreateCronJob"),
    path('process', generator_views.process_form, name="ProcessForm"),
    path('load', generator_views.load_cronjob, name="LoadForm"),
    path('executecronjobs', generator_views.execute_cronjobs, name="ExecuteCronJobs"),
    path('testing', generator_views.testing, name="testing"),
    path('test01', generator_views.test01, name="Test01"),
    path('test02', generator_views.test02, name="Test02"),
    path('test03', generator_views.test03, name="Test03"),
]

handler404 = generator_views.error_404
