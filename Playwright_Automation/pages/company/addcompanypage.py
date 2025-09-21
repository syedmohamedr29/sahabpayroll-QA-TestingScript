import pytest
from playwright.sync_api import expect, Page


class AddCompany:

    def __init__(self, page: Page):
        self.page = page

# Form Builder

        self.FormBuilder1 = page.get_by_text("Basic Details")

        self.FormBuilder2 = page.get_by_text("Address Information")

        self.FormBuilder3 = page.get_by_text("Contact Details")

        self.FormBuilder4 = page.get_by_text("Local & Display Settings")

        self.FormBuilder5 = page.get_by_text("Review & Submit")

        self.Heading = page.get_by_text("Add Company")

# Basic Details

        self.CloseIcon = page.get_by_role("img")

        self.LogoUpload = page.locator("[data-test-id=\"iBasicInformationFileUpload\"] div").filter(
            has_text="Click to upload or drag and").nth(3)
        self.LogoUpload = self.page.locator("[data-test-id='iBasicInformationFileUpload'] input[type='file']")
        #page.get_by_text("Basic Information", exact=True)

        self.CompanyNameEnPlaceholder = page.locator("[data-test-id=\"iBasicInformationName\"] [data-test-id=\"eInput\"]")

        self.CompanyNameArPlaceholder = page.get_by_role("textbox", name="الإسكان")

        self.CompanyNameHinPlaceholder = page.locator("app-zw-text-box").filter(has_text="Hindi").locator("[data-test-id=\"eInput\"]")

        self.DropDownCloseIcon = page.get_by_role("button", name="Close")

        self.ShortCodePlaceholder = page.locator("[data-test-id=\"ishortCode\"] [data-test-id=\"eInput\"]")

        self.IndustryDropDown = page.get_by_role("combobox", name="Select")

        self.IndustryDropDownValueSelect = page.get_by_role("listbox", name="Option List")

        self.WebsitePlaceholder = page.get_by_role("textbox", name="Enter").nth(2)
            #page.locator("[data-test-id=\"eInput\"]").nth(2))


        self.TaxIdPlaceholder = page.get_by_role("textbox", name="Enter").nth(3)
        #page.locator("[data-test-id=\"eInput\"]").nth(3)

        self.CompanyIdPlaceholder = page.locator("[data-test-id=\"iBasicInformationCompanyId\"] [data-test-id=\"eInput\"]")

# Address Information

        self.AddressLine1Placeholder = page.locator("[data-test-id=\"iAddressLine1\"] [data-test-id=\"eInput\"]")

        self.AddressLine2Placeholder = page.locator("[data-test-id=\"iAddressLine2\"] [data-test-id=\"eInput\"]")

        self.CountrySelectionDropdown = page.get_by_role("button", name="dropdown trigger")

        self.StatePlaceholder = page.locator("[data-test-id=\"iAddressState\"] [data-test-id=\"eInput\"]")

        self.CityPlaceholder = page.locator("[data-test-id=\"iAddressCity\"] [data-test-id=\"eInput\"]")

        self.PincodePlaceholder = page.locator("[data-test-id=\"ipinCode\"] [data-test-id=\"eInput\"]")

        self.AddAddressBtn = page.get_by_role("button", name=" Add New Address")

        self.SameAddressChecklist = page.locator("[data-test-id=\"v\"] div").nth(2)

        self.AddressLine1Placeholder2 = page.locator("[data-test-id=\"iAddressLine1Fill\"] [data-test-id=\"eInput\"]")

        self.AddressLine2Placeholder2 = page.locator("[data-test-id=\"iAddressLine2Fill\"] [data-test-id=\"eInput\"]")

        self.CountrySelectionDropdown2 = page.locator("[data-test-id=\"iAddressCountryFill\"]").get_by_role("button", name="dropdown trigger")

        self.StatePlaceholder2 = page.locator("[data-test-id=\"iAddressStateFill\"] [data-test-id=\"eInput\"]")

        self.CityPlaceholder2 = page.locator("[data-test-id=\"iAddressCityFill\"] [data-test-id=\"eInput\"]")

        self.PincodePlaceholder2 = page.locator("[data-test-id=\"ipinCodeFill\"] [data-test-id=\"eInput\"]")

        # Primary adress = Secondary

