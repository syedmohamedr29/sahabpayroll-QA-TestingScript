from http.client import responses
import os
import pytest
import json
from API_Automation.apis.loanAPI.loanAPIs import LoanAPI
from API_Automation.utils.config import BASE_URL, TOKEN
import allure

@allure.feature("Get Data")
@allure.story("GET API")
@pytest.mark.parametrize("company_id", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
def test_get_loans(playwright, company_id):
    loan_client = LoanAPI(playwright, BASE_URL, TOKEN)  # pass token with Bearer prefix

    response = loan_client.get_loans(company_id)
    assert response.status == 200, f"GET request failed with status {response.status}"

    # Print response to check if data is actually coming
    data = response.json()
    print(json.dumps(data, indent=2))

    loan_client.dispose()

@allure.feature("POST Data")
@allure.story("POST API")
@pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
def test_postLoan(playwright, companyId):
    loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
    # Load payload from JSON file
    payload_path = os.path.join(
        os.path.dirname(__file__),
        "..", "..", "data", "loan", "PositiveflowJSon.json"
    )
    with open(payload_path, "r") as f:
        payload = json.load(f)
    # Make POST request
    response = loan_client.post_loans(companyId, payload)
    # Assert response
    assert response.status == 200, f"POST request failed with status {response.status}"
    # Print JSON response
    data = response.json()
    print(json.dumps(data, indent=2))
    assert data.get("companyId") == companyId, f"POST request failed with wrong companyId: {data}"
    #assert data.get("amountAppliedFor") == payload.get("amountAppliedFor"), "amountAppliedFor mismatch"
    #assert data.get("amountSanctioned") == payload.get("amountSanctioned"), "amountSanctioned mismatch"
    #assert data.get("amountDisbursed") == payload.get("amountDisbursed"), "amountDisbursed mismatch"
    #assert data.get("totalInstallments") == payload.get("totalInstallments"), "totalInstallments mismatch"
    assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
    print("Loan record ID:", data.get("id"))
    loan_client.dispose()

