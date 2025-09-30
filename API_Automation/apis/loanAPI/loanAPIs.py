from API_Automation.utils.api_client import BaseClient

class LoanAPI(BaseClient):
    def get_loans(self, company_id: str):
        endpoint = f"/api/CompBenefits/companies/{company_id}/loans"
        return self.get(endpoint)

    def post_loans(self, company_id: str, payload: dict):
        endpoint = f"/api/CompBenefits/companies/{company_id}/loans"
        return self.post(endpoint, payload)
