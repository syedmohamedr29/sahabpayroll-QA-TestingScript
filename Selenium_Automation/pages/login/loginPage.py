from selenium.webdriver.common.by import By
import pytest

class loginPage():

    companyLogo = (By.XPATH, "//a[contains(@class,'brand')]/img[@alt='Connexions - Accounts']")
    enterButton = (By.ID, "AbpTenantSwitchLink")
    tenantModal = (By.XPATH, "//div[@class='modal-content']")
    tenatCancelButton = (By.XPATH, "//button[contains(@class,'btn btn-secondary')]")
    tenantCloseIcon = (By.XPATH, "//button[@aria-label='Close']")
    tenantNameField = (By.ID, "Input_Name")
    saveTenantButton = (By.XPATH, "//button[contains(@class,'btn btn-primary')]")
    usernameField = (By.ID, "LoginInput_UserNameOrEmailAddress")
    passwordField = (By.ID, "LoginInput_Password")
    loginButton = (By.XPATH, "//div//button[@value = 'Login']")
    alertPopup = (By.XPATH, "//div[@aria-live='assertive']")
    passwordToggle = (By.ID, "PasswordVisibilityButton")
    rememberMe = (By.ID, "LoginInput_RememberMe")
    langDropdown = (By.ID, "dropdownMenuLink")
    langArabic = (By.XPATH, "//a[@class = 'dropdown-item']")
    usernameError = (By.ID, "LoginInput_UserNameOrEmailAddress-error")
    passwordError = (By.ID, "LoginInput_Password-error")



    def __init__(self, driver):
        self.driver = driver


