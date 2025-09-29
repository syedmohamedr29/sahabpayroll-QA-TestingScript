class LoanAPI:
    ENDPOINT = "/api/CompBenefits/companies/{company_id}/loans"

    @staticmethod
    def get_loans(request_context, company_id: str):
        response = request_context.get(LoanAPI.ENDPOINT.format(company_id=company_id))
        return response
