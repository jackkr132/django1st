from django.urls import path, converters, register_converter
from file_server.app.converters import DateConverter
from file_server.app.views import file_list, file_content


register_converter(DateConverter, 'date')

urlpatterns = [
    path('', file_list, name='file_list'),
    # пришлось использовать переменную date потому что такое имя прописано в шаблоне, который менять не желательно
    path('<date:date>/', file_list, name='file_list'),
    path('<str:name>/', file_content, name='file_content')
]
