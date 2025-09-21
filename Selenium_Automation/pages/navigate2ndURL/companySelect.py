import time

from selenium.webdriver.common.by import By
import pytest

class companySelect:

    companiesCard = (By.XPATH, "//*[@class='p-element card']")
    nameElement = (By.XPATH, ".//h4[@class='heading noMargin']")
    continueButton = (By.XPATH, "// *[ @ id = 'companySelectionButtonId']")

    def __init__(self, driver):
        self.driver = driver

    def selectLastCompany(self):
        try:
            time.sleep(5)
            companies = self.driver.find_elements(*self.companiesCard)
            continueButton = self.driver.find_element(*self.continueButton)
            if not companies:
                print("No companies found!")
                return
            last_company = companies[-2]
            print("Selecting the last company...")
            last_company.click()
            print("Navigate to the next page")

        except Exception as e:
            print(f"Error: {e} - Failed to select the last company")
            pytest.fail("Failed to select the last company - Test case failed")

    def selectCompanyName(self):
        try:
            companies = self.driver.find_elements(*self.companiesCard)  # Changed to find_elements
            element = self.driver.find_element(*self.nameElement)

            if not companies:
                print("No companies found!")
                return

            for company in companies:
                if element.text.strip() == "Design":
                    print("Selecting company: Design")
                    company.click()
                    print("Navigate to the next page")
                    return

        except Exception as e:
            print(f"Error: {e} - Failed to select the company")
            pytest.fail("Failed to select the company - Test case failed")

    def continueBtn(self):
        try:
            time.sleep(5)
            continueButton = self.driver.find_element(*self.continueButton)
            continueButton.click()
            print("Continue button clicked")
        except Exception as e:
            print(f"Error: {e} - Failed to click the continue button")
            pytest.fail("Failed to click the continue button - Test case failed")




