from datetime import datetime, date
import os
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render


def file_list(request, date: date = None):
    template_name = 'index.html'
    filenames_list = os.listdir(settings.FILES_PATH)
    files_list = []
    for file_name in filenames_list:
        stat = os.stat(os.sep.join([settings.FILES_PATH, file_name]))
        dt_ctime = datetime.fromtimestamp(stat.st_ctime)
        dt_mtime = datetime.fromtimestamp(stat.st_mtime)
        if date and not (date == dt_ctime.date() or date == dt_mtime.date()):
            continue
        files_list.append({'name': file_name, 'ctime': dt_ctime, 'mtime': dt_mtime})
    return render(request, template_name, context={'files': files_list, 'date': date})


def file_content(request, name):
    template_name = 'file_content.html'
    full_name = os.sep.join([settings.FILES_PATH, name])
    if os.path.isfile(full_name):
        with open(full_name, encoding='utf8', mode='r') as f:
            content = ''.join(f.readlines())
        return render(request, template_name, context={'file_name': name, 'file_content': content})
    return HttpResponseNotFound('File not found')
