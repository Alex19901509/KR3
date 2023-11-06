import json

EXECUTED_operations = []

def read_operations_json():
    '''считывает  и возвращает json  файл'''
    with open('operations.json', 'r', encoding='utf-8') as f:
        operations = json.load(f)
        return operations


def sort_operation():
    '''сортирует операции по дате'''
    sort_operations = sorted(read_operations_json(), key=lambda x: x['date'], reverse=True)
    return sort_operations


def status():
    '''сортирует по статусу операции'''
    for i in sort_operation():
        if i['state'] == 'EXECUTED':
            EXECUTED_operations.append(i)
status()

def last_operation():
    '''возвращает 5 последних операций'''
    last_operations = EXECUTED_operations[:5]
    return last_operations

