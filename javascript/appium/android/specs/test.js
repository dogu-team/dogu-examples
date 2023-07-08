import assert from 'assert';
import { remote } from 'webdriverio'

// if called from Dogu Routine, the following environment variables will be injected from Dogu Routine.
// if you want to run this script locally, please set your access key here.
const accessKey = process.env.DOGU_ACCESS_KEY || 'INSERT_YOUR_ACCESS_KEY';
const organizationId = process.env.DOGU_ORGANIZATION_ID || 'INSERT_YOUR_ORGANIZATION_ID';
const projectId = process.env.DOGU_PROJECT_ID || 'INSERT_YOUR_PROJECT_ID';
const apiBaseUrl = process.env.DOGU_API_BASE_URL || 'https://api.dogutech.io';

const browser = await remote({
  baseUrl: apiBaseUrl,
  path: '/remote/wd/hub',
  capabilities: {
    platformName: "android",
    'appium:automationName': "uiautomator2",
    "dogu:options": {
        accessKey,
        organizationId,
        projectId,
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
