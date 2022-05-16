import os
from PIL import Image

# get image
filepath = os.path.join('Walk', 'Vener_walk_up1.png')
img = Image.open(filepath)

# get width and height
width = img.width
height = img.height
print(width, height)
# image = PIL.Image.open(os.path.join('Walk', 'Vener_walk_up1.png'))
# width, height = image.size.extract() #width and height from output tuple.
# print(width, height)



# im = cv2.imread('data/src/lena.jpg')

# print(type(im))
# # <class 'numpy.ndarray'>

# print(im.shape)
# print(type(im.shape))
# # (225, 400, 3)
# # <class 'tuple'>