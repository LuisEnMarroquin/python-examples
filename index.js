const Jimp = require("jimp")

Jimp.read("favicon.png", function (error, image) {
  if (error) {
    console.log(error)
  } else {
    image.write("favicon.ico")
  }
})
