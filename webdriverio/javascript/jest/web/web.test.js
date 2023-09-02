test("go to dogutech.io", async () => {
  await driver.url("https://dogutech.io");
}, 10_000);

test("search for dogu", async () => {
  this.doguElements = await driver.$$('xpath://*[contains(text(), "dogu")]');
});

test("check for dogu", async () => {
  expect(this.doguElements.length).toBeGreaterThan(0);
});
