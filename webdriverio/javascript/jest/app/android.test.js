test("find wikipedia", async () => {
  this.searchSelector = await driver.$("~Search Wikipedia");
  await this.searchSelector.waitForDisplayed({ timeout: 30000 });
});

test("click wikipedia", async () => {
  await this.searchSelector.click();
});

test("find insert text", async () => {
  this.insertTextSelector = await driver.$(
    'android=new UiSelector().resourceId("org.wikipedia.alpha:id/search_src_text")'
  );
  await this.insertTextSelector.waitForDisplayed({ timeout: 30000 });
});

test('add value "Wikipedia"', async () => {
  await this.insertTextSelector.addValue("Wikipedia");
  await driver.pause(5000);
}, 10 * 1000);

test('expect to find "Wikipedia"', async () => {
  const allProductsName = await driver.$$(`android.widget.TextView`);
  expect(allProductsName.length).toBeGreaterThan(0);
});