# Contact Details

        self.PrimaryContactPlaceholder = page.locator("[data-test-id=\"iContactName\"] [data-test-id=\"eInput\"]")

        self.PrimaryEmailPlaceholder = page.locator("[data-test-id=\"iContactEmail\"] [data-test-id=\"eInput\"]")

        self.PrimaryNumberPlaceholder = page.locator("[data-test-id=\"iContactNumber\"] [data-test-id=\"eInput\"]")

        self.AddSecondaryBtn = page.get_by_role("button", name=" Add New Contact")

        self.SecondaryContactPlaceholder = page.get_by_role("textbox", name="Enter").nth(2)

        self.SecondaryEmailPlaceholder = page.get_by_role("textbox", name="Enter").nth(3)

        self.SecondaryNumberPlaceholder = page.get_by_role("spinbutton").nth(1)

# # Local & Display Settings
        # Target by class
        self.CountryRegionDropdown = page.get_by_role("combobox", name="Select").nth(0)

        #self.CountryRegionDropdown = page.locator("#pn_id_386").get_by_role("combobox", name="Select")
        #   page.locator("#pn_id_386").get_by_role("combobox", name="Select").click()
            #page.locator("#pn_id_188").get_by_role("combobox", name="Select")

        self.TimeZoneDropDown = page.locator("[data-test-id=\"iLocalDisplayTimeZone\"]").get_by_role("combobox", name="Select")

        self.CurrencyDropdown = page.locator("[data-test-id=\"iLocalDisplayCurrency\"]").get_by_role("combobox", name="Select")

        self.DateFormatDropdown = page.locator("[data-test-id=\"iLocalDisplayDateFormat\"]").get_by_role("combobox", name="Select")

        self.TimeFormatDropdown = page.locator("[data-test-id=\"iLocalDisplayTimeFormat\"]").get_by_role("combobox", name="Select")

# Common

        self.FrstOption = page.get_by_role("option", name="Arabic")

        self.SndOption = page.get_by_role("option", name="Hindi")

        self.ThirdOption = page.get_by_role("option", name="English")

        self.LanguageDropdown = page.locator("[data-test-id=\"aPMultiSelect\"] div").filter(has_text="Select").nth(1)
        self.UnSelectCheckList = page.get_by_role("checkbox", name="All items selected").nth(1)

        self.SelectCheckList = page.get_by_role("checkbox", name="All items unselected").nth(1)

        self.RemoveBtn = page.get_by_role("button", name=" Remove")

        self.PreviousBtn = page.get_by_role("button", name=" Previous")

        self.DropdownSearchBox = page.get_by_role("searchbox", name="Search")

        self.DropDownPlaceHolder = page.get_by_role("searchbox")

        self.NextBtn = page.get_by_role("button", name=" Next")

# Review & Submit

        self.SubmitBtn = page.get_by_role("button", name="Submit")

# Form Builder
    def formBuilder(self):
        try:
            expect(self.FormBuilder1).to_be_visible(timeout=3000)
            expect(self.FormBuilder2).to_be_visible(timeout=3000)
            expect(self.FormBuilder3).to_be_visible(timeout=3000)
            expect(self.FormBuilder4).to_be_visible(timeout=3000)
            expect(self.FormBuilder5).to_be_visible(timeout=3000)
            print("✅ All Form Builder is Visible")
        except Exception as e:
            pytest.fail(f"❌ form builder is Not Visible: {e}")

