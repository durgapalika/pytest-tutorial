import sqlite3


def create_employee(first_name: str, last_name: str, salary: int):
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO EMPLOYEES(FIRSTNAME,LASTNAME,SALARY VALUES (?,?,?)",
                   (first_name, last_name, salary))
    conn.commit()
    conn.close()
