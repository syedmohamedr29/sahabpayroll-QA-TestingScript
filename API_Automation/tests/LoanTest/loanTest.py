import pytest
from API_Automation.utils.api_client import create_request_context
from API_Automation.apis.loanAPI.loanAPIs import LoanAPI

@pytest.mark.parametrize("company_id", [
    "3a1bfc8b-d3a6-8fad-a1e3-cc095d479d38"
])
def test_get_loans(playwright, company_id):
    # Create request context
    request_context = create_request_context(playwright)

    # Call Loan API
    response = LoanAPI.get_loans(request_context, company_id)

    # Assertions
    assert response.ok, f"Request failed with status {response.status}"
    json_data = response.json()
    print("Response JSON:", json_data)

    """
    # Extract employee counts if present
    if isinstance(json_data, list):
        employees = [item.get("totalNoOfEmployees") for item in json_data if "totalNoOfEmployees" in item]
        print("Employee Counts:", employees)
        """
