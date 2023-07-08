/** @type {import('@jest/types').Config.InitialOptions} */
module.exports = {
  testEnvironment: '@dogu-tech/jest-environment',
  globalSetup: './jest.global-setup.js',
  globalTeardown: './jest.global-teardown.js',
  bail: true
};
