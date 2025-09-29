import json

class LoanAPI:
    LandingPage_ENDPOINT = "/api/CompBenefits/companies/{company_id}/loans"
    PostAPI_ENDPOINT = "/api/CompBenefits/companies/{companyId}/loans"

    @staticmethod
    def get_loans_LandingPageAPI(request_context, company_id: str):
        response = request_context.get(LoanAPI.LandingPage_ENDPOINT.format(company_id=company_id))
        return response

    @staticmethod
    def loan_POSTAPI(request_context, company_id: str, payload: dict):
        """
        Sends a POST request to create a loan for a company.
        """
        response = request_context.post(
            LoanAPI.PostAPI_ENDPOINT.format(companyId=company_id),
            data=json.dumps(payload)
        )
        return response