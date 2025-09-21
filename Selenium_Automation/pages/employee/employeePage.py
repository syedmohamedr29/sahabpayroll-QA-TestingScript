from selenium.webdriver.common.by import By
import pytest

class employeePage():

    noDataEmpAddButton = (By.XPATH, "(//button[@data-pc-name='button'])[2]")
    empAddButton = (By.XPATH, "(//button[@data-pc-name='button'])[3]")
    searchPlaceholder = (By.XPATH, "(//input[@placeholder='Search'])[1]")

    row = (By.XPATH, "(//tr[@class='ng-star-inserted'])[1]")

    nameFilter = (By.XPATH, "(//th[@aria-sort='none'])[1]")
    nameFileterAsc = (By.XPATH, "//th[@aria-sort='ascending']")
    nameFilterDesc = (By.XPATH, "//th[@aria-sort='descending']")

    employeeCodeFilter = (By.XPATH, "(//th[@aria-sort='none'])[2]")
    employeeCodeFilterAsc = (By.XPATH, "//th[@aria-sort='ascending']")
    employeeCodeFilterDesc = (By.XPATH, "//th[@aria-sort='descending']")

    joiningDateFilter = (By.XPATH, "(//th[@aria-sort='none'])[3]")
    joiningDateFilterAsc = (By.XPATH, "//th[@aria-sort='ascending']")
    joiningDateFilterDesc = (By.XPATH, "//th[@aria-sort='descending']")


    """Employee Form"""

    employeeCode = (By.XPATH, "(//input[@placeholder='Enter'])[1]")
    employeeFirstNameEn = (By.XPATH, "(//input[@placeholder='First Name'])[1]")
    employeeLastNameEn = (By.XPATH, "(//input[@placeholder='Last Name'])[1]")
    employeeFamilyNameEn = (By.XPATH, "(//input[@placeholder='Family Name'])[1]")
    employeeFirstNameAr = (By.XPATH, "(//input[@placeholder='First Name'])[2]")
    employeeLastNameAr = (By.XPATH, "(//input[@placeholder='Last Name'])[2]")
    employeeFamilyNameAr = (By.XPATH, "(//input[@placeholder='Family Name'])[2]")

    genderDropdown = (By.XPATH, "(//div[@aria-label='dropdown trigger'])[2]")
    maleOption = (By.XPATH, "//span[text()='Male']")
    femaleOption = (By.XPATH, "//span[text()='Female']")

    martialStatusDropdown = (By.XPATH, "(//div[@aria-label='dropdown trigger'])[3]")
    singleOption = (By.XPATH, "//span[text()='Single']")
    marriedOption = (By.XPATH, "//span[text()='Married']")
    divorcedOption = (By.XPATH, "//span[text()='Divorced']")
    widowedOption = (By.XPATH, "//span[text()='Widowed']")

    identificationNumber = (By.XPATH, "(//input[@data-test-id='nInput'])[8]")
    pEmailId =  (By.XPATH, "(//input[@data-test-id='nInput'])[9]")
    phoneNumber = (By.XPATH, "(//input[@data-test-id='nInput'])[10]")

    dobCalender = (By.XPATH, "(//p-calendar)[1]//input")

    nationalityDropdown = (By.XPATH, "(//div[@aria-label='dropdown trigger'])[4]")
    search = (By.XPATH, "//input[@role='searchbox']")
    select = (By.XPATH, "//li[@role='option']")

    dojCalender = (By.XPATH, "(//p-calendar)[2]//input")


    locationDropdown = (By.XPATH, "(//div[@aria-label='dropdown trigger'])[5]")
    location = (By.XPATH, "//li[@role='option']")


    departmentDropdown = (By.XPATH, "(//div[@aria-label='dropdown trigger'])[6]")
    department = (By.XPATH, "//li[@role='option']")

    designationDropdown = (By.XPATH, "(//div[@aria-label='dropdown trigger'])[7]")
    designation = (By.XPATH, "//li[@role='option']")

    hrPartenerDropdown
    reportingManagerDropdown
    reportingManager
    reportmanagerChecklist
    addButton = (By.XPATH, "(//button[@data-pc-name='button'])[3]")
    cancelButton = (By.XPATH, "(//button[@data-pc-name='button'])[4]")
    backButton = (By.XPATH, "(//button[@data-pc-name='button'])[2]")





    def __init__(self, driver):
        self.driver = driver


    def clickEmpAddButton(self):
        try:
            if self.driver.find_elements(*self.noDataEmpAddButton).is_displayed():
                self.driver.find_element(*self.noDataEmpAddButton).click()
            else:
                self.driver.find_element(*self.empAddButton).is_displayed()
                self.driver.find_element(*self.empAddButton).click()
        except Exception as e:
            pytest.fail(f"Failed to click employee add button: {e}")

