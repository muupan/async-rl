try:
   import cv2
   imresize = cv2.resize
except:
   import scipy.misc
   imresize = scipy.misc.imresize
