import time

import pytest
from utils.basPage import basePage
from pages.navigate2ndURL.companySelect import companySelect
from pages.navigate2ndURL.navBar import navigate
from pages.login.loginPage import loginPage
from pages.myCompanyPage.company.myCompany import MyCompany
from pages.myCompanyPage.deisgnation.designationPage import designation


class TestDesignation:
    tenantName = "mscan"
    userName = "syed.mohamed@comm-it.in"
    password = "Admin@1234"

    @pytest.fixture(autouse=True)
    def setup(self, tenantName=tenantName, userName=userName, password=password):

        ''' Setup method to initialize the base page and login page '''
        self.base_page = basePage()
        self.driver = self.base_page.driver
        self.base_page.getURL()
        self.base_page.redirectURL()
        self.base_page.keepOpen()

        ''' Login to the application '''

        self.login_page = loginPage(self.driver) # ← pass the driver
        self.login_page.eneterButtonClick()
        time.sleep(3)
        self.login_page.enterTenantName(tenantName)
        time.sleep(3)
        self.login_page.saveTenant()
        time.sleep(3)
        self.login_page.useName(userName)
        time.sleep(3)
        self.login_page.password(password)
        time.sleep(3)
        self.login_page.loginButtonClick()
        time.sleep(15)

        self.company_select = companySelect(self.driver)  # ← pass the driver
        self.company_select.selectLastCompany()
        self.company_select.continueBtn()
        time.sleep(5)


        self.nav_menu = navigate(self.driver)  # ← pass the driver
        self.nav_menu.switchV2()
        time.sleep(30)
        """ Navigate to the Designation page """
        self.selectBtn = MyCompany(self.driver)  # ← pass the driver
        self.selectBtn.designationBtnClick()
        time.sleep(3)
        self.designation_page = designation(self.driver)  # ← pass the driver




    def test_designationPageTitleTC_001(self):
        try:
            time.sleep(5)
            """ Check if the Designation page title is correct """
            self.designation_page.clickDesignationAddBtn()
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e} - Designation page title check failed - Test Case Failed")
            pytest.fail("Designation page title check failed - Test case failed")
        finally:
            self.base_page.closeDriver()


