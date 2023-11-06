import json
from Utils import sort_operation, read_operations_json, last_operation, status, EXECUTED_operations



def test_read_operations_json():
    with open('test.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        def test_id():
            assert data['id'] == 441945886
        def test_state():
            assert data['state'] == "EXECUTED"
        def test_date():
            assert data['date'] == '2019-08-26T10:50:58.294041'
        def test_operationAmount():
            assert data['operationAmount'] == {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}
        def test_description():
            assert data['description'] == "Перевод организации"


        def test_from():
            assert data['from'] == "Maestro 1596837868705199"


        def test_to():
            assert data['to'] == "Счет 64686473678894779589"


def test_sort_operation():
    sort_operations = sorted(read_operations_json(), key=lambda x: x['date'], reverse=True)
    def test_sort_operations():
        assert sort_operations == sorted(read_operations_json(), key=lambda x: x['date'], reverse=True)

def test_status():
    def test_i():
        for i in sort_operation():
            assert i['state'] == 'EXECUTED'

def test_last_operation():
     last_operations = EXECUTED_operations[:5]
     def test_last_operations():
         assert  last_operations == EXECUTED_operations[:5]
     def test_len(last_operations):
         assert len(last_operations) == 5

