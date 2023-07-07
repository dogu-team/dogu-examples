exports.config = {
  updateJob: false,
  specs: [
    './specs/test.js'
  ],
  exclude: [],
  hostname: 'localhost',
  port: 4000,
  path: '/wd/hub',

  capabilities: [{
    platformName: "android",
    'appium:automationName': "uiautomator2",
    'dogu:options': {
      accessKey: "",
      organizationId: "",
      projectId: "",
      tag: "android",
      appVersion: "2.5.194-alpha-2017-05-30",
    }
  }],

  logLevel: 'info',
  coloredLogs: true,
  screenshotPath: './errorShots/',
  baseUrl: '',
  waitforTimeout: 10000,
  connectionRetryTimeout: 90000,
  connectionRetryCount: 3,

  framework: 'mocha',
  mochaOpts: {
    ui: 'bdd',
    timeout: 20000
  }
};
