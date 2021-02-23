import csv
from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def get_bus_stations_paginator() -> Paginator:
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as file:
        reader = []
        for pos, item in enumerate(csv.DictReader(file), 1):
            item.update({'number': pos})
            reader.append(item)
    paginator = Paginator(reader, settings.BS_PER_PAGE)
    return paginator


# This will be called once, during server start up
bus_paginator = get_bus_stations_paginator()


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page_number = request.GET.get(settings.BS_PARAM_NAME_PAGE, '1')
    current_page = bus_paginator.get_page(current_page_number)
    prev_page_url, next_page_url = None, None
    if current_page.has_previous():
        payload = {settings.BS_PARAM_NAME_PAGE: current_page.previous_page_number()}
        prev_page_url = f'{reverse(bus_stations)}?{urlencode(payload)}'
    if current_page.has_next():
        payload = {settings.BS_PARAM_NAME_PAGE: current_page.next_page_number()}
        next_page_url = f'{reverse(bus_stations)}?{urlencode(payload)}'
    return render(request, 'index.html', context={
        'bus_stations': current_page.object_list,
        'current_page': current_page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url
    })
