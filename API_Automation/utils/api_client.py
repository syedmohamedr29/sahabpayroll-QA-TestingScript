from playwright.sync_api import Playwright, APIRequestContext
import json

class BaseClient:
    def __init__(self, playwright: Playwright, base_url: str, token: str):
        # Make sure token is exactly how the API expects it
        self.request_context: APIRequestContext = playwright.request.new_context(
            base_url=base_url,
            extra_http_headers={
                "Accept": "text/plain",   # same as your working code
                "Content-Type": "application/json",
                "Authorization": token,   # use token as-is from .env
                "X-Requested-With": "XMLHttpRequest"
            }
        )

    def get(self, endpoint: str):
        return self.request_context.get(endpoint)

    def post(self, endpoint: str, payload: dict):
        return self.request_context.post(endpoint, data=json.dumps(payload))

    def dispose(self):
        self.request_context.dispose()
