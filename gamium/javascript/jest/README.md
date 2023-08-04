# @dogu-examples/webdriverio-javascript-jest

# Requirements

- Node.js 16.0.0 or higher

# Installation

```sh
npm install
```

# Configuration

```json
// dogu.config.json
{
  // ...
  "apiBaseUrl": "INSERT_YOUR_API_BASE_URL",         // required
  "organizationId": "INSERT_YOUR_ORGANIZATION_ID",  // required
  "projectId": "INSERT_YOUR_PROJECT_ID",            // required
  "token": "INSERT_YOUR_TOKEN",                     // required
  "runsOn": "INSERT_YOUR_TAG",                      // required. example: "macos", "windows", "android", "ios"

  // turn on if you want to run web test
  "browserName": "chrome",                          // optional

  // turn on if you want to run app test
  "appVersion": "INSERT_YOUR_APP_VERSION",          // optional
}
```

# Run tests

```sh
# run web test ( dogu.config.json -> browserName is required )
npm run test:web

# run android app test ( dogu.config.json -> appVersion is required )
npm run test:app:android
```
