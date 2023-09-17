import json
from datetime import datetime


def get_operations_list(file_path):
    '''
    открывает файл json
    возвращает список словарей с операциями
    :param file_path - путь к файлу
    :return: list - список словарей
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_filtered_list(operations_list, key, value):
    '''Фильтрует список словарей по ключу "key"
    возвращает новый список словарей, в которых
    "key" имеет значение "value"
    :param operations_list - список словарей с операциями, key, value - пара ключ/значение
    :return executed_list - новый список словарей, отфильтрованный
    по ключу "key"'''

    return list(filter(lambda x: x.get(key) == value, operations_list))


def get_sorted_list(filtred_list, key):
    '''сортирует по убыванию список словарей по ключу "key"
    :param filtred_list- список словарей
    :return sorted_list - список отсортированных по ключу словарей'''

    return sorted(filtred_list, key=lambda x: x[key], reverse=True)


def get_formatted_date(date):
    '''переводит значение "date" в объект datetime
     и возвращает в формате для вывода
     :param date - str
     :return formatted_date - str'''
    my_date = datetime.fromisoformat(date)
    formatted_date = my_date.strftime('%d.%m.%Y')
    return formatted_date


def hide_number(number):
    '''проверяет строку на соответсивие номеру карты или счета по кол-ву символов
    возвращает соответствующий формат для вывода на печать'''
    if len(number) == 16:
        return f'{number[:4]} {number[4:6]}** **** {number[12:]}'
    return f'**{number[-4:]}'


def get_formatted_data_str(data):
    '''получает строку с наименованием счета/карты
    возвращает строку в формате для вывода на печать
    использует функцию hide_number
    если данные отсутствуют - выводит "данные не указаны"'''
    data_str = data
    if data_str:
        data_list = data.split()
        data_name = ' '.join(data_list[:-1])
        data_number = data_list[-1]
        data_result = f'{data_name} {hide_number(data_number)}'
    else:
        data_result = 'Данные не указаны'
    return data_result


def get_operations_output(operation):
    '''получает словарь возвращает 3 строки в нужном формате для вывода на печать,
    использует функции get_formatted_date, utils.get_formatted_data_str, '''

    operation_date = get_formatted_date(operation['date'])  # переменная даты в нужном формате
    operation_description = operation['description']  # переменная "описание"
    from_ = get_formatted_data_str(operation.get('from'))  # переменная "откуда" в нужном формате
    to_ = get_formatted_data_str(operation.get('to'))  # переменная "куда" в нужном формате
    operation_amount = float(operation['operationAmount']['amount'])  # переменная суммы операции
    currency = operation['operationAmount']['currency']['name']  # переменная наименования валюты

    return (f'{operation_date}  {operation_description}\n'  # 3 строки для вывода на печать
            f'{from_} -> {to_}\n'
            f'{operation_amount} {currency}\n')