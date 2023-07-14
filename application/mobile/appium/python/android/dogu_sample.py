from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# if called from Dogu Routine, the following environment variables will be injected from Dogu Routine.
# if you want to run this script locally, please set your access key here.
access_key = os.environ.get("DOGU_ACCESS_KEY", "INSERT_YOUR_ACCESS_KEY")
organization_id = os.environ.get("DOGU_ORGANIZATION_ID", "INSERT_YOUR_ORGANIZATION_ID")
project_id = os.environ.get("DOGU_PROJECT_ID", "INSERT_YOUR_PROJECT_ID")
api_base_url = os.environ.get("DOGU_API_BASE_URL", "https://api.dogutech.io")

options = UiAutomator2Options().load_capabilities(
    {
        # Specify dogu:options for testing
        "platformName": "android",
        "dogu:options": {
            "accessKey": access_key,
            "organizationId": organization_id,
            "projectId": project_id,
            "runs-on": "android",
            "appVersion": "2.5.194-alpha-2017-05-30",
        },
    }
)

# Initialize the remote Webdriver using Dogu remote URL
# and options defined above
driver = webdriver.Remote(f"{api_base_url}/remote/wd/hub", options=options)

search_element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
search_element.click()
search_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")))
search_input.send_keys("Wikipedia")
time.sleep(5)
search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert len(search_results) > 0

driver.quit()