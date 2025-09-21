from selenium.webdriver.common.by import By
import pytest

class Location:

    backBtn = (By.XPATH, "//p-button[@data-test-id='_WithIcon']")
    noDataAddBtn = (By.XPATH, "(//button[@data-pc-name='button'])[3]")
    locationAddBtn = (By.XPATH, "(//button[@data-pc-name='button'])[4]")
    SearchPlaceholder = (By.XPATH, "//input[@placeholder='Search']")

    #Form
    enName = (By.XPATH,"(//input[@data-test-id='nInput'])[1]")
    arName = (By.XPATH,"(//input[@data-test-id='nInput'])[2]")
    shortCode = (By.XPATH,"(//input[@data-test-id='nInput'])[3]")
    addressLine1 = (By.XPATH,"(//input[@data-test-id='nInput'])[4]")
    addressLine2 = (By.XPATH,"(//input[@data-test-id='nInput'])[5]")
    countryDropdown = (By.XPATH,"(//div[@aria-haspopup='listbox'])[2]")
    selectValue = (By.XPATH,"//li[@aria-label='Saudi Arabia']")
    state = (By.XPATH,"(//input[@data-test-id='nInput'])[6]")
    city = (By.XPATH,"(//input[@data-test-id='nInput'])[7]")
    pincode = (By.XPATH,"(//input[@data-test-id='nInput'])[8]")
    saveChangesBtn = (By.XPATH, "(//button[@data-pc-name='button'])[7]")


    xIcon = (By.XPATH,"(//button[@data-pc-name='button'])[5]")
    cancelBtn = (By.XPATH,"(//button[@data-pc-name='button'])[6]")
    addBtn = (By.XPATH,"(//button[@data-pc-name='button'])[7]")
    deleteIcon = (By.XPATH,"(//i[@data-test-id='svg-icon'])[19]")
    editIcon = (By.XPATH,"(//i[@data-test-id='svg-icon'])[20]")

    row1St = (By.XPATH,"(//tr[@class='ng-star-inserted'])[1])")

    deleteBtn = (By.XPATH, "(//button[@data-pc-name='button'])[6]")
    deleteCancelBtn = (By.XPATH, "(//button[@data-pc-name='button'])[5]")

    toasterMessageAdd = (By.XPATH, "")
    toasterMessageDelete = (By.XPATH, "")
    toasterMessageEdit = (By.XPATH, "")

    noDataFound = (By.XPATH, "(//a[@data-test-id='w'])[28]")

    errorMessageLocationName = (By.XPATH, "(//small[@data-test-id='nErrorMsg'])[1]")
    errorMessageShortCode = (By.XPATH, "(//small[@data-test-id='nErrorMsg'])[2]")

    errorMessageDuplicateName = \
        (By.XPATH,
         "//div[contains(@class, 'p-toast-message-content')]//a[contains(text(), 'There is already a company location with the same name')]")

    errorMessageDuplicateShortCode = \
        (By.XPATH,
         "//div[contains(@class, 'p-toast-message-content')]//a[contains(text(), 'Location ShortCode already exists')]")



    def __init__(self, driver):
        self.driver = driver

#----------------------------------------------------------------------------------


    def clickLocationAddBtn(self):
        try:
            if self.driver.find_element(*self.noDataAddBtn).is_displayed():
                self.driver.find_element(*self.noDataAddBtn).click()
            else:
                self.driver.find_element(*self.locationAddBtn).is_displayed()
                self.driver.find_element(*self.locationAddBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click location add button: {e}")


    def clickBackBtn(self):
        try:
            self.driver.find_element(*self.backBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click back button: {e}")

    def enterSearchPlaceholder(self, search_locationName):
        """Enter text in the search placeholder."""
        try:
            search_field = self.driver.find_element(*self.SearchPlaceholder)
            search_field.clear()
            search_field.send_keys(search_locationName)
        except Exception as e:
            pytest.fail(f"Failed to enter text in search placeholder: {e}")

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

    def enterShortCode(self, short_code):
        """Enter short code in the form."""
        try:
            short_code_field = self.driver.find_element(*self.shortCode)
            short_code_field.clear()
            short_code_field.send_keys(short_code)
        except Exception as e:
            pytest.fail(f"Failed to enter short code: {e}")

    def enterAddressLine1(self, address_line1):
        """Enter address line 1 in the form."""
        try:
            address_line1_field = self.driver.find_element(*self.addressLine1)
            address_line1_field.clear()
            address_line1_field.send_keys(address_line1)
        except Exception as e:
            pytest.fail(f"Failed to enter address line 1: {e}")

    def enterAddressLine2(self, address_line2):
        """Enter address line 2 in the form."""
        try:
            address_line2_field = self.driver.find_element(*self.addressLine2)
            address_line2_field.clear()
            address_line2_field.send_keys(address_line2)
        except Exception as e:
            pytest.fail(f"Failed to enter address line 2: {e}")

    def selectCountry(self):
        """Select country from the dropdown."""
        try:
            self.driver.find_element(*self.countryDropdown).click()
            self.driver.find_element(*self.selectValue).click()
        except Exception as e:
            pytest.fail(f"Failed to select country: {e}")

    def enterState(self, state):
        """Enter state in the form."""
        try:
            state_field = self.driver.find_element(*self.state)
            state_field.clear()
            state_field.send_keys(state)
        except Exception as e:
            pytest.fail(f"Failed to enter state: {e}")

    def enterCity(self, city):
        """Enter city in the form."""
        try:
            city_field = self.driver.find_element(*self.city)
            city_field.clear()
            city_field.send_keys(city)
        except Exception as e:
            pytest.fail(f"Failed to enter city: {e}")

    def enterPincode(self, pincode):
        """Enter pincode in the form."""
        try:
            pincode_field = self.driver.find_element(*self.pincode)
            pincode_field.clear()
            pincode_field.send_keys(pincode)
        except Exception as e:
            pytest.fail(f"Failed to enter pincode: {e}")

    def clickSaveChangesBtn(self):
        """Click the save changes button."""
        try:
            self.driver.find_element(*self.saveChangesBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click save changes button: {e}")

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
        """Click the edit icon for the first row."""
        try:
            self.driver.find_element(*self.editIcon).click()
        except Exception as e:
            pytest.fail(f"Failed to click edit icon: {e}")

    def SaveChangesBtn(self):
        """Click the save changes button."""
        try:
            self.driver.find_element(*self.saveChangesBtn).click()
        except Exception as e:
            pytest.fail(f"Failed to click save changes button: {e}")

    def  clickDeleteBtn(self):
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

    def errorNamePopup(self):
        """Get the error message for department name."""
        try:
            error_message = self.driver.find_element(*self.errorMessageLocationName).text
            assert error_message.is_displayed(), "Error message for department name is not displayed"
            print(error_message)
            return error_message
        except Exception as e:
            print(f"Error: {e} - Failed to get error message for department name - Test Case Failed")
            pytest.fail(f"Failed to get error message for department name: {e}")
            return None

    def errorShortCodePopup(self):
        try:
            error_message = self.driver.find_element(*self.errorMessageShortCode).text
            assert error_message.is_displayed(), "Error message for department name is not displayed"
            print(error_message)
            return error_message
        except Exception as e:
            print(f"Error: {e} - Failed to get error message for department name - Test Case Failed")
            pytest.fail(f"Failed to get error message for department name: {e}")
            return None