# Basic Details
    def closeIcon(self):
        try:
            expect(self.CloseIcon).to_be_visible(timeout=3000)
            expect(self.CloseIcon).to_be_enabled()
            self.CloseIcon.click()
            print("✅ Close Icon Menu is Visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Close Icon is Not Visible and Not clickable: {e}")

    def logoUpload(self, LogoUploadPath):
        try:
            expect(self.LogoUpload).to_be_visible()
            self.LogoUpload.click()
            self.LogoUpload.set_input_files(LogoUploadPath)
            print("✅ Image uploaded successfully")
        except Exception as e:
            pytest.fail(f"❌ LogoUpload failed: {e}")

    def companyEnNameFilling(self,CompanyNameEN):
        try:
            expect(self.CompanyNameEnPlaceholder).to_be_visible(timeout=3000)
            expect(self.CompanyNameEnPlaceholder).to_be_enabled()
            self.CompanyNameEnPlaceholder.fill(CompanyNameEN)
            print("✅ Placeholder visible, enable and use can able to fill the company english name")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send English Name: {e}")

    def companyArNameFilling(self,CompanyNameAR):
        try:
            expect(self.CompanyNameArPlaceholder).to_be_visible(timeout=3000)
            expect(self.CompanyNameArPlaceholder).to_be_enabled()
            self.CompanyNameArPlaceholder.fill(CompanyNameAR)
            print("✅ Placeholder visible, enable and use can able to fill the company Arabic name")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Arabic Name: {e}")

    def companyNameHinFilling(self):
        try:
            expect(self.CompanyNameHinPlaceholder).to_be_visible(timeout=3000)
            expect(self.CompanyNameHinPlaceholder).to_be_enabled()
            self.CompanyNameHinPlaceholder.fill("टेस्ट कंपनी हिंदी")
            print("✅ Placeholder visible, enable and use can able to fill the company Hindi name")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Hindi Name: {e}")

    def shortCode(self,shortcode):
        try:
            expect(self.ShortCodePlaceholder).to_be_visible(timeout=3000)
            expect(self.ShortCodePlaceholder).to_be_enabled()
            self.ShortCodePlaceholder.fill(shortcode)
            print("✅ Placeholder visible, enable and use can able to fill the Short Code")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to Short Code: {e}")


    def industryDropdown(self):
        try:
            expect(self.IndustryDropDown).to_be_visible(timeout=3000)
            self.IndustryDropDown.click()
            print("✅ Can able to Click on the Dropdown")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

    def industryValueSelect(self):
        try:
            expect(self.IndustryDropDownValueSelect).to_be_visible(timeout=3000)
            self.IndustryDropDownValueSelect.click()
            print("✅ Can able to Select the Value")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to Select the dropdown: {e}")

    def website(self,url):
        try:
            expect(self.WebsitePlaceholder).to_be_visible(timeout=3000)
            expect(self.WebsitePlaceholder).to_be_enabled()
            self.WebsitePlaceholder.fill(url)
            print("✅ Placeholder visible, enable and use can able to fill the website")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to website: {e}")

    def taxId(self,taxid):
        try:
            expect(self.TaxIdPlaceholder).to_be_visible(timeout=3000)
            expect(self.TaxIdPlaceholder).to_be_enabled()
            self.TaxIdPlaceholder.fill(taxid)
            print("✅ Placeholder visible, enable and use can able to fill the Tax Id")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to Tax id: {e}")

    def companyId(self,compid):
        try:
            expect(self.CompanyIdPlaceholder).to_be_visible(timeout=3000)
            expect(self.CompanyIdPlaceholder).to_be_enabled()
            self.CompanyIdPlaceholder.fill(compid)
            print("✅ Placeholder visible, enable and use can able to fill the company id")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send company id: {e}")




