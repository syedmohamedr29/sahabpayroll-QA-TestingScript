from playwright.sync_api import Playwright, expect , Page
import pytest

class Menus:

    def __init__(self, page: Page):
        self.page = page

        # organisation
        self.Entities = page.locator("[data-test-id=\"mt_3_11\"]")

        self.MyCompany =  page.locator("[data-test-id=\"mt_3_2\"] [data-test-id=\"y\"]")

        # Report
        self.Reports = page.locator("[data-test-id=\"mt_3_25\"]")

        # Employee
        self.AllEmployees = page.locator("[data-test-id=\"mt_3_3\"] [data-test-id=\"y\"]")

        self.EmployeeExit = page.locator("[data-test-id=\"mt_3_13\"] [data-test-id=\"y\"]")

        # Attendance
        self.Attendance = page.locator("[data-test-id=\"mt_3_12\"] [data-test-id=\"y\"]")

        #
        self.Configuration = page.locator("[data-test-id=\"mt_3_28\"] [data-test-id=\"y\"]")

        # Leave
        self.EncashmentsApplication =page.locator("[data-test-id=\"mt_3_14\"]")

        self.Resumption = page.locator("[data-test-id=\"mt_3_15\"] [data-test-id=\"y\"]")

        self.LeaveType = page.locator("[data-test-id=\"mt_3_5\"]")

        self.LeaveApplication = page.locator("[data-test-id=\"mt_3_16\"] [data-test-id=\"y\"]")

        self.LeaveBalance = page.locator("[data-test-id=\"mt_3_19\"] [data-test-id=\"y\"]")

        # Payrun
        self.PayRun = page.locator("[data-test-id=\"mt_3_27\"]")

        # compbenefits - Managements
        self.Management = page.locator("[data-test-id=\"mt_3_21\"]")

        self.EmployeeSalaries = page.locator("[data-test-id=\"mt_3_26\"]")

        # compbenefits - Configuration
        self.Cfs = page.locator("[data-test-id=\"mt_3_20\"] [data-test-id=\"y\"]")

        # Other
        self.Setting = page.locator("[data-test-id=\"mt_3_23\"]")

        self.Help = page.locator("[data-test-id=\"mt_3_24\"]")


    def entitiesMenu(self):
        try:
            expect(self.Entities).to_be_visible(timeout=3000)
            expect(self.Entities).to_be_enabled()
            self.Entities.click()
            print("✅ Entities Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Entities Menu is Not Visible and Not clickable: {e}")

    def myCompanyMenu(self):
        try:
            expect(self.MyCompany).to_be_visible(timeout=3000)
            expect(self.MyCompany).to_be_enabled()
            self.MyCompany.click()
            print("✅ MyCompany Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ MyCompany Menu is Not Visible and Not clickable: {e}")

    def reportsMenu(self):
        try:
            expect(self.Reports).to_be_visible(timeout=3000)
            expect(self.Reports).to_be_enabled()
            self.Reports.click()
            print("✅ Reports Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Reports Menu is Not Visible and Not clickable: {e}")

    def employeeMenu(self):
        try:
            expect(self.AllEmployees).to_be_visible(timeout=3000)
            expect(self.AllEmployees).to_be_enabled()
            self.AllEmployees.click()
            print("✅ All Employees Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ All Employees Menu is Not Visible and Not clickable: {e}")

    def employeeExitMenu(self):
        try:
            expect(self.EmployeeExit).to_be_visible(timeout=3000)
            expect(self.EmployeeExit).to_be_enabled()
            self.EmployeeExit.click()
            print("✅ EmployeeExit Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ EmployeeExit Menu is Not Visible and Not clickable: {e}")

    def AttendanceMenu(self):
        try:
            expect(self.Attendance).to_be_visible(timeout=3000)
            expect(self.Attendance).to_be_enabled()
            self.Attendance.click()
            print("✅ Attendance Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Attendance Menu is Not Visible and Not clickable: {e}")

    def configurationMenu(self):
        try:
            expect(self.Configuration).to_be_visible(timeout=3000)
            expect(self.Configuration).to_be_enabled()
            self.Configuration.click()
            print("✅ Configuration Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Configuration Menu is Not Visible and Not clickable: {e}")

    def encashmentAppMenu(self):
        try:
            expect(self.EncashmentsApplication).to_be_visible(timeout=3000)
            expect(self.EncashmentsApplication).to_be_enabled()
            self.EncashmentsApplication.click()
            print("✅ Encashment Application Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Encashment Application Menu is Not Visible and Not clickable: {e}")

    def resumptionMenu(self):
        try:
            expect(self.Resumption).to_be_visible(timeout=3000)
            expect(self.Resumption).to_be_enabled()
            self.Resumption.click()
            print("✅ Resumption Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Resumption Menu is Not Visible and Not clickable: {e}")

    def leaveTypeMenu(self):
        try:
            expect(self.LeaveType).to_be_visible(timeout=3000)
            expect(self.LeaveType).to_be_enabled()
            self.LeaveType.click()
            print("✅ LeaveType Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ LeaveType Menu is Not Visible and Not clickable: {e}")

    def LeaveAppMenu(self):
        try:
            expect(self.LeaveApplication).to_be_visible(timeout=3000)
            expect(self.LeaveApplication).to_be_enabled()
            self.LeaveApplication.click()
            print("✅ Leave Application Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Leave Application Menu is Not Visible and Not clickable: {e}")

    def leaveBalanceMenu(self):
        try:
            expect(self.LeaveBalance).to_be_visible(timeout=3000)
            expect(self.LeaveBalance).to_be_enabled()
            self.LeaveBalance.click()
            print("✅ Leave Balance Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Leave Balance Menu is Not Visible and Not clickable: {e}")

    def payrunMenu(self):
        try:
            expect(self.PayRun).to_be_visible(timeout=3000)
            expect(self.PayRun).to_be_enabled()
            self.PayRun.click()
            print("✅ Payrun Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Payrun Menu is Not Visible and Not clickable: {e}")

    def managementMenu(self):
        try:
            expect(self.Management).to_be_visible(timeout=3000)
            expect(self.Management).to_be_enabled()
            self.Management.click()
            print("✅ Management Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Management Menu is Not Visible and Not clickable: {e}")

    def cfsMenu(self):
        try:
            expect(self.Cfs).to_be_visible(timeout=3000)
            expect(self.Cfs).to_be_enabled()
            self.Cfs.click()
            print("✅ Cfs Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Cfs Menu is Not Visible and Not clickable: {e}")

    def employeeSalariesMenu(self):
        try:
            expect(self.EmployeeSalaries).to_be_visible(timeout=3000)
            expect(self.EmployeeSalaries).to_be_enabled()
            self.EmployeeSalaries.click()
            print("✅ Employee Salaries Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Employee Salaries Menu is Not Visible and Not clickable: {e}")

    def settingMenu(self):
        try:
            expect(self.Setting).to_be_visible(timeout=3000)
            expect(self.Setting).to_be_enabled()
            self.Setting.click()
            print("✅ Setting Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Setting Menu is Not Visible and Not clickable: {e}")

    def helpMenu(self):
        try:
            expect(self.Help).to_be_visible(timeout=3000)
            expect(self.Help).to_be_enabled()
            self.Help.click()
            print("✅ Help Menu is Visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Help Menu is Not Visible and Not clickable: {e}")






