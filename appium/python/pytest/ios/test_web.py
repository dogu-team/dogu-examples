from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from pytest_dogu_sdk.common import DoguClient


def test_go_to_dogutech_io(dogu_client: DoguClient):
    dogu_client.cast(WebDriver).get("https://dogutech.io/")


def test_search_for_dogu(dogu_client: DoguClient):
    global dogu_elements
    dogu_elements = dogu_client.cast(WebDriver).find_elements(AppiumBy.XPATH, '//*[contains(text(), "dogu")]')


def test_check_for_dogu():
    assert len(dogu_elements) > 0
