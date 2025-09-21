from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class driverPath:
    chromeDriverPath = "C:/Users/Comm-IT India/OneDrive - comm-it india pvt ltd/Desktop/SahabPayroll/Selenium_Automation/drivers/chromedriver-win64/chromedriver.exe"
    #service = Service(chromeDriverPath)
    #driver = webdriver.Chrome(service=service)
    service = Service(chromeDriverPath  )


    @classmethod
    def getdriver(cls):
        return webdriver.Chrome(service=cls.service)

