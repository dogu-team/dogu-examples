const { remote } = require('webdriverio');

module.exports = async (globalConfig, projectConfig) => {
  if (globalThis.driver) {
    throw new Error('globalThis.driver already exists');
  }

  globalThis.driver = await remote({
    capabilities: {
      browserName: 'chrome'
    }
  })
};
