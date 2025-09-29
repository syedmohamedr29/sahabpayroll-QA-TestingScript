import requests
import pytest
from joblib.testing import param

from API_Automation.utils.config import get_auth_token, get_env_variable , get_credentials
from API_Automation.apis.employeeAPIs.employeeAPI import EmployeeAPI

@pytest.fixture(scope='module')
def test_employeeGET(self):
    """
    Fixture to set up the API client for testing employee GET requests.
    """
    base_url = EmployeeAPI.employee_get_url()
    headers = {
        "Authorization": get_auth_token(),
        "Content-Type": "application/json"
    }

    params = {
        "companyId": "3a191c9d-64cd-7600-c591-e2c5663f9b75",

    }

    self.response = requests.get(url=base_url, headers=headers , params=params)
    print("Status Code:", self.response.status_code)
    if self.response.status_code == 200:
        json_data = self.response.json()
        print("Response JSON Data:", json_data)
    else:
        print("Error Response:", self.response.text)

    assert self.response.status_code == 200, f"Request failed with status code {self.response.status_code}"
    print("Request was successful.")
