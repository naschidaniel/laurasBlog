const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "/static/"
      : "http://localhost:8080/",
  outputDir: "./dist/",

  chainWebpack: (config) => {
    config.optimization.splitChunks(false);

    config.optimization.minimize(
      process.env.NODE_ENV === "production" ? true : false
    );

    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "webpack-stats.json" }]);

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://0.0.0.0:8080")
      .host("0.0.0.0")
      .port(8080)
      .hot(true)
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  },
};
