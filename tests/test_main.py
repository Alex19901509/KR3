from main import date, operation_date, operation_amount, operation_description
from Utils import last_operation
from datetime import datetime
def test_main():
    for operation in last_operation():
        def test_operation_date():
            assert operation_date == operation['date']
        def test_operation_amount():
            assert operation_amount == operation['operationAmount']
        def test_operation_description():
            assert operation_description == operation['description']
        def test_date():
            assert date == datetime.strptime(operation_date, format('%Y-%m-%dT%H:%M:%S.%f'))

