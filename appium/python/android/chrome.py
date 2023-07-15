from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# if called from Dogu Routine, the following environment variables will be injected from Dogu Routine.
# if you want to run this script locally, please set your access key here.
token = os.environ.get("DOGU_TOKEN", "INSERT_YOUR_TOKEN")
organization_id = os.environ.get("DOGU_ORGANIZATION_ID", "INSERT_YOUR_ORGANIZATION_ID")
project_id = os.environ.get("DOGU_PROJECT_ID", "INSERT_YOUR_PROJECT_ID")
api_base_url = os.environ.get("DOGU_API_BASE_URL", "https://api.dogutech.io")

options = AppiumOptions().load_capabilities(
    {
        # Specify dogu:options for testing
        "dogu:options": {
            "accessKey": token,
            "organizationId": organization_id,
            "projectId": project_id,
            "runs-on": "android",  # or "ios"
            "browserName": "chrome",  # or "safari" on ios
        },
    }
)


driver = None
try:
    driver = webdriver.Remote(f"{api_base_url}/remote/wd/hub", options=options)
    driver.get("https://dogutech.io")
    driver.find_element(AppiumBy.XPATH, '//*[contains(text(), "dogu")]')
finally:
    if driver:
        driver.quit()
