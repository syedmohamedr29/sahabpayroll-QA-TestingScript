import time

from utils.basPage import basePage
from pages.login.loginPage import loginPage
from pages.navigate2ndURL.companySelect import companySelect
from pages.navigate2ndURL.navBar import navigate

if __name__  == '__main__':
    """Login Page"""
    basePageFunc = basePage()
    basePageFunc.getURL()
    basePageFunc.redirectURL()
    basePageFunc.keepOpen()

    loginPageFunc = loginPage(basePageFunc.driver)
    time.sleep(3)
    loginPageFunc.eneterButtonClick()
    time.sleep(3)
    loginPageFunc.enterTenantName("mscan")
    time.sleep(3)
    loginPageFunc.saveTenant()
    time.sleep(3)
    loginPageFunc.useName("syed.mohamed@comm-it.in")
    time.sleep(3)
    loginPageFunc.password("Admin@123")
    time.sleep(3)
    loginPageFunc.loginButtonClick()
    time.sleep(3)

    companySelectFunc = companySelect(basePageFunc.driver)
    time.sleep(3)
    companySelectFunc.selectLastCompany()

    time.sleep(3)
    navbarFunc = navigate(basePageFunc.driver)
    navbarFunc.switchV2()

    time.sleep(20)

    basePageFunc.closeDriver()