# Address Information

    def primaryAddressLine1(self,Padress1):
        try:
            expect(self.AddressLine1Placeholder).to_be_visible(timeout=3000)
            expect(self.AddressLine1Placeholder).to_be_enabled()
            self.AddressLine1Placeholder.fill(Padress1)
            print("✅ Placeholder visible, enable and use can able to fill the Address Line 1")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to Address Line 1: {e}")

    def primaryAddressLine2(self, Padress2):
        try:
            expect(self.AddressLine2Placeholder).to_be_visible(timeout=3000)
            expect(self.AddressLine2Placeholder).to_be_enabled()
            self.AddressLine2Placeholder.fill(Padress2)
            print("✅ Placeholder visible, enable and use can able to fill the Address Line 2")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to Address Line 2: {e}")

    def countrySelectDropdown(self):
        try:
            expect(self.CountrySelectionDropdown).to_be_visible(timeout=3000)
            self.CountrySelectionDropdown.click()
            print("✅ Can able to Click on the Dropdown")

        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

    def state1(self, pstate):  # Added missing method for StatePlaceholder
        try:
            expect(self.StatePlaceholder).to_be_visible(timeout=3000)
            expect(self.StatePlaceholder).to_be_enabled()
            self.StatePlaceholder.fill(pstate)
            print("✅ Placeholder visible, enable and use can able to fill the State")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to State: {e}")

    def city1(self,pcity):
        try:
            expect(self.CityPlaceholder).to_be_visible(timeout=3000)
            expect(self.CityPlaceholder).to_be_enabled()
            self.CityPlaceholder.fill(pcity)
            print("✅ Placeholder visible, enable and use can able to fill the City")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to City: {e}")

    def pincode1(self, ppincode):
        try:
            expect(self.PincodePlaceholder).to_be_visible(timeout=3000)
            expect(self.PincodePlaceholder).to_be_enabled()
            self.PincodePlaceholder.fill(ppincode)
            print("✅ Placeholder visible, enable and use can able to fill the Pin Code")
        except Exception as e:
                pytest.fail(f"❌ User cannot able to Pin Code: {e}")

    def addAddressBtn(self):
        try:
            expect(self.AddAddressBtn).to_be_visible(timeout=3000)
            expect(self.AddAddressBtn).to_be_enabled()
            self.AddAddressBtn.click()
            print("✅ Add Address Btn button is visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to Add Address Btn: {e}")

    def sameAddressChecklist(self):
        try:
            expect(self.SameAddressChecklist).to_be_visible(timeout=3000)
            expect(self.SameAddressChecklist).to_be_enabled()
            self.SameAddressChecklist.click()
            print("✅ Same Address CheckList button is visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to Same Address CheckList: {e}")

    def primaryAddress2Line1(self,saddress1):
        try:
            expect(self.AddressLine1Placeholder2).to_be_visible(timeout=3000)
            expect(self.AddressLine1Placeholder2).to_be_enabled()
            self.AddressLine1Placeholder2.fill(saddress1)
            print("✅ Placeholder visible, enable and use can able to fill the Address Line 1")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to Address Line 1: {e}")

    def primaryAddress2Line2(self,saddress2):
        try:
            expect(self.AddressLine2Placeholder2).to_be_visible(timeout=3000)
            expect(self.AddressLine2Placeholder2).to_be_enabled()
            self.AddressLine2Placeholder2.fill(saddress2)
            print("✅ Placeholder visible, enable and use can able to fill the Address Line 2")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to Address Line 2: {e}")

    def countrySelectDropdown2(self):
        try:
            expect(self.CountrySelectionDropdown2).to_be_visible(timeout=3000)
            self.CountrySelectionDropdown2.click()
            print("✅ Can able to Click on the Dropdown")

        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

    def state2(self, sstate):  # Added missing method for StatePlaceholder2
        try:
            expect(self.StatePlaceholder2).to_be_visible(timeout=3000)
            expect(self.StatePlaceholder2).to_be_enabled()
            self.StatePlaceholder2.fill(sstate)
            print("✅ Placeholder visible, enable and use can able to fill the State")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to State: {e}")

    def city2(self,scity):
        try:
            expect(self.CityPlaceholder2).to_be_visible(timeout=3000)
            expect(self.CityPlaceholder2).to_be_enabled()
            self.CityPlaceholder2.fill(scity)
            print("✅ Placeholder visible, enable and use can able to fill the City")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to City: {e}")

    def pincode2(self,spincode):
        try:
            expect(self.PincodePlaceholder2).to_be_visible(timeout=3000)
            expect(self.PincodePlaceholder2).to_be_enabled()
            self.PincodePlaceholder2.fill(spincode)
            print("✅ Placeholder visible, enable and use can able to fill the Pin Code")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to Pin Code: {e}")



    # same value primary and secondary address -  Primary adress = Secondary


