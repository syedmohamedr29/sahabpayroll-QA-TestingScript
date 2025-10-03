from http.client import responses
import os
import pytest
import json
from API_Automation.apis.loanAPI.loanAPIs import LoanAPI
from API_Automation.utils.config import BASE_URL, TOKEN
import allure
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from datetime import timezone



"""
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
"""

@allure.feature("Loan Management")
@allure.story("Record Loan")
class TestLoanManagement:

    @allure.title("TC_001 - Verify loan recorded with positive Case flow")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_postLoan(self,playwright, companyId):
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
        assert data.get("recordSource") == 3
        print("Loan record ID:", data.get("id"))
        print("Employee Code: ", data.get("employeeCode"))
        loan_client.dispose()

    """Employee Active, EmployeeOffboarding, EmployeeOffboarded"""

    @allure.title("TC_002 - Verify that a loan record cannot be created for an inactive employee")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_InactiveEmployee(self,playwright,companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "inactiveEmployee.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)
        assert response.status == 403, f"POST request failed with inactive employee allowed, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        loan_client.dispose()


    @allure.title("TC_003 - Verify that a loan record can be created for an offboarding employee")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_offboardingEmployee(self,playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "offboardingEmployee.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)
        assert response.status == 200, f"POST request failed with offboarding employee Not allowed, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        print("Employee Code: ", data.get("employeeCode"))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3
        loan_client.dispose()


    @allure.title("TC_004 - Verify that a loan record can be created for an offboarded employee")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_offboardedEmployee(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "offboardedEmployee.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)
        assert response.status == 200, f"POST request failed with offboarded employee Not allowed, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        print("Employee Code: ", data.get("employeeCode"))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3
        loan_client.dispose()


    """With Opening balance"""

    @allure.title("TC_005 - Verify that a loan record can be created with an opening balance.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_withOpeningBalance(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "offboardedEmployee.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        #validate the response status 200
        assert response.status == 200, f"POST request failed with opening balance Not allowed, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))
        print("Employee Code: ", data.get("employeeCode"))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert  data.get("recordSource") == 3
        #validate the isWithOpeningBalance is true
        assert data.get("isWithOpeningBalance") == True, "isWithOpeningBalance is not true"

        # Validate disbursement and approved dates
        disbursement_date_str = data.get("disbursementDate")
        approved_date_str = data.get("approvedDate")
        repayment_start_str = data.get("repaymentStartDate")
        repayment_end_str = data.get("repaymentEndDate")

        assert disbursement_date_str, "disbursementDate is missing"
        disbursement_date = datetime.fromisoformat(disbursement_date_str.replace("Z", "+00:00")).date()
        approved_date = datetime.fromisoformat(approved_date_str.replace("Z", "+00:00")).date()
        repayment_start_date = datetime.fromisoformat(repayment_start_str.replace("Z", "+00:00")).date()
        repayment_end_date = datetime.fromisoformat(repayment_end_str.replace("Z", "+00:00")).date()
        today = date.today()

        assert disbursement_date <= today, f"disbursementDate {disbursement_date} is greater than today {today}"
        assert disbursement_date == approved_date, f"disbursementDate {disbursement_date} != approvedDate {approved_date}"
        assert disbursement_date <= repayment_start_date, f"disbursementDate {disbursement_date} > repaymentStartDate {repayment_start_date}"

        # Validate totalInstallments based on start/end dates
        total_installments = data.get("totalInstallments")
        diff = relativedelta(repayment_end_date, repayment_start_date)
        expected_installments = diff.years * 12 + diff.months + 1
        assert total_installments == expected_installments, (
            f"Installments mismatch: expected {expected_installments}, got {total_installments}"
        )
        expected_end_date = repayment_start_date + relativedelta(months=total_installments - 1)
        assert repayment_end_date == expected_end_date, f"Repayment end date mismatch: expected {expected_end_date}, got {repayment_end_date}"

        # Validate pendingInstallments
        assert total_installments == data.get("pendingInstallments"), "totalInstallments != pendingInstallments"

        # Validate opening balance vs amount disbursed
        amount_disbursed = data.get("amountDisbursed", 0)
        opening_balance = data.get("openingBalance", 0)
        assert opening_balance <= amount_disbursed, f"Opening balance {opening_balance} cannot exceed amountDisbursed {amount_disbursed}"

        # Validate totalAmountRePaid ≤ (amountDisbursed - openingBalance)
        total_amount_repaid = data.get("totalAmountRePaid", 0)
        expected_repaid = amount_disbursed - opening_balance
        assert total_amount_repaid <= expected_repaid, f"totalAmountRePaid {total_amount_repaid} > {expected_repaid}"

        # Validate outsidePayrollPaymentDetails
        if data.get("isWithOpeningBalance"):
            outside_payment = data.get("outsidePayrollPaymentDetails")
            assert outside_payment not in (None, [], {},
                                           ""), "outsidePayrollPaymentDetails required for opening balance"

            # Pay mode checks
            pay_mode = outside_payment.get("payMode")
            if pay_mode == 1:
                assert outside_payment.get("paymentDetails", {}).get(
                    "referenceNo"), "referenceNo is mandatory for payMode=1"
            elif pay_mode == 2:
                assert outside_payment.get("companyBankAccountId"), "companyBankAccountId mandatory for payMode=2"
            elif pay_mode == 3:
                assert outside_payment.get("paymentDetails", {}).get("notes"), "notes mandatory for payMode=3"

            # Amount and date checks
            amount_paid = outside_payment.get("amountPaid", 0)
            paid_on = datetime.fromisoformat(outside_payment.get("paidOn").replace("Z", "+00:00"))
            current_date = datetime.now(timezone.utc)  # aware UTC
            assert amount_paid == opening_balance, f"amountPaid {amount_paid} != openingBalance {opening_balance}"
            assert paid_on <= current_date, f"paidOn {paid_on} cannot be in the future"
            assert paid_on.date() <= repayment_start_date, f"paidOn {paid_on.date()} must be <= repaymentStartDate {repayment_start_date}"

        # Validate repaymentCalculations
        repayment_calc = data.get("repaymentCalculations", {})
        total_pending = data.get("totalAmountPending", 0)
        installment_amount = repayment_calc.get("installmentAmount", 0)
        loan_tenure = repayment_calc.get("loanTenure", 0)

        if installment_amount > 0:
            expected_tenure = total_pending // installment_amount
            assert expected_tenure == loan_tenure, f"loanTenure mismatch: expected {expected_tenure}, got {loan_tenure}"

        if loan_tenure > 0:
            expected_installment = total_pending // loan_tenure
            assert expected_installment == installment_amount, f"installmentAmount mismatch: expected {expected_installment}, got {installment_amount}"

        # Validate first repayment ledger for opening balance
        first_repayment = data.get("repayments", [])[0]
        assert first_repayment.get("repaymentStatus") == 7, "First repayment status should be 7 for opening balance"

        # Validate last installment due date matches repaymentEndDate
        repayments = [r for r in data.get("repayments", []) if r.get("installmentDueOn") != "0001-01-01T00:00:00"]
        assert repayments, "No valid installments found"
        last_installment = repayments[-1]
        last_due_date = datetime.fromisoformat(last_installment.get("installmentDueOn").replace("Z", "+00:00")).date()
        assert last_due_date == repayment_end_date, f"Last installment due date {last_due_date} != repaymentEndDate {repayment_end_date}"

        # Validate totalInstallments matches last installmentNumber (0-based)
        last_installment_number = last_installment.get("installmentNumber")
        assert total_installments == last_installment_number, f"totalInstallments {total_installments} != last installmentNumber {last_installment_number + 1}"

        loan_client.dispose()

    @allure.title("TC_006 - Verify that when isWithOpeningBalance = false and the disbursement date is in the past, the system should not allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_isWithOpeningBalanceFalse(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "isWithOpeningBalanceFalse.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 400 , f"POST request allowed to post with opening balance False, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        loan_client.dispose()

    @allure.title("TC_007 - Verify that when isWithOpeningBalance = true and the disbursement date is in the Future or Current, the system should not allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_isWithOpeningBalanceTrue(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "disbursementDateFutorCu.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 403, f"POST request allowed to post with isWithOpeningBalance = true and the disbursement date is in the Future or Current, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        loan_client.dispose()

    @allure.title("TC_008 - Verify that when Loan start date cannot be less than disbursement date, the system should not allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_LoanStartDateLesserDisbursement(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "startDategreaterThendisubersmnetDate.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 403, f"POST request allowed to post with Loan start date cannot be less than disbursement date, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        loan_client.dispose()

    @allure.title("TC_009 - Verify that opening balance filed remove or null, the system should not allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_OpeningBalanceFilledRemoveOrNull(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "openingbalanceFieldremoveorNull.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 400, f"POST request allowed to post opening balance filed remove or null, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        loan_client.dispose()

    @allure.title("TC_010 - Verify that Opening balance cannot exceed the loan amount, the system should not allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_OpeningBalanceExceed(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "loanamountLessThanOpeningBalance.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 400, f"POST request allowed to post Opening balance cannot exceed the loan amount, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        loan_client.dispose()

    @allure.title("TC_011 - Verify that Opening balance and Loan amount should be equal or less than equal, the system should  allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_OpenbalanceLoanAmountEqaul(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "LoanAmOpenBalanCEqual.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be allowed to post Opening balance and loan amount not equal greater loan amount, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3
        # Validate opening balance vs amount disbursed
        amount_disbursed = data.get("amountDisbursed", 0)
        opening_balance = data.get("openingBalance", 0)
        assert opening_balance <= amount_disbursed, f"Opening balance {opening_balance} cannot exceed amountDisbursed {amount_disbursed}"
        loan_client.dispose()

    @allure.title("TC_012 - Verify that disbursement date lesser than are equal to today, the system should  allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_disbursementLessThanToday(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "disbursementDateLessthanToday.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be allowed to post disbursement date lesser than are not equal to today, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))

        # Validate disbursement and approved dates
        disbursement_date_str = data.get("disbursementDate")
        assert disbursement_date_str, "disbursementDate is missing"
        disbursement_date = datetime.fromisoformat(disbursement_date_str.replace("Z", "+00:00")).date()
        today = date.today()
        assert disbursement_date <= today, f"disbursementDate {disbursement_date} is greater than today {today}"
        loan_client.dispose()


    @allure.title("TC_013 - Verify that Loan Start greater then disbursementDate, the system should  allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_LoanStratDateGreaterdisbursementDate(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "startDateGretterThanDisubDate.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be allowed to post disbursement date lesser than are not equal to today, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))


        disbursement_date_str = data.get("disbursementDate")
        repayment_start_str = data.get("repaymentStartDate")
        assert disbursement_date_str, "disbursementDate is missing"
        assert repayment_start_str, "repaymentDate is missing"
        repayment_start_date = datetime.fromisoformat(repayment_start_str.replace("Z", "+00:00")).date()
        disbursement_date = datetime.fromisoformat(disbursement_date_str.replace("Z", "+00:00")).date()
        assert repayment_start_date >= disbursement_date, f"disbursementDate {disbursement_date} < repaymentStartDate {repayment_start_date}"
        loan_client.dispose()

    @allure.title("TC_014 - Verify that Loan Start date is equal to today date or lesser than today or greater than today, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_LoanStratEqualToday(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "startDateGretterThanDisubDate.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be not allowed to post Loan Start date is equal to today date or lesser that to today or greater today, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))

        disbursement_date_str = data.get("disbursementDate")
        repayment_start_str = data.get("repaymentStartDate")
        today = date.today()
        repayment_start_date = datetime.fromisoformat(repayment_start_str.replace("Z", "+00:00")).date()
        disbursement_date = datetime.fromisoformat(disbursement_date_str.replace("Z", "+00:00")).date()

        # repayment_start_date should be:
        # 1. Equal to today, OR
        # 2. Equal to disbursement_date, OR
        # 3. Before today, OR
        # 4. After today
        # → In short: it must be a valid date, not null

        assert repayment_start_date, "repaymentStartDate is missing"

        if repayment_start_date == today:
            assert True, f"✅ repaymentStartDate {repayment_start_date} is equal to today {today}"
        elif repayment_start_date == disbursement_date:
            assert True, f"✅ repaymentStartDate {repayment_start_date} is equal to disbursementDate {disbursement_date}"
        elif repayment_start_date < today:
            assert True, f"✅ repaymentStartDate {repayment_start_date} is less than today {today}"
        elif repayment_start_date > today:
            assert True, f"✅ repaymentStartDate {repayment_start_date} is greater than today {today}"
        else:
            assert False, f"❌ repaymentStartDate {repayment_start_date} is invalid"

        data = response.json()
        print(json.dumps(data, indent=2))
        loan_client.dispose()



    @allure.title("TC_015 - Verify that OpeningBalanceTrue means outsidePayrollPayment(with) Field Non Mandatory, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_outsidePayrollPaymentMandatory(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "WithoutsidePayrollPayment.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))

        assert data.get("isWithOpeningBalance") == True, "isWithOpeningBalance is not true"
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3
        # Validate outsidePayrollPaymentDetails
        if data.get("isWithOpeningBalance"):
            outside_payment = data.get("outsidePayrollPaymentDetails")
            assert outside_payment not in (None, [], {},
                                           ""), "outsidePayrollPaymentDetails required for opening balance"

            # Pay mode checks
            pay_mode = outside_payment.get("payMode")
            if pay_mode == 1:
                assert outside_payment.get("paymentDetails", {}).get(
                    "referenceNo"), "referenceNo is mandatory for payMode=1"
            elif pay_mode == 2:
                assert outside_payment.get("companyBankAccountId"), "companyBankAccountId mandatory for payMode=2"
            elif pay_mode == 3:
                assert outside_payment.get("paymentDetails", {}).get("notes"), "notes mandatory for payMode=3"

        loan_client.dispose()

    @allure.title(
        "TC_016 - Verify that OpeningBalanceTrue means outsidePayrollPayment(without) Field Remove Non Mandatory, system should  allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_outsidePayrollPaymentRemoveOrNull(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "WithOUToutsidePayrollPayment.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)
        #Disubermnet channel is mandorty for outsidePayrollPayment with
        assert response.status == 400, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 11, "loanStatus not 100 (success)"


        assert data.get("isWithOpeningBalance") == True, "isWithOpeningBalance is not true"
        assert data.get("outsidePayrollPaymentDetails") is None, f"Expected outsidePayrollPaymentDetails to be null, but got {data.get('outsidePayrollPaymentDetails')}"

        loan_client.dispose()

    @allure.title(
        "TC_017 - Verify that disbursementChannel(with) Filed Non Mandatory, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_WithdisbursementChannel(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "disbursementChannelWith.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))

        assert data.get("disbursementChannel") == 2, f"POST request cannot be allowed to disbursementChannel , status {response.status}"
        loan_client.dispose()


    @allure.title(
        "TC_018 - Verify that disbursementChannel(without) Filed Non Mandatory, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_WithOutdisbursementChannel(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "disbursementChannelWithout.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 400, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        #assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        #assert data.get("recordSource") == 3
        #assert data.get(
        #    "disbursementChannel") is None, f"Expected disbursementChannel to be null, but got {data.get('outsidePayrollPaymentDetails')}"

        loan_client.dispose()

    @allure.title(
        "TC_019 - Verify that Pay mode 1, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_payMode1(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "payMode1.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3
        assert data.get("outsidePayrollPaymentDetails", {}).get("paymentDetails", {}).get("referenceNo") == \
               payload.get("outsidePayrollPayment", {}).get("paymentDetails", {}).get("referenceNo"), \
            "referenceNo mismatch between payload and response"

        assert data.get("outsidePayrollPaymentDetails", {}).get("paymentDetails", {}).get("notes") is None
        assert data.get("outsidePayrollPaymentDetails", {}).get("companyBankAccountId") is None

        loan_client.dispose()

    @allure.title(
        "TC_020 - Verify that Pay mode 2, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_payMode2(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "payMode2.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3
        assert data.get("outsidePayrollPaymentDetails", {}).get("companyBankAccountId") == \
               payload.get("outsidePayrollPayment", {}).get("companyBankAccountId"), \
            "companyBankAccountId mismatch between payload and response"

        assert data.get("outsidePayrollPaymentDetails", {}).get("paymentDetails") is None
        loan_client.dispose()

    @allure.title(
        "TC_021 - Verify that Pay mode 3, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_payMode3(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "payMode3.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3

        assert data.get("outsidePayrollPaymentDetails", {}).get("paymentDetails", {}).get("notes") == \
               payload.get("outsidePayrollPayment", {}).get("paymentDetails", {}).get("notes"), \
            "notes mismatch between payload and response"

        assert data.get("outsidePayrollPaymentDetails", {}).get("paymentDetails", {}).get("referenceNo") is None
        assert data.get("outsidePayrollPaymentDetails", {}).get("companyBankAccountId") is None

        loan_client.dispose()

    @allure.title(
        "TC_022 - Verify that openingBalance is there should be same amount for amount paid, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_amountPaid(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "ValAmaountPaid.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3
        assert data.get("outsidePayrollPaymentDetails",{}).get("amountPaid") == data.get("openingBalance"), f"POST openingBalance is there should be same amount for amount paid, system should not allow creating (POST) a loan record."

        loan_client.dispose()

    @allure.title(
        "TC_023 - Verify that opening repayment should be validate, system should allow creating (POST) a loan record.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_repaymentOpeningLedger(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "ValAmaountPaid.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        assert response.status == 200, f"POST request can be OpeningBalanceTrue means outsidePayrollPayment(with) Field Mandatory, status {response.status}"
        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 100, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 3

        if data.get("isWithOpeningBalance") == True:
            # Ensure 'repayments' exists and has at least one element
            repayments = data.get("repayments", [])
            assert repayments, "No repayments found in response"

            # Check first repayment status
            first_repayment = repayments[0]
            assert first_repayment.get("repaymentStatus") == 7, (
                f"Expected first repaymentStatus 7, but got {first_repayment.get('repaymentStatus')}"
            )

            assert first_repayment.get("totalAmountRemaining") == data.get("openingBalance")

            assert first_repayment.get("installmentNumber") == 0

            assert data.get("amountDisbursed") - data.get("openingBalance") == first_repayment.get("totalAmountRepaid")

            assert first_repayment.get("repaymentMode") == 0

            loan_client.dispose()

    """Without Opening Balance"""

    @allure.title("TC_024 - Verify that a loan record can be created without opening balance.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_withoutOpeningBalance(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "withoutOpeningBalance.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        #validate the response status 200
        assert response.status == 200, f"POST request failed with opening balance Not allowed, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))
        print("Employee Code: ", data.get("employeeCode"))
        assert data.get("loanStatus") == 11, "loanStatus not 100 (success)"
        assert data.get("recordSource") == 2
        #validate the isWithOpeningBalance is true
        assert data.get("isWithOpeningBalance") == False, "isWithOpeningBalance is not true"

        # Validate disbursement and approved dates
        disbursement_date_str = data.get("disbursementDate")
        approved_date_str = data.get("approvedDate")
        repayment_start_str = data.get("repaymentStartDate")
        repayment_end_str = data.get("repaymentEndDate")

        assert disbursement_date_str, "disbursementDate is missing"
        disbursement_date = datetime.fromisoformat(disbursement_date_str.replace("Z", "+00:00")).date()
        approved_date = datetime.fromisoformat(approved_date_str.replace("Z", "+00:00")).date()
        repayment_start_date = datetime.fromisoformat(repayment_start_str.replace("Z", "+00:00")).date()
        repayment_end_date = datetime.fromisoformat(repayment_end_str.replace("Z", "+00:00")).date()
        today = date.today()

        assert disbursement_date >= today, f"disbursementDate {disbursement_date} is Lesser than today {today}"
        assert disbursement_date == approved_date, f"disbursementDate {disbursement_date} != approvedDate {approved_date}"
        assert disbursement_date >= repayment_start_date, f"disbursementDate {disbursement_date} < repaymentStartDate {repayment_start_date}"

        # Validate totalInstallments based on start/end dates
        total_installments = data.get("totalInstallments")
        diff = relativedelta(repayment_end_date, repayment_start_date)
        expected_installments = diff.years * 12 + diff.months + 1
        assert total_installments == expected_installments, (
            f"Installments mismatch: expected {expected_installments}, got {total_installments}"
        )
        expected_end_date = repayment_start_date + relativedelta(months=total_installments - 1)
        assert repayment_end_date == expected_end_date, f"Repayment end date mismatch: expected {expected_end_date}, got {repayment_end_date}"

        # Validate pendingInstallments
        assert total_installments == data.get("pendingInstallments"), "totalInstallments != pendingInstallments"

        # Validate opening balance vs amount disbursed
        amount_disbursed = data.get("amountDisbursed", 0)
        opening_balance = data.get("openingBalance", 0)
        assert opening_balance <= amount_disbursed, f"Opening balance {opening_balance} cannot exceed amountDisbursed {amount_disbursed}"

        # Validate totalAmountRePaid ≤ (amountDisbursed - openingBalance)
        total_amount_repaid = data.get("totalAmountRePaid", 0)
        expected_repaid = amount_disbursed - opening_balance
        assert total_amount_repaid <= expected_repaid, f"totalAmountRePaid {total_amount_repaid} > {expected_repaid}"

        # Validate outsidePayrollPaymentDetails
        assert data.get("outsidePayrollPaymentDetails") is None, "outsidePayrollPaymentDetails not set"


        # Validate repaymentCalculations
        repayment_calc = data.get("repaymentCalculations", {})
        total_pending = data.get("totalAmountPending", 0)
        installment_amount = repayment_calc.get("installmentAmount", 0)
        loan_tenure = repayment_calc.get("loanTenure", 0)

        if installment_amount > 0:
            expected_tenure = total_pending // installment_amount
            assert expected_tenure == loan_tenure, f"loanTenure mismatch: expected {expected_tenure}, got {loan_tenure}"

        if loan_tenure > 0:
            expected_installment = total_pending // loan_tenure
            assert expected_installment == installment_amount, f"installmentAmount mismatch: expected {expected_installment}, got {installment_amount}"

        # Validate first repayment ledger for opening balance
        first_repayment = data.get("repayments", [])[0]
        assert first_repayment.get("repaymentStatus") == 1, "First repayment status should be 7 for opening balance"

        # Validate last installment due date matches repaymentEndDate
        repayments = [r for r in data.get("repayments", []) if r.get("installmentDueOn") != "0001-01-01T00:00:00"]
        assert repayments, "No valid installments found"
        last_installment = repayments[-1]
        last_due_date = datetime.fromisoformat(last_installment.get("installmentDueOn").replace("Z", "+00:00")).date()
        assert last_due_date == repayment_end_date, f"Last installment due date {last_due_date} != repaymentEndDate {repayment_end_date}"

        # Validate totalInstallments matches last installmentNumber (0-based)
        last_installment_number = last_installment.get("installmentNumber")
        assert total_installments == last_installment_number, f"totalInstallments {total_installments} != last installmentNumber {last_installment_number + 1}"

        loan_client.dispose()

    @allure.title("TC_025 - Verify that without Balance and disbursement past system should not allowed to post.")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_disbursementPast(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "disbursmentPAST.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 400, f"Opening balance is mandatory when disbursement date is in the past, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))

        loan_client.dispose()


        #FalseOUtsidePyaroll

    @allure.title("TC_026 - Verify that without Opening Balance send the outside payroll Payment .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_FalseSendOutSIdePayroll(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "FalseOUtsidePyaroll.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 400, f"Opening balance is mandatory when disbursement date is in the past, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))

        loan_client.dispose()

    @allure.title("TC_027 - Verify that without Opening Balance send the disbursement channel .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_FalseDischannel(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "FalsedisbursementChannel.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 400, f"Opening balance is mandatory when disbursement date is in the past, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))

        loan_client.dispose()

    @allure.title("TC_028 - Verify that validat date disbursementDate and StartDate .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_Date(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "date.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 200, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 11
        assert data.get("recordSource") == 2
        disbursement_date_str = data.get("disbursementDate")
        approved_date_str = data.get("approvedDate")
        repayment_start_str = data.get("repaymentStartDate")

        disbursement_date = datetime.fromisoformat(disbursement_date_str.replace("Z", "+00:00")).date()
        approved_date = datetime.fromisoformat(approved_date_str.replace("Z", "+00:00")).date()
        repayment_start_date = datetime.fromisoformat(repayment_start_str.replace("Z", "+00:00")).date()
        today = date.today()

        assert disbursement_date >= today, f"disbursementDate {disbursement_date} is Lesser than today {today}"
        assert disbursement_date == approved_date, f"disbursementDate {disbursement_date} != approvedDate {approved_date}"
        assert disbursement_date <= repayment_start_date, f"disbursementDate {disbursement_date} < repaymentStartDate {repayment_start_date}"

        loan_client.dispose()

    @allure.title("TC_029 - Verify that Validate the with reason .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_WithReason(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "Withreason.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 200, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 11
        assert data.get("recordSource") == 2
        assert data.get("reason"), f"reason is missing"
        assert data.get("reason") == payload.get("reason"), "reason mismatch between payload and response"
        loan_client.dispose()

    @allure.title("TC_030 - Verify that Validate the with out reason .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_WithOutReason(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "WithOutreason.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 200, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 11
        assert data.get("recordSource") == 2
        assert data.get("reason") is None, "reason mismatch between payload and response"
        loan_client.dispose()

    @allure.title("TC_031 - Verify that Validate repayment Mode 1 .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_repaymentMode1(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "repaymentMode1.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 200, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 11
        assert data.get("recordSource") == 2

        repayment_calc = data.get("repaymentCalculations", {})
        total_pending = float(data.get("totalAmountPending", 0))
        installment_amount = float(repayment_calc.get("installmentAmount", 0))
        loan_tenure = repayment_calc.get("loanTenure", 0)

        if loan_tenure > 0:
            expected_installment = round(total_pending / loan_tenure, 2)  # round to 2 decimals
            assert round(installment_amount, 2) == expected_installment, (
                f"installmentAmount mismatch: expected {expected_installment}, got {installment_amount}"
            )

        if installment_amount > 0:
            expected_tenure = round(total_pending / installment_amount)
            assert expected_tenure == loan_tenure, (
                f"loanTenure mismatch: expected {expected_tenure}, got {loan_tenure}"
            )
        loan_client.dispose()

    @allure.title("TC_032 - Verify that Validate repayment Mode 2 .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_repaymentMode2(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "repaymentMode2.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 200, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))
        assert data.get("loanStatus") == 11
        assert data.get("recordSource") == 2

        repayment_calc = data.get("repaymentCalculations", {})
        total_pending = float(data.get("totalAmountPending", 0))
        installment_amount = float(repayment_calc.get("installmentAmount", 0))
        loan_tenure = repayment_calc.get("loanTenure", 0)

        if loan_tenure > 0:
            expected_installment = round(total_pending / loan_tenure, 2)  # round to 2 decimals
            assert round(installment_amount, 2) == expected_installment, (
                f"installmentAmount mismatch: expected {expected_installment}, got {installment_amount}"
            )

        if installment_amount > 0:
            expected_tenure = round(total_pending / installment_amount)
            assert expected_tenure == loan_tenure, (
                f"loanTenure mismatch: expected {expected_tenure}, got {loan_tenure}"
            )

        loan_client.dispose()

    @allure.title("TC_033 - Verify that Validate without installmentAmount  send repayment Mode 1 .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_WithoutInstallmentAmount(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "WithoutinstallmentAmount.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 403, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))

        loan_client.dispose()

    @allure.title("TC_034 - Verify that Validate without Tenure send repayment Mode 1 .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_WithoutTenure(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "WithoutTenure.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 403, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))

        loan_client.dispose()

    @allure.title("TC_035 - Verify that inactive loan system should not allowed to post .")
    @pytest.mark.parametrize("companyId", ["3a1a417d-51c2-bab1-6b7f-5b97cd6a53f8"])
    def test_POST_inactiveLoan(self, playwright, companyId):
        loan_client = LoanAPI(playwright, BASE_URL, TOKEN)
        payload_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "data", "loan", "inactiveLoan.json"
        )
        with open(payload_path, "r") as f:
            payload = json.load(f)
        # Make POST request
        response = loan_client.post_loans(companyId, payload)

        # validate the response status 200
        assert response.status == 403, f"validat date disbursementDate and StartDate, status {response.status}"

        data = response.json()
        print(json.dumps(data, indent=2))

        loan_client.dispose()