import time

import pytest
from utils.basPage import basePage
from pages.navigate2ndURL.companySelect import companySelect
from pages.navigate2ndURL.navBar import navigate
from pages.login.loginPage import loginPage
from pages.myCompanyPage.company.myCompany import MyCompany
from pages.myCompanyPage.department.departmantPage import department


class TestCasesDepartment:
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

        self.login_page = loginPage(self.driver) # ← pass the driver
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
        """ Navigate to the Department page """
        self.selectBtn = MyCompany(self.driver)  # ← pass the driver
        self.selectBtn.departmentBtnClick()
        time.sleep(3)
        self.department_page = department(self.driver)  # ← pass the driver



    def test_TC001_validateInLineMessage(self):
        """ Test case to validate inline message on the Department page """
        try:
            time.sleep(3)
            self.department_page.clickDepartmentAddBtn()
            time.sleep(2)
            self.department_page.clickAddBtn()
            self.department_page.inlineValidationEmployeeName()
            self.department_page.inlineValidationShortCode()
            time.sleep(5)
        except Exception as e:
            print("Failed to validate inline message:", e)
            pytest.fail(f"Failed to validate inline message: {e}")
        finally:
            self.base_page.closeDriver()

    def test_TC_002_errorDuplicateDepartmentName(self):
        """ Test case to add a department """
        departmentNameEn = "Test Department"
        departmentNameAR = "قسم الاختبار"
        departmentShortCode = "TSS"
        departmentDescriptionEn = "This is a test department."
        departmentDescriptionAR = "هذا قسم اختبار."
        mailAlias = "td@gmail.com"

        try:
            self.department_page.clickDepartmentAddBtn()
            time.sleep(3)
            self.department_page.enterEnName(departmentNameEn)
            self.department_page.enterArName(departmentNameAR)
            self.department_page.enterDescriptionEn(departmentDescriptionEn)
            self.department_page.enterDescriptionAr(departmentDescriptionAR)
            self.department_page.enterShortCode(departmentShortCode)
            self.department_page.enterMailAlias(mailAlias)
            time.sleep(2)
            self.department_page.clickAddBtn()
            # Attempt to add the same department again to trigger the error
            time.sleep(2)
            self.department_page.duplicateName(), "Department name already exists.", "Pop-up should be displayed for same department name"
            print("Error message for same department name validated successfully.")
            time.sleep(3)
        except Exception as e:
            print("Failed to validate error message for same department name:", e)
            pytest.fail("Failed to validate error message for same department name: {e}")

        finally:
            self.base_page.closeDriver()

    def test_TC_002_errorDuplicateShortCodeName(self):
        """ Test case to add a department """
        departmentNameEn = "Test Department 2"
        departmentNameAR = "قسم الاختبار 2"
        departmentShortCode = "TDS"
        departmentDescriptionEn = "This is a test department."
        departmentDescriptionAR = "هذا قسم اختبار."
        mailAlias = "td@gmail.com"

        try:
            self.department_page.clickDepartmentAddBtn()
            time.sleep(3)
            self.department_page.enterEnName(departmentNameEn)
            self.department_page.enterArName(departmentNameAR)
            self.department_page.enterDescriptionEn(departmentDescriptionEn)
            self.department_page.enterDescriptionAr(departmentDescriptionAR)
            self.department_page.enterShortCode(departmentShortCode)
            self.department_page.enterMailAlias(mailAlias)
            time.sleep(2)
            self.department_page.clickAddBtn()
            # Attempt to add the same department again to trigger the error
            time.sleep(2)
            self.department_page.duplicateShortCode(), "Department Short Code already exists.", "Pop-up should be displayed for same department Short Code"
            print("Error message for same department Short Code validated successfully.")
            time.sleep(3)
        except Exception as e:
            print("Failed to validate error message for same department Short code:", e)
            pytest.fail("Failed to validate error message for same department Short code: {e}")

        finally:
            self.base_page.closeDriver()



    def test_add_department(self):
        """ Test case to add a department """
        departmentNameEn = "Test Department"
        departmentNameAR = "قسم الاختبار"
        departmentShortCode = "TDS"
        departmentDescriptionEn = "This is a test department."
        departmentDescriptionAR = "هذا قسم اختبار."
        mailAlias = "td@gmail.com"

        try:
            self.department_page.clickDepartmentAddBtn()
            time.sleep(3)
            self.department_page.enterEnName(departmentNameEn)
            self.department_page.enterArName(departmentNameAR)
            self.department_page.enterDescriptionEn(departmentDescriptionEn)
            self.department_page.enterDescriptionAr(departmentDescriptionAR)
            self.department_page.enterShortCode(departmentShortCode)
            self.department_page.enterMailAlias(mailAlias)
            self.department_page.clickAddBtn()
            time.sleep(2)
            print("Department added successfully.")
        except Exception as e:
            print("Failed to add department:", e)
            pytest.fail(f"Failed to add department: {e}")
        finally:
            self.base_page.closeDriver()







      #  self.department_page.addDepartment()
       # time.sleep(5)
        #assert self.department_page.is_department_added(), "Department was not added successfully"
