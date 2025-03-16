from db import create_employee


def test_create_employee(mocker):
    mock_conn = mocker.patch("sqlite3.conn")
    mock_cursor = mock_conn.reurn_value.cursor.return_value

    create_employee("Developers", "Heaven", 50000)

    mock_cursor.assert_called_once_with("employees.db")
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO EMPLOYEES(FIRSTNAME,LASTNAME,SALARY VALUES ('Developers','Heaven','50000')"
    )
