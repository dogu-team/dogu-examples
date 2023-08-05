from typing import Any, Dict

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ChromeOptions, Remote
from pytest_dogu_sdk.dogu_config import DoguConfig
from pytest_dogu_sdk.dogu_hooks import DoguClient


pytest_plugins = ["pytest_dogu_sdk"]


def pytest_dogu_create_client() -> DoguClient:
    class SeleniumDoguClient(DoguClient):
        def on_setup(self, dogu_config: DoguConfig):
            options = ChromeOptions()
            options.set_capability(
                "dogu:options",
                {
                    "organizationId": dogu_config.organization_id,
                    "projectId": dogu_config.project_id,
                    "token": dogu_config.token,
                    "runsOn": dogu_config.runs_on,
                    "browserName": dogu_config.browser_name,
                    "browserVersion": dogu_config.browser_version,
                },
            )
            return Remote(
                command_executor=f"{dogu_config.api_base_url}/remote/wd/hub",
                options=options,
            )

        @property
        def dogu_results(self) -> Dict[str, Any]:
            return self.cast(WebDriver).capabilities["dogu:results"]

        def on_teardown(self):
            if self.impl:
                self.cast(WebDriver).quit()

    return SeleniumDoguClient()
