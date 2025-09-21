import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from Selenium_Automation.utils.chromeDriverPath import driverPath

# Load configuration from JSON file
configJSONFile = r"C:\Users\Comm-IT India\OneDrive - comm-it india pvt ltd\Desktop\SahabPayroll\Selenium_Automation\resources\URL.json"
with open(configJSONFile) as configURLFile:
    configURL = json.load(configURLFile)

class basePage:

    def __init__(self):
        """Initialize the base page with a WebDriver instance."""
        self.driver = driverPath.getdriver()
        self.wait = WebDriverWait(self.driver, 10)

    def getURL(self):
        """Open the specified URL in the browser."""
        self.driver.get(configURL["baseURL"])
        self.driver.maximize_window()
        print("Current web link:", self.driver.current_url)
        time.sleep(3)

    def redirectURL(self):
        """Wait for the URL to contain the expected part."""
        WebDriverWait(self.driver, 20).until(EC.url_contains(configURL["redirectURL"]))
        time.sleep(3)


    def keepOpen(self, duration=10):
        """Keep the browser open for a specified duration."""
        time.sleep(duration)

    def closeDriver(self):
        """Close the browser."""
        self.driver.quit()
        print("Browser closed.")

