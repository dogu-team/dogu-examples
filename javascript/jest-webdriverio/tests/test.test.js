const { remote } = require('webdriverio');

beforeAll(async () => {
  this.driver = await remote({
    capabilities: {
      browserName: 'chrome'
    }
  })
});

afterAll(async () => {
  await this.driver?.deleteSession();
});

test('test', async () => {
  await this.driver.url('https://dogutech.io');
});
