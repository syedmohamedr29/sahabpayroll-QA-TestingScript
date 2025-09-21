from selenium.webdriver.common.by import By
import time


class navigate:

    """V1 Nav Menus"""
    dashboardNavV1 = (By.XPATH, "(//button[@type='button'])[2]")
    employeeNavV1 = (By.XPATH, "(//button[@type='button'])[3]")
    leaveNavV1 = (By.XPATH, "(//button[@type='button'])[4]")
    organizationMenuV1 = (By.XPATH, "(//button[@type='button'])[5]")

    """V2 Nav menus"""
    v2Window = (By.XPATH, "(//button[@type='button'])[5]")
    homeNavV2= (By.XPATH, "(//a[@data-test-id='se_2_1'])")
    entitiesNavV2 = (By.XPATH, "(//a[@data-test-id='se_3_11'])")
    myCompanyNavV2 = (By.XPATH,"(//a[@data-test-id='se_3_2'])")
    employeeNavV2 = (By.XPATH, "(//a[@data-test-id='w'])")
    exitNavV2 = (By.XPATH, "(//a[@data-test-id='se_3_13'])")
    payrollAttendanceV2 = (By.XPATH, "(//a[@data-test-id='se_3_12'])")
    leaveEncashV2 = (By.XPATH, "(//a[@data-test-id='se_3_14'])")
    leaveResumptionV2 = (By.XPATH, "(//a[@data-test-id='se_3_15'])")
    leaveTypeV2 = (By.XPATH, "(//a[@data-test-id='se_3_5'])")
    leaveApplicationV2 = (By.XPATH, "(//a[@data-test-id='se_3_16'])")
    leaveBalanceV2 = (By.XPATH, "(//a[@data-test-id='se_3_19'])")



    """V1 Nav Functions"""
    def __init__(self, driver):
        self.driver = driver

    def dashboardNavv1(self):
        """Navigate to the dashboard."""
        dashboardNav = self.driver.find_element(*self.dashboardNavV1)
        dashboardNav.click()
        self.driver.implicitly_wait(5)

    def leaveNavv1(self):
        """Navigate to the leave section."""
        leaveNav = self.driver.find_element(*self.leaveNavV1)
        leaveNav.click()
        self.driver.implicitly_wait(5)

    def organisationNavv1(self):
        """Navigate to the organization section."""
        organizationMenu = self.driver.find_element(*self.organizationMenuV1)
        organizationMenu.click()
        self.driver.implicitly_wait(5)

    def employeeNavv1(self):
        """Navigate to the employee section."""
        employeeNav = self.driver.find_element(*self.employeeNavV1)
        employeeNav.click()
        self.driver.implicitly_wait(5)

    def switchV2(self):
        v2Window = self.driver.find_element(*self.v2Window)
        v2Window.click()
        time.sleep(2)

        originalWindow = self.driver.current_window_handle
        allWindows = self.driver.window_handles

        for window in allWindows:
            if window != originalWindow:
                self.driver.switch_to.window(window)
                time.sleep(5)
                break

        print("Now at:", self.driver.current_url)


    """V2 Nav Functions"""

    def homeNavv2(self):
        """Navigate to the home section."""
        homeNav = self.driver.find_element(*self.homeNavV2)
        homeNav.click()
        self.driver.implicitly_wait(5)

    def entitiesNavv2(self):
        """Navigate to the entities section."""
        entitiesNav = self.driver.find_element(*self.entitiesNavV2)
        entitiesNav.click()
        self.driver.implicitly_wait(5)

    def myCompanyNavv2(self):
        """Navigate to the company section."""
        myCompanyNav = self.driver.find_element(*self.myCompanyNavV2)
        myCompanyNav.click()
        self.driver.implicitly_wait(5)

    def employeeNavv2(self):
        """Navigate to the employee section."""
        employeeNav = self.driver.find_element(*self.employeeNavV2)
        employeeNav.click()
        self.driver.implicitly_wait(5)

    def exitNavv2(self):
        """Navigate to the exit section."""
        exitNav = self.driver.find_element(*self.exitNavV2)
        exitNav.click()
        self.driver.implicitly_wait(5)

    def payrollAttendanceNavv2(self):
        """Navigate to the payroll attendance section."""
        payrollAttendanceNav = self.driver.find_element(*self.payrollAttendanceV2)
        payrollAttendanceNav.click()
        self.driver.implicitly_wait(5)

    def leaveEncashNavv2(self):
        """Navigate to the leave encashment section."""
        leaveEncashNav = self.driver.find_element(*self.leaveEncashV2)
        leaveEncashNav.click()
        self.driver.implicitly_wait(5)

    def leaveResumptionNavv2(self):
        """Navigate to the leave resumption section."""
        leaveResumptionNav = self.driver.find_element(*self.leaveResumptionV2)
        leaveResumptionNav.click()
        self.driver.implicitly_wait(5)

    def leaveTypeNavv2(self):
        """Navigate to the leave type section."""
        leaveTypeNav = self.driver.find_element(*self.leaveTypeV2)
        leaveTypeNav.click()
        self.driver.implicitly_wait(5)

    def leaveApplicationNavv2(self):
        """Navigate to the leave application section."""
        leaveApplicationNav = self.driver.find_element(*self.leaveApplicationV2)
        leaveApplicationNav.click()
        self.driver.implicitly_wait(5)

    def leaveBalanceNavv2(self):
        """Navigate to the leave balance section."""
        leaveBalanceNav = self.driver.find_element(*self.leaveBalanceV2)
        leaveBalanceNav.click()
        self.driver.implicitly_wait(5)



