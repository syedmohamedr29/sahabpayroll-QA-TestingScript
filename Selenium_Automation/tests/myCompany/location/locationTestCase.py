import time

import pytest
from utils.basPage import basePage
from pages.navigate2ndURL.companySelect import companySelect
from pages.navigate2ndURL.navBar import navigate
from pages.login.loginPage import loginPage
from pages.myCompanyPage.company.myCompany import MyCompany
from pages.myCompanyPage.location.locationPage import Location

class TestCasesLocation:
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

        self.login_page = loginPage(self.driver)  # ← pass the driver
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
        self.selectBtn.locationBtnClick()
        time.sleep(3)

        self.location_page = Location(self.driver)  # ← pass the driver

    def test_add_location(self):

        LocationNameEn = "Test Location"
        LocationNameAr = "موقع الاختبار"
        shortCode = "AGS"
        addressLine1 = "123 Test Street"
        addressLine2 = "Test Data"
        state = "Jeddah"
        city = "Jeddah"
        pincode = "123456"

        try:
            """ Test case to add a new location """
            time.sleep(5)
            self.location_page.clickLocationAddBtn()
            self.location_page.enterEnName(LocationNameEn)
            self.location_page.enterArName(LocationNameAr)
            self.location_page.enterShortCode(shortCode)
            self.location_page.enterAddressLine1(addressLine1)
            self.location_page.enterAddressLine2(addressLine2)
            self.location_page.selectCountry()
            self.location_page.enterState(state)
            self.location_page.enterCity(city)
            self.location_page.enterPincode(pincode)
            self.location_page.clickAddBtn()
            time.sleep(5)

        except Exception as e:
            print(f"An error occurred while adding the location: {e}")
            assert False, f"Test failed due to an error: {e}"

        finally:
            self.base_page.closeDriver()




