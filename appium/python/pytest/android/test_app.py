import time

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_dogu_sdk.common import DoguClient


def test_click_wikipedia(dogu_client: DoguClient):
    search_element = WebDriverWait(dogu_client.cast(WebDriver), 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
    search_element.click()


def test_send_keys(dogu_client: DoguClient):
    search_input = WebDriverWait(dogu_client.cast(WebDriver), 30).until(EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")))
    search_input.send_keys("Wikipedia")


def test_search_results(dogu_client: DoguClient):
    time.sleep(5)
    search_results = dogu_client.cast(WebDriver).find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert len(search_results) > 0
