const purgecss = require("@fullhuman/postcss-purgecss");

module.exports = {
  plugins: [
    require("tailwindcss")("tailwind.config.js"),
    require("tailwindcss")("tailwind.js"),
    require("autoprefixer")(),
    process.env.NODE_ENV === "production" &&
      purgecss({
        content: [
          "./src/**/*.vue",
          "./src/**/*.css",
          "./public/index.html",
          "./@(public|src)/**/*.@(${extensionsUsingCSS.join('|')})",
          "./node_modules/vue-spinner/src/**/*.vue"
        ],
        defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
      })
  ]
};
