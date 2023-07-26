from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.conf import settings
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime('%H ч. %M м. %S с.')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # Получаю все файлы директории
    files_list = os.listdir(settings.BASE_DIR)
    # join с переносом на новую строку
    files_list = ',<br>'.join(files_list)
    return HttpResponse(files_list)

