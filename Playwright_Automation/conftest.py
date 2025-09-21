import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright():
    """Start Playwright once per test session"""
    pw = sync_playwright().start()
    yield pw
    pw.stop()


@pytest.fixture(scope="session")
def browser(playwright):
    """Launch Chromium browser (visible)"""
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #browser =playwright.firefox.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()

"""
@pytest.fixture(scope="function")
def page(browser):
    #Create a new page for each test
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
"""

@pytest.fixture(scope="function")
def page(browser):

    context = browser.new_context(
        storage_state=None,  # no saved storage
        java_script_enabled=True,
        viewport={"width": 1500, "height": 800}
    )

    context.clear_cookies()
    context.clear_permissions()

    page = context.new_page()

    yield page

    context.close()