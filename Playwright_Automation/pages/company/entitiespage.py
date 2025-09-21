import pytest
from playwright.sync_api import expect, Page

class Entities:

    def __init__(self, page: Page):
        self.page = page

        self.AddCompanyBtn = page.get_by_role("button", name=" Company")


    def addCompanyBtn(self):

        try:
            expect(self.AddCompanyBtn).to_be_visible(timeout=3000)
            expect(self.AddCompanyBtn).to_be_enabled()
            self.AddCompanyBtn.click()
            print("✅ Add Company Button is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Add Company Button is Not Visible and Not clickable: {e}")