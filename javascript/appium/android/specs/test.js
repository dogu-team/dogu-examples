import assert from 'assert';
import { remote } from 'webdriverio'


const browser = await remote({
  hostname: 'api.dogutech.io',
  port: 80,
  path: '/wd/hub',
  capabilities: {
    platformName: "android",
    'appium:automationName': "uiautomator2",
    "dogu:options": {
        accessKey: "",
        organizationId: "",
        projectId: "",
        tag: "android",
        appVersion: "2.5.194-alpha-2017-05-30",
    },
  }
})

var searchSelector = await browser.$(`~Search Wikipedia`);
await searchSelector.waitForDisplayed({ timeout: 30000 });
await searchSelector.click();

var insertTextSelector = await browser.$('android=new UiSelector().resourceId("org.wikipedia.alpha:id/search_src_text")');
await insertTextSelector.waitForDisplayed({ timeout: 30000 });

await insertTextSelector.addValue("Wikipedia");
await browser.pause(5000);

var allProductsName = await browser.$$(`android.widget.TextView`);
assert(allProductsName.length > 0);

await browser.deleteSession();
