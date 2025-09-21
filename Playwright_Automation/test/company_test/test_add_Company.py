
from Playwright_Automation.utils.webPage import Webpage
from Playwright_Automation.pages.login.loginpage import LoginPage
import time
from  Playwright_Automation.pages.company.entitiespage import Entities
from Playwright_Automation.pages.menus.menus import Menus
from Playwright_Automation.pages.company.addcompanypage import AddCompany
import pytest
import json



companyAddJSONFile = r"C:\Users\Comm-IT India\OneDrive - comm-it india pvt ltd\Desktop\SahabPayroll\Playwright_Automation\resources\weblogin\company\company.json"
with open(companyAddJSONFile, "r", encoding="utf-8") as jsonFile:
    companyAdd = json.load(jsonFile)
class TestAddCompany:
    @pytest.fixture(autouse=True)
    def setup(self,page):
            self.base = Webpage(page)
            self.login = LoginPage(page)
            self.menu = Menus(page)
            self.entities = Entities(page)
            self.addCompany = AddCompany(page)

            # Base File
            self.base.getURL()
            self.base.redirectURL()
            self.base.keepOpen(10)

            self.login.enterButtonClick()
            self.login.tenantPopupVisible()
            self.login.tenantName()
            self.login.saveBtnClick()
            self.login.username()
            self.login.password()
            self.login.signin()
            time.sleep(10)
            # Entities
            self.menu.entitiesMenu()
            time.sleep(5)

            self.entities.addCompanyBtn()
            time.sleep(5)



    def test_verify_AddCompany(self):

        actions = [
            (self.addCompany.companyEnNameFilling, companyAdd["basicDetails"]["companyName"]["en"]["name"],
             "Company English Name"),
            (self.addCompany.languageDropdown, None, "Language Dropdown"),
            (self.addCompany.firstOption, None, "First Language Option"),
            (self.addCompany.dropdownCloseIconClick, None, "Dropdown Close Icon"),
            (self.addCompany.companyArNameFilling, companyAdd["basicDetails"]["companyName"]["ar"]["name"],
             "Company Arabic Name"),
            (self.addCompany.shortCode, companyAdd["basicDetails"]["shortCode"], "Short Code"),
            (self.addCompany.industryDropdown, None, "Industry Dropdown"),
            (self.addCompany.dropdownSearchBoxFilling, "Manufacturing", "Industry Search"),
            (self.addCompany.industryValueSelect, None, "Industry Option"),
            (self.addCompany.website, companyAdd["basicDetails"]["webSiteUrl"], "Website"),
            (self.addCompany.taxId, companyAdd["basicDetails"]["companyTaxID"], "Tax ID"),
            (self.addCompany.companyId, companyAdd["basicDetails"]["companyID"], "Company ID"),
            (self.addCompany.nextBtnClk, None, "Click on Next Button"),
            (self.addCompany.primaryAddressLine1,
             companyAdd["localeSettings"]["addresses"]["addresses"][0]["addressLine1"], "Primary Address Line 1"),
            (self.addCompany.primaryAddressLine2,
             companyAdd["localeSettings"]["addresses"]["addresses"][0]["addressLine2"], "Primary Address Line 2"),
            (self.addCompany.countrySelectDropdown,None , "Click on Dropdown"),
            (self.addCompany.dropdownSearchBoxFilling, "Saudi Arabia", "Country Search"),
            (self.addCompany.industryValueSelect, None , "Select the country"),
            (self.addCompany.state1, companyAdd["localeSettings"]["addresses"]["addresses"][0]["state"], "State"),
            (self.addCompany.city1, companyAdd["localeSettings"]["addresses"]["addresses"][0]["city"], "City"),
            (self.addCompany.pincode1, companyAdd["localeSettings"]["addresses"]["addresses"][0]["pinCode"], "Pin Code"),
            (self.addCompany.addAddressBtn, None, "Secondary address form is Shown"),
            (self.addCompany.sameAddressChecklist, None,  "Secondary address Shown Primary address details shown"),
            (self.addCompany.nextBtnClk, None, "Click on Next Button"),  # Assuming a Next button exists
            (self.addCompany.primaryEmail, companyAdd["contacts"]["contact"][0]["emailId"], "Primary Email"),
            (self.addCompany.primaryContact, companyAdd["contacts"]["contact"][0]["contactName"], "Primary Contact"),
            (self.addCompany.primaryNumber, companyAdd["contacts"]["contact"][0]["contactNumber"], "Primary Number"),
            (self.addCompany.addSenBtn, None, " Add new secondary contact"),
            (self.addCompany.secondaryEmail, companyAdd["contacts"]["contact"][1]["emailId"], "Secondary Email"),
            (self.addCompany.secondaryContact, companyAdd["contacts"]["contact"][1]["contactName"], "Secondary Contact"),
            (self.addCompany.secondaryNumber, companyAdd["contacts"]["contact"][1]["contactNumber"], "Secondary Number"),
            (self.addCompany.nextBtnClk, None, "Click on Next Button"),  # Assuming a Next button exists
            (self.addCompany.countryRegionFormatDropdown, None, "Click on dropdown"),
            (self.addCompany.dropdownSearchBoxFilling, companyAdd["localeSettings"]["localeSettings"]["countryRegion"]["englishName"], "Search Saudi Arabia"),
            (self.addCompany.industryValueSelect, None, "Select the Region"),
            (self.addCompany.timeZonFormatDropdown, None, "Click on dropdown"),
            (self.addCompany.dropdownSearchBoxFilling, companyAdd["localeSettings"]["localeSettings"]["timeZone"]["displayName"], "Timezone Search"),
            (self.addCompany.industryValueSelect, None, "Select the TimeZone"),
            (self.addCompany.currencyFormatDropdown, None, "Click on dropdown"),
            (self.addCompany.dropdownSearchBoxFilling, companyAdd["localeSettings"]["localeSettings"]["currency"]["currencyName"], "Currency Search"),
            (self.addCompany.industryValueSelect, None, "Select the Currency"),
            (self.addCompany.dateFormatDropdown, None, "Click on dropdown"),
            (self.addCompany.dropdownSearchBoxFilling, companyAdd["displaySettings"]["dateFormat"]["dateFormat"],"Date Format Search"),
            (self.addCompany.industryValueSelect, None, "Select the Date Format"),
            (self.addCompany.timeFormatDropdown,None, "click on the time format"),
            (self.addCompany.dropdownSearchBoxFilling, companyAdd["displaySettings"]["timeFormat"]["timeFormat"], "Time Format Search"),
            (self.addCompany.industryValueSelect, None, "Select the time Format"),
            (self.addCompany.languageDropdown, None, "language dropdown clik"),
            (self.addCompany.firstOption, None, "Select the First Option"),
            (self.addCompany.thirdOption, None, "Select the second Option"),
            (self.addCompany.dropdownCloseIconClick, None, "Dropdown Close Icon"),
            (self.addCompany.nextBtnClk, None, "Click on Next Button")  # Assuming a Next button exists

        ]

        for action, value, name in actions:
            try:
                if value is not None:
                    action(value)
                else:
                    action()  # Call method without arguments (e.g., click)
                print(f"✅ {name} executed successfully")
            except Exception as e:
                pytest.fail(f"❌ Failed to execute {name}: {str(e)}")


        #assert self.addCompany.is_address_page_visible(), "Successfully navigate to the Address Information Page"

        time.sleep(10)


    """
        try:
            time.sleep(3)
            self.addCompany.companyEnNameFilling(
                companyAdd["basicDetails"]["companyName"]["en"]["name"]
            )
            time.sleep(3)
            print("✅ Company English Name entered successfully")
        except Exception as e:
            pytest.fail(f"❌ Unable to enter En company name: {str(e)}")

        try:
            self.addCompany.languageDropdown()
            print("✅ User Can able to click on Language Dropdown successfully")
        except Exception as e:
            pytest.fail(f"❌ Unable to Click Language Dropdown: {str(e)}")

        try :
            time.sleep(3)
            self.addCompany.firstOption()
        except Exception as e:
            pytest.fail(f"❌ Unable to Click Language Dropdown: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.dropdownCloseIconClick()
        except Exception as e:
            pytest.fail(f"❌ Unable to Click Close Icon: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.companyArNameFilling(
                companyAdd["basicDetails"]["companyName"]["ar"]["name"]
            )
            time.sleep(3)
            print("✅ Company Arabic Name entered successfully")
        except Exception as e:
            pytest.fail(f"❌ Unable to enter company ar name: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.shortCode(
                companyAdd["basicDetails"]["shortCode"]
            )
            time.sleep(3)
            print("✅ Company Short Code entered successfully")
        except Exception as e:
            pytest.fail(f"❌ Unable to enter company short code: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.industryDropdown()
        except Exception as e:
            pytest.fail(f"❌ Unable to Click Industry Dropdown: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.dropdownSearchBoxFilling("Manufacturing")
        except Exception as e:
            pytest.fail(f"❌ Unable to search Industry: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.industryValueSelect()
        except Exception as e:
            pytest.fail(f"❌ Unable to Click Industry Dropdown: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.website(
                companyAdd["basicDetails"]["webSiteUrl"]
            )
            time.sleep(3)
            print("✅ Company Website entered successfully")
        except Exception as e:
            pytest.fail(f"❌ Unable to enter company website: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.taxId(
                companyAdd["basicDetails"]["companyTaxID"]
            )
            time.sleep(3)
            print("✅ Company Tax Id entered successfully")
        except Exception as e:
            pytest.fail(f"❌ Unable to enter company Tax Id: {str(e)}")

        try:
            time.sleep(3)
            self.addCompany.companyId(
                companyAdd["basicDetails"]["companyID"]
            )
            time.sleep(3)
            print("✅ Company Id entered successfully")
        except Exception as e:
            pytest.fail(f"❌ Unable to enter company Id: {str(e)}")

    """



    def test_verify_formBuilder(self):
            try:
                self.addCompany.formBuilder()
                print("✅ Pass - Successfully shown formBuilder")
            except Exception as e:
                pytest.fail(f"❌ FormBuilder failed: {str(e)}")




