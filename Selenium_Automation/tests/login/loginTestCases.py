import time

import pytest
from Selenium_Automation.utils.basPage import basePage
from Selenium_Automation.pages.login.loginPage import loginPage

class TestLogin:



    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_page = basePage()
        self.driver = self.base_page.driver
        self.base_page.getURL()
        self.base_page.redirectURL()
        self.base_page.keepOpen()
        self.login_page = loginPage(self.driver)  # ← pass the driver


    def test_loginLogoVisisbleTC_001(self):
        try:
            self.login_page.logoVisible()
            print("Company logo is visible.")
        except Exception as e:
            print(f"Error: {e} - Logo is not visible - Test Case Failed")
            pytest.fail("Logo is not visible - Test case failed")

        finally:
            self.base_page.closeDriver()


    def test_eneterValidTennatNameTC_002(self):
        tenantName = "mscan"
        # data will be get hard core

        try:
            self.login_page.eneterButtonClick()
            time.sleep(3)
            print("Enter button clicked successfully.")
            self.login_page.tenatPoupVisible()
            time.sleep(3)
            print("Tenant popup is visible.")
            time.sleep(3)
            self.login_page.enterTenantName(tenantName)
            print(tenantName)
            time.sleep(3)
            self.login_page.saveTenant()
            print("Tenant name entered successfully.")
            time.sleep(3)
        except Exception as e:
            print(f"Error: {e} - Tenant name entry failed - Test Case Failed")
            pytest.fail("Tenant name entry failed - Test case failed")

        finally:
            self.base_page.closeDriver()


    def test_loginPageTitleTC_003(self):
        tenantName = "mscan"
        userName = "syed.mohamed@comm-it.in"
        password = "Admin@123"
        try:
            self.login_page.eneterButtonClick()
            time.sleep(3)
            print("Enter button clicked successfully.")
            self.login_page.tenatPoupVisible()
            time.sleep(3)
            print("Tenant popup is visible.")
            time.sleep(3)
            self.login_page.enterTenantName(tenantName)
            print("Tenant name entered successfully.")
            time.sleep(3)
            self.login_page.saveTenant()
            time.sleep(3)
            self.login_page.useName(userName)
            print("User name entered successfully.")
            time.sleep(3)
            self.login_page.password(password)
            print("Password entered successfully.")
            time.sleep(3)
            self.login_page.loginButtonClick()
            print("Login button clicked successfully.")
            time.sleep(5)

        except Exception as e:
            print(f"Error: {e} - Page title verification failed - Test Case Failed")
            pytest.fail("Page title verification failed - Test case failed")

        finally:
            self.base_page.closeDriver()
