# There are a number of options for doing this:
# 1. opencv
# 2. PIL resize
# 3. scipy interpn
# 4. scipy.misc.imresize ( bad option as this in turn calls PIL )
#
# Does anyone know which is the fastest?

try:
   import cv2
   imresize = cv2.resize
except:
   import numpy as np
   import PIL.Image

   def tmp(img,size):
        return np.array(PIL.Image.fromarray(img).resize(size,PIL.Image.BILINEAR))

   imresize = tmp
