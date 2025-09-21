import time

from selenium.webdriver.common.by import By
import pytest

class MyCompany:
    companyDetailsCard = (By.XPATH, "//div[@class='over-view-card-outline flex flex-column border-round-xl cursor-pointer']")

    companyNameTxt = (By.XPATH, "(//a[@data-test-id='w'])[23]")
    departmentCountTxt = (By.XPATH, "(//a[@data-test-id='w'])[25]")
    designationCountTxt = (By.XPATH, "(//a[@data-test-id='w'])[26]")
    locationCountTxt = (By.XPATH, "(//a[@data-test-id='w'])[27]")
    emailIDTxt = (By.XPATH, "(//a[@data-test-id='w'])[29]")
    phoneNumberTxt = (By.XPATH, "(//a[@data-test-id='w'])[31]")
    countryTxt = (By.XPATH, "(//a[@data-test-id='w'])[33]")


    departmentBtn = (By.XPATH, "(//button[@data-pc-name='button'])[2]")
    designationBtn = (By.XPATH, "(//button[@data-pc-name='button'])[3]")
    locationBtn = (By.XPATH, "(//button[@data-pc-name='button'])[4]")
    companyCalendar = (By.XPATH, "(//button[@data-pc-name='button'])[5]")
    locationCalendar = (By.XPATH, "(//button[@data-pc-name='button'])[6]")


    def __init__(self, driver):
        self.driver = driver

#-----------------------------------------------------------------------------------------
    def companyDetailsCardVisible(self):
        """Check if the company details card is visible."""
        try:
            self.driver.implicitly_wait(5)
            card = self.driver.find_element(*self.companyDetailsCard)
            assert card.is_displayed(), "Company details card should be visible"
        except Exception as e:
            print(f"Error: {e} - Company details card is not visible - Test Case Failed")
            pytest.fail("Company details card is not visible - Test case failed")

    def getCompanyName(self):
        """Get the company name text."""
        try:
            self.driver.implicitly_wait(5)
            company_name = self.driver.find_element(*self.companyNameTxt).text
            print(company_name)
            return company_name
        except Exception as e:
            print(f"Error: {e} - Failed to get company name - Test Case Failed")
            pytest.fail("Failed to get company name - Test case failed")
            return None

    def getDepartmentCount(self):
        """Get the department count text."""
        try:
            self.driver.implicitly_wait(5)
            department_count = self.driver.find_element(*self.departmentCountTxt).text
            print(department_count)
            return department_count
        except Exception as e:
            print(f"Error: {e} - Failed to get department count - Test Case Failed")
            pytest.fail("Failed to get department count - Test case failed")
            return None

    def getDesignationCount(self):
        """Get the designation count text."""
        try:
            self.driver.implicitly_wait(5)
            designation_count = self.driver.find_element(*self.designationCountTxt).text
            print(designation_count)
            return designation_count
        except Exception as e:
            print(f"Error: {e} - Failed to get designation count - Test Case Failed")
            pytest.fail("Failed to get designation count - Test case failed")
            return None

    def getLocationCount(self):
        """Get the location count text."""
        try:
            self.driver.implicitly_wait(5)
            location_count = self.driver.find_element(*self.locationCountTxt).text
            print(location_count)
            return location_count
        except Exception as e:
            print(f"Error: {e} - Failed to get location count - Test Case Failed")
            pytest.fail("Failed to get location count - Test case failed")
            return None

    def departmentBtnClick(self):
        """Click the department button."""
        try:
            self.driver.implicitly_wait(5)
            department_button = self.driver.find_element(*self.departmentBtn)
            department_button.click()
        except Exception as e:
            print(f"Error: {e} - Department button click failed - Test Case Failed")
            pytest.fail("Department button click failed - Test case failed")

    def designationBtnClick(self):
        """Click the designation button."""
        try:
            time.sleep(2)
            designationBtn = self.driver.find_element(*self.designationBtn)
            designationBtn.click()
        except Exception as e:
            print(f"Error: {e} - Designation button click failed - Test Case Failed")
            pytest.fail("Designation button click failed - Test case failed")

    def locationBtnClick(self):
        """Click the location button."""
        try:
            self.driver.implicitly_wait(5)
            location_button = self.driver.find_element(*self.locationBtn)
            location_button.click()
        except Exception as e:
            print(f"Error: {e} - Location button click failed - Test Case Failed")
            pytest.fail("Location button click failed - Test case failed")