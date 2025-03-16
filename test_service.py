import pytest
from employeeService import EmployeeService, HTTPClient


def test_get_employee_name(mocker):
    mock_api_client = mocker.Mock()

    mock_api_client.get.return_value = {"first_name": "Developers", "last_name": "Heaven", "salary": 50000}

    service = EmployeeService(mock_api_client)
    result = service.get_employee_details(1)

    assert result == {'first_name': 'Developers', 'last_name': 'Heaven', "salary": 50000}
    mock_api_client.get.assert_called_once_with("/details/1")
