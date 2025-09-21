from Playwright_Automation.pages.menus.menus import Menus
from Playwright_Automation.utils.webPage import Webpage
from Playwright_Automation.pages.login.loginpage import LoginPage
import time
from  Playwright_Automation.pages.company.entitiespage import Entities
from Playwright_Automation.pages.company.addcompanypage import AddCompany

# playwright codegen --browser=chromium https://sp.dev.zoolwork.com/

def test_open_site(page):
    base = Webpage(page)
    login = LoginPage(page)
    menu = Menus(page)
    entities = Entities(page)
    addCompany = AddCompany(page)

# Base File
    base.getURL()
    base.redirectURL()
    base.keepOpen(10)

    login.enterButtonClick()
    login.tenantPopupVisible()
    login.tenantName()
    login.saveBtnClick()
    login.username()
    login.password()
    login.signin()
    time.sleep(10)
# Entities
    menu.entitiesMenu()
    time.sleep(5)

    #entities.addCompanyBtn()
    #time.sleep(5)

# Add Company
    #addCompany.formBuilder()


    #time.sleep(15)

    base.closeBrowser()