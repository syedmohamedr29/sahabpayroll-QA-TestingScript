import pytest
from API_Automation.utils.api_client import create_request_context
from API_Automation.apis.loanAPI.loanAPIs import LoanAPI
import json

@pytest.mark.parametrize("company_id", [
    "3a1bfc8b-d3a6-8fad-a1e3-cc095d479d38"
])
def test_get_loans(playwright, company_id):
    # Create request context
    request_context = create_request_context(playwright)

    # Call Loan API
    response = LoanAPI.get_loans_LandingPageAPI(request_context, company_id)
    # Assertions
    assert response.status == 200, f"API failed: {response.text()}"
    assert response.ok, f"Request failed with status {response.status}"
    """
    {
      "summary": {
        "totalPausedLoans": 0,
        "totalPauseScheduledLoans": 0,
        "totalCreatedPendingProcessing": 0,
        "totalCreatedPendingDisbursement": 0
      },
      "count": 0,
      "output": []
    }
    """
    json_data = response.json()
    print("Response JSON:", json_data)
    print(json_data["summary"]["totalPausedLoans"])
    print("Count:", json_data["count"])



@pytest.mark.parametrize("company_id", [
    "3a1bfc8b-d3a6-8fad-a1e3-cc095d479d38"
])
def test_post_Loan(playwright, company_id):
    request_context = create_request_context(playwright)

    with open(
        r"C:/Users/Comm-IT India/OneDrive - comm-it india pvt ltd/Desktop/SahabPayroll/API_Automation/data/loan/postJSON.json",
        "r"
    ) as f:
        jsonPayload = json.load(f)


    response = LoanAPI.loan_POSTAPI(request_context, company_id, jsonPayload)

    assert response.status == 200, f"API failed: {response.text()}"
    assert response.ok, f"Request failed with status {response.status}"

    json_data = response.json()
    print("Response JSON:", json_data)



