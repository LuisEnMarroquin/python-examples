from PIL import Image

filename = r'src/favicon.png'
img = Image.open(filename)
img.save('src/favicon.ico')
