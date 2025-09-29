from playwright.sync_api import Playwright
from API_Automation.utils import config

def create_request_context(playwright: Playwright):
    """Reusable API request context"""
    return playwright.request.new_context(
        base_url=config.BASE_URL,
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config.TOKEN}"
        }
    )
