import json
import time

import pytest
from playwright.sync_api import expect, Page

loginfile = r"C:\Users\Comm-IT India\OneDrive - comm-it india pvt ltd\Desktop\SahabPayroll\Playwright_Automation\resources\weblogin\loginDetails.json"
with open(loginfile) as jsonFile:
    login = json.load(jsonFile)


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.companyLogo = page.get_by_role("link", name="Connexions - Accounts")
        self.enterButton = page.get_by_text("Enter")
            #page.locator("#AbpTenantSwitchLink")page.get_by_text("Enter")
        self.tenantModal = page.get_by_role("textbox", name="Enter your Oranganisation Name")
            #page.locator("//div[@class='modal-content']")


        self.cancelButton = page.get_by_role("button", name="Cancel")
        self.closeIcon = page.get_by_role("button", name="Close")
        self.tenantNameField = page.get_by_role("textbox", name="Enter your Oranganisation Name")
        self.saveButton = page.get_by_role("button", name=" Save")
        self.usernameField = page.get_by_role("textbox", name="Username or email address")
        self.passwordField = page.get_by_role("textbox", name="Password")
        self.passwordVisibilityToggle = page.locator("#PasswordVisibilityButton")
        self.loginButton = page.locator("button[name=\"Action\"]")
        self.alertPopup = page.get_by_text("× Given tenant doesn't exist")
        self.alertPopupOK = page.get_by_role("button", name="Ok")
        self.rememberMeCheckbox = page.get_by_role("checkbox", name="Remember me")

        self.rememberMeUnCheckbox = page.get_by_role("checkbox", name="Remember me")

        self.langDropdown = page.get_by_role("button", name="English")

        self.langArabic = page.get_by_role("link", name="العربية")

        self.usernameError = page.get_by_text("The Username or email address")

        self.passwordError = page.get_by_text("The Password field is")

        self.forgotPassword = page.get_by_role("link", name="Forgot password?")

    def logVisible(self):
        try:
            expect(self.companyLogo).to_be_visible(timeout=3000)
            print("✅ Logo is Visible")
        except Exception as e:
            pytest.fail(f"❌ Logo not visible: {e}")

    def enterButtonClick(self):
        try:
            expect(self.enterButton).to_be_visible(timeout=5000)
            expect(self.enterButton).to_be_enabled(timeout=5000)
            self.enterButton.click()
            print("✅ Enter button clicked successfully")
        except Exception as e:
            print(f"❌ Error: {e} - Enter button click failed")
            pytest.fail("Enter button click failed - Test case failed")

    def tenantPopupVisible(self):
        try:
            expect(self.tenantModal).to_be_visible(timeout=10000)
            print("✅ Tenant popup is visible")
        except Exception as e:
            self.page.screenshot(path="tenant_popup_error.png")
            print(f"❌ Error: {e} - Tenant popup is not visible")
            pytest.fail("Tenant popup is not visible - Test case failed")

    """
    def tenantPopupVisible(self, retries=3, delay=2):
        for i in range(retries):
            try:
                self.tenantModal.wait_for(state="visible", timeout=5000)
                print("✅ Tenant popup is visible")
                return
            except Exception:
                if i < retries - 1:
                    self.page.wait_for_timeout(delay * 1000)
                else:
                    self.page.screenshot(path="tenant_popup_error.png")
                    pytest.fail("Tenant popup is not visible after retries")
    """

    def cancelBtnClick(self):
        try:
            expect(self.cancelButton).to_be_visible(timeout=3000)
            expect(self.cancelButton).to_be_enabled()
            self.cancelButton.click()
            print("✅ Cancel Button Clicked")
        except Exception as e:
            pytest.fail(f"❌ Cancel Button issue: {e}")

    def closeIconClick(self):
        try:
            expect(self.closeIcon).to_be_visible(timeout=3000)
            expect(self.closeIcon).to_be_enabled()
            self.closeIcon.click()
            print("✅ Close Icon Clicked")
        except Exception as e:
            pytest.fail(f"❌ Close Icon issue: {e}")

    def tenantName(self):
        try:
            expect(self.tenantNameField).to_be_visible(timeout=3000)
            expect(self.tenantNameField).to_be_enabled()
            self.tenantNameField.fill(login["OrganisationName"])
            print("✅ Tenant Name Filled")
        except Exception as e:
            pytest.fail(f"❌ Tenant Name issue: {e}")

    def saveBtnClick(self):
        try:
            expect(self.saveButton).to_be_visible(timeout=3000)
            expect(self.saveButton).to_be_enabled()
            self.saveButton.click()
            print("✅ Save Button Clicked")
        except Exception as e:
            pytest.fail(f"❌ Save Button issue: {e}")

    def username(self):
        try:
            time.sleep(3)
            expect(self.usernameField).to_be_visible(timeout=5000)
            expect(self.usernameField).to_be_enabled()
            self.usernameField.fill(login["UserName"])
            print("✅ Username Filled")
        except Exception as e:
            pytest.fail(f"❌ Username issue: {e}")

    def password(self):
        try:
            expect(self.passwordField).to_be_visible(timeout=5000)
            expect(self.passwordField).to_be_enabled()
            self.passwordField.fill(login["Password"])
            print("✅ Password Filled")
        except Exception as e:
            pytest.fail(f"❌ Password issue: {e}")

    def passwordIconVisibleClick(self):
        try:
            expect(self.passwordIconVisible).to_be_visible(timeout=3000)
            self.passwordIconVisible.click()
            print("✅ Password Visible Icon Clicked")
        except Exception as e:
            pytest.fail(f"❌ Password Visible Icon issue: {e}")

    def passwordIconDeVisibleClick(self):
        try:
            expect(self.passwordIconDeVisible).to_be_visible(timeout=3000)
            self.passwordIconDeVisible.click()
            print("✅ Password DeVisible Icon Clicked")
        except Exception as e:
            pytest.fail(f"❌ Password DeVisible Icon issue: {e}")

    def signin(self):
        try:
            expect(self.loginButton).to_be_visible(timeout=3000)
            expect(self.loginButton).to_be_enabled()
            self.loginButton.click()
            print("✅ Login Button Clicked")
        except Exception as e:
            pytest.fail(f"❌ Login Button issue: {e}")

    def alertPopupVisible(self):
        try:
            expect(self.alertPopup).to_be_visible(timeout=3000)
            print("✅ Alert Popup Visible")
        except Exception as e:
            pytest.fail(f"❌ Alert Popup issue: {e}")

    def alertPopupOKClick(self):
        try:
            expect(self.alertPopupOK).to_be_visible(timeout=3000)
            expect(self.alertPopupOK).to_be_enabled()
            self.alertPopupOK.click()
            print("✅ Alert Popup OK Clicked")
        except Exception as e:
            pytest.fail(f"❌ Alert Popup OK issue: {e}")

    def rememberMeCheckClick(self):
        try:
            expect(self.rememberMeCheckbox).to_be_visible(timeout=3000)
            expect(self.rememberMeCheckbox).to_be_enabled()
            self.rememberMeCheckbox.check()
            print("✅ Remember Me Checked")
        except Exception as e:
            pytest.fail(f"❌ Remember Me Check issue: {e}")

    def rememberMeUncheckClick(self):
        try:
            expect(self.rememberMeCheckbox).to_be_visible(timeout=3000)
            expect(self.rememberMeCheckbox).to_be_enabled()
            self.rememberMeCheckbox.uncheck()
            print("✅ Remember Me Unchecked")
        except Exception as e:
            pytest.fail(f"❌ Remember Me Uncheck issue: {e}")

    def langDropdownClick(self):
        try:
            expect(self.langDropdown).to_be_visible(timeout=3000)
            expect(self.langDropdown).to_be_enabled()
            self.langDropdown.click()
            print("✅ Language Dropdown Clicked")
        except Exception as e:
            pytest.fail(f"❌ Language Dropdown issue: {e}")

    def langArabicClick(self):
        try:
            expect(self.langArabic).to_be_visible(timeout=3000)
            expect(self.langArabic).to_be_enabled()
            self.langArabic.click()
            print("✅ Arabic Language Selected")
        except Exception as e:
            pytest.fail(f"❌ Arabic Language issue: {e}")

    def usernameErrorVisible(self):
        try:
            expect(self.usernameError).to_be_visible(timeout=3000)
            print("✅ Username Error Visible")
        except Exception as e:
            pytest.fail(f"❌ Username Error not visible: {e}")

    def passwordErrorVisible(self):
        try:
            expect(self.passwordError).to_be_visible(timeout=3000)
            print("✅ Password Error Visible")
        except Exception as e:
            pytest.fail(f"❌ Password Error not visible: {e}")
