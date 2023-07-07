from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options().load_capabilities(
    {
        # Specify dogu:options for testing
        "platformName": "android",
        "dogu:options": {
            "userName": "",
            "accessKey": "",
            "organizationId": "",
            "projectId": "",
            "tag": "android",
            "appVersion": "2.5.194-alpha-2017-05-30",
        },
    }
)

# Initialize the remote Webdriver using Dogu remote URL
# and options defined above
driver = webdriver.Remote("http://localhost:4000/wd/hub", options=options)

search_element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
search_element.click()
search_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")))
search_input.send_keys("Wikipedia")
time.sleep(5)
search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert len(search_results) > 0

driver.quit()
