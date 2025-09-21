import re
from playwright.sync_api import expect
import json

urlfile = r"C:\Users\Comm-IT India\OneDrive - comm-it india pvt ltd\Desktop\SahabPayroll\Playwright_Automation\resources\weblogin\webUrl.json"
with open(urlfile) as jsonFile:
    auth = json.load(jsonFile)

class Webpage:

    def __init__(self, page):
        """Initialize with Playwright Page fixture."""
        self.page = page

    def getURL(self):
        """Open the specified URL in the browser."""
        #self.page.goto(auth["baseURL"])
        self.page.goto(auth["v2Url"])
        print("✅ Current web link:", self.page.url)
        self.page.evaluate("localStorage.clear(); sessionStorage.clear();")

    def redirectURL(self):
        """Wait for redirect URL."""
        expect(self.page).to_have_url(
            re.compile(auth["redirectURL"]),
            timeout=15000  # wait up to 15s
        )
        self.page.evaluate("localStorage.clear(); sessionStorage.clear();")

    def keepOpen(self, duration=10):
        """Keep the browser open for a specified duration."""
        print("Current web link:", self.page.url),
        self.page.wait_for_timeout(duration * 1000)

    def wait(self, duration=2):
        """Wait for a specified duration in seconds."""
        self.page.wait_for_timeout(duration * 1000)

    def closeBrowser(self):
        """Close the browser."""
        print("✅ Browser closed.")
        self.page.context.browser.close()
