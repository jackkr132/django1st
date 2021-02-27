import csv
from django.shortcuts import render
from django.conf import settings


def csv_to_dict(filename, delimiter=';', encoding='utf-8') -> (list, list):
    """
    Parse CSV data and return as dictionary
    :param encoding: CSV file encoding
    :param filename: name of sample data in CSV file
    :param delimiter: delimiter used in CSV file
    :return: dictionary with all found elements in CSV file
    """
    with open(filename, mode='rt', encoding=encoding) as data_file:
        # let's get columns order at first
        columns = data_file.readline().strip().split(delimiter)
        data_file.seek(0)
        csv.register_dialect('MyDialect', delimiter=delimiter)
        reader = csv.DictReader(data_file, dialect='MyDialect')
        result = [item for item in reader]
    return result, columns


def inflation_view(request):
    template_name = 'inflation.html'
    table, columns = csv_to_dict(settings.CSV_FILE)
    context = {'columns': columns, 'table': table}
    return render(request, template_name, context)