# Contact Details

    def primaryContact(self,primarycontact):
        try:
            expect(self.PrimaryContactPlaceholder).to_be_visible(timeout=3000)
            expect(self.PrimaryContactPlaceholder).to_be_enabled()
            self.PrimaryContactPlaceholder.fill(primarycontact)
            print("✅ Placeholder visible, enable and use can able to fill the Contact Name")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Contact Name: {e}")

    def primaryEmail(self,primaryemail):
        try:
            expect(self.PrimaryEmailPlaceholder).to_be_visible(timeout=3000)
            expect(self.PrimaryEmailPlaceholder).to_be_enabled()
            self.PrimaryEmailPlaceholder.fill(primaryemail)
            print("✅ Placeholder visible, enable and use can able to fill the Email")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Email: {e}")

    def primaryNumber(self,primarynumber):
        try:
            expect(self.PrimaryNumberPlaceholder).to_be_visible(timeout=3000)
            expect(self.PrimaryNumberPlaceholder).to_be_enabled()
            self.PrimaryNumberPlaceholder.fill(primarynumber)
            print("✅ Placeholder visible, enable and use can able to fill the Number")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Number: {e}")

    def addSenBtn(self):
        try:
            expect(self.AddSecondaryBtn).to_be_visible(timeout=3000)
            expect(self.AddSecondaryBtn).to_be_enabled()
            self.AddSecondaryBtn.click()
            print("✅ Add Secondary button is visible and clickable")

        except Exception as e:
            pytest.fail(f"❌ Cannot able to Add Secondary: {e}")

    def secondaryContact(self,secondarycontact):
        try:
            expect(self.SecondaryContactPlaceholder).to_be_visible(timeout=3000)
            expect(self.SecondaryContactPlaceholder).to_be_enabled()
            self.SecondaryContactPlaceholder.fill(secondarycontact)
            print("✅ Placeholder visible, enable and use can able to fill the Contact Name")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Contact Name: {e}")

    def secondaryEmail(self,secondaryemial):
        try:
            expect(self.SecondaryEmailPlaceholder).to_be_visible(timeout=3000)
            expect(self.SecondaryEmailPlaceholder).to_be_enabled()
            self.SecondaryEmailPlaceholder.fill(secondaryemial)
            print("✅ Placeholder visible, enable and use can able to fill the Email")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Email: {e}")

    def secondaryNumber(self,secondarynumber):
        try:
            expect(self.SecondaryNumberPlaceholder).to_be_visible(timeout=3000)
            expect(self.SecondaryNumberPlaceholder).to_be_enabled()
            self.SecondaryNumberPlaceholder.fill(secondarynumber)
            print("✅ Placeholder visible, enable and use can able to fill the Number")

        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Number: {e}")

# Local & Display Settings

    def countryRegionFormatDropdown(self):
        try:
            expect(self.CountryRegionDropdown).to_be_visible(timeout=5000)
            expect(self.CountryRegionDropdown).to_be_enabled()
            self.CountryRegionDropdown.click()
            print("✅ Country/Region dropdown clicked successfully")
        except Exception as e:
            pytest.fail(f"❌ Cannot click Country/Region dropdown: {e}")

    def timeZonFormatDropdown(self):
        try:
            expect(self.TimeZoneDropDown).to_be_visible(timeout=3000)
            expect(self.TimeZoneDropDown).to_be_enabled()
            self.TimeZoneDropDown.click()
            print("✅ Can able to Click on the Dropdown")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

    def currencyFormatDropdown(self):
        try:
            expect(self.CurrencyDropdown).to_be_visible(timeout=3000)
            expect(self.CurrencyDropdown).to_be_enabled()
            self.CurrencyDropdown.click()
            print("✅ Can able to Click on the Dropdown")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

    def dateFormatDropdown(self):
        try:
            expect(self.DateFormatDropdown).to_be_visible(timeout=3000)
            expect(self.DateFormatDropdown).to_be_enabled()
            self.DateFormatDropdown.click()
            print("✅ Can able to Click on the Dropdown")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

    def timeFormatDropdown(self):
        try:
            expect(self.TimeFormatDropdown).to_be_visible(timeout=3000)
            expect(self.TimeFormatDropdown).to_be_enabled()
            self.TimeFormatDropdown.click()
            print("✅ Can able to Click on the Dropdown")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

