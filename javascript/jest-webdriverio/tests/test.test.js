const driver = globalThis.driver;

describe('test dogu', () => {
  test('go to dogutech.io', async () => {
    await driver.url('https://dogutech.io');
  });

  test('find dogu image on header', async () => {
    this.dogu = await driver.$('//header//img[@alt="Dogu"]');
  });

  test('check dogu image src', async () => {
    const src = await this.dogu.getAttribute('src');
    expect(src).toBe("/resources/icons/logo-horizontal.svg");
  });
});
