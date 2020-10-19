from PIL import Image
from PIL import ImageFilter

baby = Image.open('cute-baby.jpg')

blur = baby.filter(ImageFilter.BLUR)


baby.show()
blur.show()