#-----------------------------------------------------------------------------------------

    def logoVisible(self):
        """Check if the company logo is visible."""
        try:
            self.driver.implicitly_wait(5)
            logo = self.driver.find_element(*self.companyLogo)
            assert logo.is_displayed(), "Company logo should be visible"
        except Exception as e:
            print(f"Error: {e} - Logo is not visible - Test Case Failed")
            pytest.fail("Logo is not visible - Test case failed")


    def eneterButtonClick(self):
        """Click the Enter button."""
        try:
            self.driver.implicitly_wait(5)
            enter_button = self.driver.find_element(*self.enterButton)
            enter_button.click()
        except Exception as e:
            print(f"Error: {e} - Enter button click failed - Test Case Failed")
            pytest.fail("Enter button click failed - Test case failed")

    def tenatPoupVisible(self):
        """Check if the tenant popup is visible."""
        try:
            self.driver.implicitly_wait(5)
            tenant_popup = self.driver.find_element(*self.tenantModal)
            assert tenant_popup.is_displayed(), "Tenant popup should be visible"
        except Exception as e:
            print(f"Error: {e} - Tenant popup is not visible - Test Case Failed")
            pytest.fail("Tenant popup is not visible - Test case failed")

    def cancelPopup(self):
        """Click the cancel button in the tenant popup."""
        try:
            self.driver.implicitly_wait(5)
            cancel_button = self.driver.find_element(*self.tenatCancelButton)
            cancel_button.click()
        except Exception as e:
            print(f"Error: {e} - Cancel button click failed - Test Case Failed")
            pytest.fail("Cancel button click failed - Test case failed")

    def closeIcon(self):
        """Click the close icon in the tenant popup."""
        try:
            self.driver.implicitly_wait(5)
            close_icon = self.driver.find_element(*self.tenantCloseIcon)
            close_icon.click()
        except Exception as e:
            print(f"Error: {e} - Close icon click failed - Test Case Failed")
            pytest.fail("Close icon click failed - Test case failed")

    def enterTenantName(self, tenant_name):
        """Enter the tenant name in the tenant popup."""
        try:
            self.driver.implicitly_wait(5)
            tenant_name_field = self.driver.find_element(*self.tenantNameField)
            tenant_name_field.send_keys(tenant_name)
        except Exception as e:
            print(f"Error: {e} - Tenant name entry failed - Test Case Failed")
            pytest.fail("Tenant name entry failed - Test case failed")

    def saveTenant(self):
        """Click the save button in the tenant popup."""
        try:
            self.driver.implicitly_wait(5)
            save_button = self.driver.find_element(*self.saveTenantButton)
            save_button.click()
        except Exception as e:
            print(f"Error: {e} - Save button click failed - Test Case Failed")
            pytest.fail("Save button click failed - Test case failed")

    def alertPopupVisible(self):
        """Check if the alert popup is visible."""
        try:
            self.driver.implicitly_wait(5)
            #alert_popup = self.driver.find_element(*self.alertPopup)
            alert_popup = self.driver.switch_to.alert
            alert_text = alert_popup.text
            print(f"Alert text: {alert_text}")
            #assert alert_popup.is_displayed(), "Alert popup should be visible"
            alert_popup.accept()  # Accept the alert
            print("Alert popup accepted successfully.")
        except Exception as e:
            print(f"Error: {e} - Alert popup is not visible or failed to accept - Test Case Failed")
            pytest.fail("Alert popup is not visible or failed to accept - Test case failed")

    def useName(self, username):
        """Enter the username in the login form."""
        try:
            self.driver.implicitly_wait(5)
            username_field = self.driver.find_element(*self.usernameField)
            username_field.send_keys(username)
        except Exception as e:
            print(f"Error: {e} - Username entry failed - Test Case Failed")
            pytest.fail("Username entry failed - Test case failed")

    def password(self, password):
        """Enter the password in the login form."""
        try:
            self.driver.implicitly_wait(5)
            password_field = self.driver.find_element(*self.passwordField)
            password_field.send_keys(password)
        except Exception as e:
            print(f"Error: {e} - Password entry failed - Test Case Failed")
            pytest.fail("Password entry failed - Test case failed")

    def loginButtonClick(self):
        """Click the login button."""
        try:
            self.driver.implicitly_wait(5)
            login_button = self.driver.find_element(*self.loginButton)
            login_button.click()
        except Exception as e:
            print(f"Error: {e} - Login button click failed - Test Case Failed")
            pytest.fail("Login button click failed - Test case failed")

    def passwordToggleClick(self):
        """Click the password toggle button."""
        try:
            self.driver.implicitly_wait(5)
            password_toggle = self.driver.find_element(*self.passwordToggle)
            password_toggle.click()
        except Exception as e:
            print(f"Error: {e} - Password toggle click failed - Test Case Failed")
            pytest.fail("Password toggle click failed - Test case failed")

    def rememberMeClick(self):
        """Click the remember me checkbox."""
        try:
            self.driver.implicitly_wait(5)
            remember_me = self.driver.find_element(*self.rememberMe)
            remember_me.click()
        except Exception as e:
            print(f"Error: {e} - Remember me click failed - Test Case Failed")
            pytest.fail("Remember me click failed - Test case failed")

    def errorInlineValidUserName(self):
        try:
            self.driver.implicitly_wait(5)
            error_message = self.driver.find_element(*self.usernameError)
            assert error_message.is_displayed(), "Username error message should be visible"
        except Exception as e:
            print(f"Error: {e} - Username error message is not visible - Test Case Failed")
            pytest.fail("Username error message is not visible - Test case failed")

    def errorInlineValidPassword(self):
        try:
            self.driver.implicitly_wait(5)
            error_message = self.driver.find_element(*self.passwordError)
            assert error_message.is_displayed(), "Password error message should be visible"
        except Exception as e:
            print(f"Error: {e} - Password error message is not visible - Test Case Failed")
            pytest.fail("Password error message is not visible - Test case failed")

    def langDropdownClick(self):
        """Click the language dropdown."""
        try:
            self.driver.implicitly_wait(5)
            lang_dropdown = self.driver.find_element(*self.langDropdown)
            lang_dropdown.click()
        except Exception as e:
            print(f"Error: {e} - Language dropdown click failed - Test Case Failed")
            pytest.fail("Language dropdown click failed - Test case failed")

    def langArabicClick(self):
        """Click the Arabic language option."""
        try:
            self.driver.implicitly_wait(5)
            lang_arabic = self.driver.find_element(*self.langArabic)
            lang_arabic.click()
        except Exception as e:
            print(f"Error: {e} - Arabic language click failed - Test Case Failed")
            pytest.fail("Arabic language click failed - Test case failed")







