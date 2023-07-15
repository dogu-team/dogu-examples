module.exports = async (globalConfig, projectConfig) => {
  await globalThis.driver?.deleteSession();
};
