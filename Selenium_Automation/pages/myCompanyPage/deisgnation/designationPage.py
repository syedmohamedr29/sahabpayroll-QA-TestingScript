from selenium.webdriver.common.by import By
import pytest


class designation:

    backBtn = (By.XPATH, "//p-button[@data-test-id='_WithIcon']")
    noDataAddBtn = (By.XPATH, "(//button[@data-pc-name='button'])[3]")
    designationAddBtn = (By.XPATH, "(//button[@data-pc-name='button'])[4]")
    SearchPlaceholder = (By.XPATH, "//input[@placeholder='Search']")

    # Form
    enName = (By.XPATH, "(//input[@data-test-id='nInput'])[1]")
    arName = (By.XPATH, "(//input[@data-test-id='nInput'])[2]")
    shortCode = (By.XPATH, "(//input[@data-test-id='nInput'])[3]")
    mailAlias = (By.XPATH, "(//input[@data-test-id='nInput'])[4]")

    xIcon = (By.XPATH, "(//button[@data-pc-name='button'])[5]")
    cancelBtn = (By.XPATH, "(//button[@data-pc-name='button'])[6]")
    addBtn = (By.XPATH, "(//button[@data-pc-name='button'])[7]")
    deleteIcon = (By.XPATH, "(//i[@data-test-id='svg-icon'])[19]")
    editIcon = (By.XPATH, "(//i[@data-test-id='svg-icon'])[20]")
    saveChangesBtn = (By.XPATH, "(//button[@data-pc-name='button'])[7]")

    row1St = (By.XPATH,"(//tr[@class='ng-star-inserted'])[1]")

    deleteBtn = (By.XPATH, "(//button[@data-pc-name='button'])[6]")
    deleteCancelBtn = (By.XPATH, "(//button[@data-pc-name='button'])[5]")

    toasterMessageAdd = (By.XPATH, "")
    toasterMessageDelete = (By.XPATH, "")
    toasterMessageEdit = (By.XPATH, "")

    noDataFound = (By.XPATH, "(//a[@data-test-id='w'])[28]")

    def __init__(self, driver):
        self.driver = driver
#-----------------------------------------------------------------------------------------

    def clickDesignationAddBtn(self):
        """Click the add button to open the designation form."""
        try:
            if self.driver.find_element(*self.noDataAddBtn).is_displayed():
                self.driver.find_element(*self.noDataAddBtn).click()
            else:
                self.driver.find_element(*self.designationAddBtn).is_displayed()
                self.driver.find_element(*self.designationAddBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click add button: {e}")

    def clickBackBtn(self):
        try:
            self.driver.find_element(*self.backBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click back button: {e}")

    def enterSearchPlaceholder(self, search_designationName):
        """Enter text in the search placeholder."""
        try:
            search_input = self.driver.find_element(*self.SearchPlaceholder)
            search_input.clear()
            search_input.send_keys(search_designationName)
        except Exception as e:
            pytest.fail(f"Failed to enter search text: {e}")

    # Form Methods

    def enterEnName(self, enName):
        """Enter English name in the form."""
        try:
            en_name_input = self.driver.find_element(*self.enName)
            en_name_input.clear()
            en_name_input.send_keys(enName)
        except Exception as e:
            pytest.fail(f"Failed to enter English name: {e}")

    def enterArName(self, arName):
        """Enter Arabic name in the form."""
        try:
            ar_name_input = self.driver.find_element(*self.arName)
            ar_name_input.clear()
            ar_name_input.send_keys(arName)
        except Exception as e:
            pytest.fail(f"Failed to enter Arabic name: {e}")

    def enterShortCode(self, shortCode):

        """Enter short code in the form."""
        try:
            short_code_input = self.driver.find_element(*self.shortCode)
            short_code_input.clear()
            short_code_input.send_keys(shortCode)
        except Exception as e:
            pytest.fail(f"Failed to enter short code: {e}")

    def enterMailAlias(self, mailAlias):
        """Enter mail alias in the form."""
        try:
            mail_alias_input = self.driver.find_element(*self.mailAlias)
            mail_alias_input.clear()
            mail_alias_input.send_keys(mailAlias)
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
        """Click the add button to save the new designation."""
        try:
            self.driver.find_element(*self.addBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click add button: {e}")

    def clickDeleteIcon(self):
        """Click the delete icon to remove a designation."""
        try:
            self.driver.find_element(*self.deleteIcon).click()
        except Exception as e:
            pytest.fail(f"Failed to click delete icon: {e}")

    def clickEditIcon(self):
        """Click the edit icon to modify a designation."""
        try:
            self.driver.find_element(*self.editIcon).click()
        except Exception as e:
            pytest.fail(f"Failed to click edit icon: {e}")

    def clickSaveChangesBtn(self):
        """Click the save changes button to apply modifications."""
        try:
            self.driver.find_element(*self.saveChangesBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click save changes button: {e}")

    def clickDeleteBtn(self):
        """Click the delete button to confirm deletion."""
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

    def getRow1St(self):
        """Get the first row element."""
        try:
            self.driver.implicitly_wait(5)
            row1 = self.driver.find_element(*self.row1St).text
            print(row1)
            return row1
        except Exception as e:
            print(f"Error: {e} - Failed to get first row element - Test Case Failed")
            pytest.fail(f"Failed to get first row element: {e}")
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