# Common

    def languageDropdown(self):
        try:
            expect(self.LanguageDropdown).to_be_visible(timeout=3000)
            expect(self.LanguageDropdown).to_be_enabled()
            self.LanguageDropdown.click()
            print("✅ Can able to Click on the Dropdown")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click on the dropdown: {e}")

    def firstOption(self):
        try:
            expect(self.FrstOption).to_be_visible(timeout=3000)
            self.FrstOption.click()
            print("✅ First Option Can able to select")
        except Exception as e:
            pytest.fail(f"❌ First Option Cannot able to click: {e}")

    def secondOption(self):
        try:
            expect(self.SndOption).to_be_visible(timeout=3000)
            self.SndOption.click()
            print("✅ Second Option Can able to select")
        except Exception as e:
            pytest.fail(f"❌ Second Option Cannot able to click: {e}")

    def thirdOption(self):
        try:
            expect(self.ThirdOption).to_be_visible(timeout=3000)

            self.ThirdOption.click()
            print("✅ Third Option Can able to select")
        except Exception as e:
            pytest.fail(f"❌ Third Option Cannot able to click: {e}")

    def dropdownCloseIconClick(self):
        try:
            expect(self.DropDownCloseIcon).to_be_visible(timeout=3000)
            expect(self.DropDownCloseIcon).to_be_enabled()
            self.DropDownCloseIcon.click()
            print("✅ Dropdown Close Icon is Visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Drop down Close Icon is Not Visible and Not clickable: {e}")

    def dropdownSearchBoxFilling(self,search):
        try:
            expect(self.DropdownSearchBox).to_be_visible(timeout=3000)
            expect(self.DropdownSearchBox).to_be_enabled()
            self.DropdownSearchBox.fill(search)
            print("✅ Placeholder visible, enable and use can able to fill the details")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Details: {e}")

    def dropdownPlaceholderFilling(self):
        try:
            expect(self.DropDownPlaceHolder).to_be_visible(timeout=3000)
            expect(self.DropDownPlaceHolder).to_be_enabled()
            self.DropDownPlaceHolder.fill("placeholder value")
            print("✅ Placeholder visible, enable and use can able to fill the details")
        except Exception as e:
            pytest.fail(f"❌ User cannot able to send Details: {e}")

    def unSelectAllCheckList(self):
        try:
            expect(self.UnSelectCheckList).to_be_visible(timeout=3000)
            expect(self.UnSelectCheckList).to_be_enabled()
            self.UnSelectCheckList.uncheck()
            print("✅ Un Select the all Checklist option")
        except Exception as e:
            pytest.fail(f"❌ Unable to Un select all the checklist options: {e}")

    def selectAllCheckList(self):
        try:
            expect(self.SelectCheckList).to_be_visible(timeout=3000)
            expect(self.SelectCheckList).to_be_enabled()
            self.SelectCheckList.check()
            print("✅ Select the all Checklist option")
        except Exception as e:
            pytest.fail(f"❌ Unable to select all the checklist options: {e}")

    def removeBtnClk(self):
        try:
            expect(self.RemoveBtn).to_be_visible(timeout=3000)
            expect(self.RemoveBtn).to_be_enabled()
            self.RemoveBtn.click()
            print("✅ Remove button is visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click remove button: {e}")

    def previousBtnClk(self):
        try:
            expect(self.PreviousBtn).to_be_visible(timeout=3000)
            expect(self.PreviousBtn).to_be_enabled()
            self.PreviousBtn.click()
            print("✅ previous button is visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click previous button: {e}")

    def nextBtnClk(self):
        try:
            expect(self.NextBtn).to_be_visible(timeout=3000)
            expect(self.NextBtn).to_be_enabled()
            self.NextBtn.click()
            print("✅ Next button is visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to click Next button: {e}")

# Review & Submit

    def submitBtnClk(self):
        try:
            expect(self.SubmitBtn).to_be_visible(timeout=3000)
            expect(self.SubmitBtn).to_be_enabled()
            self.SubmitBtn.click()
            print("✅ Form submit button is visible and clickable")
        except Exception as e:
            pytest.fail(f"❌ Cannot able to submit form: {e}")