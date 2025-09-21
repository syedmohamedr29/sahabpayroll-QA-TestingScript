from selenium.webdriver.common.by import By
import pytest
import time

class department:
    backBtn = (By.XPATH, "//p-button[@data-test-id='_WithIcon']")
    noDataAddBtn = (By.XPATH, "(//button[@data-pc-name='button'])[3]")
    departmentAddBtn = (By.XPATH, "(//button[@data-pc-name='button'])[4]")
    SearchPlaceholder = (By.XPATH, "//input[@placeholder='Search']")

    # Form
    enName = (By.XPATH, "(//input[@data-test-id='nInput'])[1]")
    arName = (By.XPATH, "(//input[@data-test-id='nInput'])[2]")
    descriptionEn = (By.XPATH, "(//input[@data-test-id='nInput'])[3]")
    descriptionAr = (By.XPATH, "(//input[@data-test-id='nInput'])[4]")
    shortCode = (By.XPATH, "(//input[@data-test-id='nInput'])[5]")
    mailAlias = (By.XPATH, "(//input[@data-test-id='nInput'])[6]")

    xIcon = (By.XPATH, "(//button[@data-pc-name='button'])[5]")
    cancelBtn = (By.XPATH, "(//button[@data-pc-name='button'])[6]")
    addBtn = (By.XPATH, "(//button[@data-pc-name='button'])[7]")
    deleteIcon = (By.XPATH, "(//i[@data-test-id='svg-icon'])[19]")
    editIcon = (By.XPATH, "(//i[@data-test-id='svg-icon'])[20]")
    saveChangesBtn = (By.XPATH, "(//button[@data-pc-name='button'])[7]")

    row1St = (By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    deleteBtn = (By.XPATH, "(//button[@data-pc-name='button'])[6]")
    deleteCancelBtn = (By.XPATH, "(//button[@data-pc-name='button'])[5]")

    toasterMessageAdd = (By.XPATH, "")
    toasterMessageDelete = (By.XPATH, "")
    toasterMessageEdit = (By.XPATH, "")

    noDataFound = (By.XPATH, "(//a[@data-test-id='w'])[28]")

    errorMessageDepartmentName = (By.XPATH,"(//small[@data-test-id='nErrorMsg'])[1]")
    errorMessageShortCode = (By.XPATH,"(//small[@data-test-id='nErrorMsg'])[2]")

    errorMessageDuplicateName =\
        (By.XPATH, "//div[contains(@class, 'p-toast-message-content')]//a[contains(text(), 'There is already a company department with the same name')]")

    errorMessageDuplicateShortCode =\
        (By.XPATH, "//div[contains(@class, 'p-toast-message-content')]//a[contains(text(), 'Department ShortCode already exists')]")

    def __init__(self, driver):
        self.driver = driver

#----------------------------------------------------------------------------------

    def clickBackBtn(self):
        try:
            self.driver.find_element(*self.backBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click back button: {e}")

    def clickDepartmentAddBtn(self):
        try:
            if self.driver.find_element(*self.noDataAddBtn).is_displayed():
                self.driver.find_element(*self.noDataAddBtn).click()
            else:
                self.driver.find_element(*self.departmentAddBtn).is_displayed()
                self.driver.find_element(*self.departmentAddBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click department add button: {e}")


    def enterSearchPlaceholder(self, search_departmentName):
        """Enter text in the search placeholder."""
        try:
            search_field = self.driver.find_element(*self.SearchPlaceholder)
            search_field.clear()
            search_field.send_keys(search_departmentName)
        except Exception as e:
            pytest.fail(f"Failed to enter text in search placeholder: {e}")

    # Form Methods

    def enterEnName(self, en_name):
        """Enter English name in the form."""
        try:
            en_name_field = self.driver.find_element(*self.enName)
            en_name_field.clear()
            en_name_field.send_keys(en_name)
        except Exception as e:
            pytest.fail(f"Failed to enter English name: {e}")

    def enterArName(self, ar_name):
        """Enter Arabic name in the form."""
        try:
            ar_name_field = self.driver.find_element(*self.arName)
            ar_name_field.clear()
            ar_name_field.send_keys(ar_name)
        except Exception as e:
            pytest.fail(f"Failed to enter Arabic name: {e}")

    def enterDescriptionEn(self, description_en):
        """Enter English description in the form."""
        try:
            description_en_field = self.driver.find_element(*self.descriptionEn)
            description_en_field.clear()
            description_en_field.send_keys(description_en)
        except Exception as e:
            pytest.fail(f"Failed to enter English description: {e}")

    def enterDescriptionAr(self, description_ar):
        """Enter Arabic description in the form."""
        try:
            description_ar_field = self.driver.find_element(*self.descriptionAr)
            description_ar_field.clear()
            description_ar_field.send_keys(description_ar)
        except Exception as e:
            pytest.fail(f"Failed to enter Arabic description: {e}")

    def enterShortCode(self, short_code):
        """Enter short code in the form."""
        try:
            short_code_field = self.driver.find_element(*self.shortCode)
            short_code_field.clear()
            short_code_field.send_keys(short_code)
        except Exception as e:
            pytest.fail(f"Failed to enter short code: {e}")

    def enterMailAlias(self, mail_alias):
        """Enter mail alias in the form."""
        try:
            mail_alias_field = self.driver.find_element(*self.mailAlias)
            mail_alias_field.clear()
            mail_alias_field.send_keys(mail_alias)
        except Exception as e:
            pytest.fail(f"Failed to enter mail alias: {e}")

    def clickXIcon(self):
        """Click the X icon to close the form."""
        try:
            self.driver.find_element(*self.xIcon).click()
        except Exception as e:
            pytest.fail(f"Failed to click X icon: {e}")

    def clickCancelBtn(self):
        """Click the cancel button to discard changes."""
        try:
            self.driver.find_element(*self.cancelBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click cancel button: {e}")

    def clickAddBtn(self):
        """Click the add button to save changes."""
        try:
            self.driver.find_element(*self.addBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click add button: {e}")

    def clickDeleteIcon(self):
        """Click the delete icon for the first row."""
        try:
            self.driver.find_element(*self.deleteIcon).click()
        except Exception as e:
            pytest.fail(f"Failed to click delete icon: {e}")

    def clickEditIcon(self):
        try:
            self.driver.find_element(*self.editIcon).click()
        except Exception as e:
            pytest.fail(f"Failed to click edit icon: {e}")

    def clickSaveChangesBtn(self):
        """Click the save changes button."""
        try:
            self.driver.find_element(*self.saveChangesBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click save changes button: {e}")

    def clickDeleteBtn(self):
        """Click the delete button in the confirmation dialog."""
        try:
            self.driver.find_element(*self.deleteBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click delete button: {e}")

    def clickDeleteCancelBtn(self):
        """Click the cancel button in the delete confirmation dialog."""
        try:
            self.driver.find_element(*self.deleteCancelBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click delete cancel button: {e}")

    def getRow1st(self):
        """Get the first row element."""
        try:
            self.driver.implicitly_wait(10)  # Wait for elements to load
            row1St = self.driver.find_element(*self.row1St)
            print(row1St)
            return row1St
        except Exception as e:
            print(f"Failed to get the first row element: {e}")
            pytest.fail(f"Failed to get the first row element: {e}")
            return None

    def getToasterMessageAdd(self):
        """Get the toaster message after adding a designation."""
        try:
            toaster_message = self.driver.find_element(*self.toasterMessageAdd).text
            assert toaster_message.is_displayed(), "Toaster message is not displayed"
            print(toaster_message)
            return toaster_message
        except Exception as e:
            print(f"Error: {e} - Failed to get toaster message after add - Test Case Failed")
            pytest.fail(f"Failed to get toaster message after add: {e}")
            return None

    def getToasterMessageDelete(self):
        """Get the toaster message after deleting a designation."""
        try:
            toaster_message = self.driver.find_element(*self.toasterMessageDelete).text
            assert toaster_message.is_displayed(), "Toaster message is not displayed"
            print(toaster_message)
            return toaster_message
        except Exception as e:
            print(f"Error: {e} - Failed to get toaster message after delete - Test Case Failed")
            pytest.fail(f"Failed to get toaster message after delete: {e}")
            return None

    def getToasterMessageEdit(self):
        """Get the toaster message after editing a designation."""
        try:
            toaster_message = self.driver.find_element(*self.toasterMessageEdit).text
            assert toaster_message.is_displayed(), "Toaster message is not displayed"
            print(toaster_message)
            return toaster_message
        except Exception as e:
            print(f"Error: {e} - Failed to get toaster message after edit - Test Case Failed")
            pytest.fail(f"Failed to get toaster message after edit: {e}")
            return None

    def getNoDataFound(self):
        """Get the 'No Data Found' message."""
        try:
            no_data_message = self.driver.find_element(*self.noDataFound).text
            assert no_data_message.is_displayed(), "No Data Found message is not displayed"
            print(no_data_message)
            return no_data_message
        except Exception as e:
            print(f"Error: {e} - Failed to get 'No Data Found' message - Test Case Failed")
            pytest.fail(f"Failed to get 'No Data Found' message: {e}")
            return None

    def inlineValidationEmployeeName(self):
        try:
            time.sleep(2)
            element = self.driver.find_element(*self.errorMessageDepartmentName)
            assert element.is_displayed(), "Inline message is not displayed"
            inlineName = element.text
            print(inlineName)
            return inlineName
        except Exception as e:
            print(f"Error: {e} - Failed to get inline validation for employee name - Test Case Failed")
            pytest.fail(f"Failed to get inline validation for employee name: {e}")
            return None

    def inlineValidationShortCode(self):
        try:
            time.sleep(2)
            element = self.driver.find_element(*self.errorMessageShortCode)
            assert element.is_displayed(), "In Line message is displayed"
            inlineName = element.text
            print(inlineName)
            return inlineName
        except Exception as e:
            print(f"Error: {e} - Failed to get inline validation for short code - Test Case Failed")
            pytest.fail(f"Failed to get inline validation for short code: {e}")
            return None

    def duplicateName(self):
        """Check if the department name is already in use."""
        try:
            time.sleep(2)
            element = self.driver.find_element(*self.errorMessageDuplicateName)
            assert element.is_displayed(), "Error message for same name is  displayed"
            errorMessage = element.text
            print(errorMessage)
            return errorMessage
        except Exception as e:
            print(f"Error: {e} - Failed to check for same name - Test Case Failed")
            pytest.fail(f"Failed to check for same name: {e}")
            return None

    def duplicateShortCode(self):
        """Check if the department name is already in use."""
        try:
            time.sleep(2)
            element = self.driver.find_element(*self.errorMessageDuplicateShortCode)
            assert element.is_displayed(), "Error message for same name is  displayed"
            errorMessage = element.text
            print(errorMessage)
            return errorMessage
        except Exception as e:
            print(f"Error: {e} - Failed to check for same name - Test Case Failed")
            pytest.fail(f"Failed to check for same name: {e}")
            return None


