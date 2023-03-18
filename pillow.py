from PIL import Image

im_file  = "data/page00.png"

im = Image.open(im_file)
print (im.size)
im.show()