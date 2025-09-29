import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TENANT_NAME = os.getenv("TENANT_NAME")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TOKEN = os.getenv("TOKEN")
