import requests


class HTTPClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url):
        response = requests.get(f"{self.base_url}{url}")
        if response.status_code == 200:
            return response.json()
        raise ValueError("Something went wrong")

    def post(self):
        pass


class EmployeeService:
    def __init__(self, http_client):
        self.http_client = http_client

    def get_employee_details(self, employee_id):
        employee_data = self.http_client.get(f"/details/{employee_id}")
        return employee_data
