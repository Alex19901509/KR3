from datetime import datetime
from Utils import last_operation
# запуск цикла по списку отсортированных по дате и и статусу операций
for operation in last_operation():
    # дата операции
    operation_date = operation['date']
    # сумма операции и валюта
    operation_amount = operation['operationAmount']
    # описание типа перевода
    operation_description = operation['description']
    # откуда
    operation_from = operation.get('from', 'none')
    # валюта операции
    currency = operation_amount["currency"]
    # куда
    operation_to = operation.get('to', 'N/A')
    operation_from_split = operation_from.split()
    word = []
    number = []

    for i in operation_from_split:
        if i.isalpha():
            word.append(i)
        else:
            number.append(i)

    number_str = str(number)
    word_join = ''.join(word)
    # формат даты
    date = datetime.strptime(operation_date, format('%Y-%m-%dT%H:%M:%S.%f'))

    # вывод информации про операцию
    print(f'{date:%d.%m.%Y} {operation_description}')
    print(f'{word_join} {number_str[2:6]} {number_str[6:8]}** **** {number_str[-6:-2]} -> **{operation_to[-4:]}')
    print(f'{operation_amount["amount"]} {currency["name"]}\n')



