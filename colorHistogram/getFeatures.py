# import the necessary packages
import numpy as np
import cv2
import imutils	# make basic image processing functions such as translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV

bins = (8, 12, 3)

# Inside of our describe method we’ll convert from the RGB color space  to the HSV color space
def GetFeatures(image):
	# convert image into HSV from BGR
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	# get height and center of the image
	(h, w) = image.shape[:2]
	cX = int(w/2)
	cY = int(h/2)

	# divide the image into four rectangles/segments (top-left, top-right, bottom-right, bottom-left)
	segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),	(0, cX, cY, h)]

	# construct an elliptical mask representing the center of the image
	# make axes for the ellipse, that 75% full which id 75%//2 from the origin that is center of the image
	axesX = int(w*0.75)//2
	axesY = int(h*0.75)//2

	# make an elliptical mask with all zeros
	ellipticalMask = np.zeros(image.shape[:2], dtype="uint8")
	cv2.ellipse(ellipticalMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

	# feature list for the image
	features = []

	# loop over the segments which we created
	for (startX, endX, startY, endY) in segments:
		# construct a mask for each corner of the image, subtracting the elliptical center from it
		baseMask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.rectangle(baseMask, (startX, startY), (endX, endY), 255, -1)
		cornerMask = cv2.subtract(baseMask, ellipticalMask)

		# extract a color histogram from the image, then update the feature vector
		hist = histogram(image, cornerMask)
		features.extend(hist)

	# extract a color histogram from the elliptical region and update the feature vector
	hist = histogram(image, ellipticalMask)
	features.extend(hist)
	# return the feature vector
	return features

def histogram( image, mask):
	# extract a 3D color histogram from the masked region of the image, using the supplied number of bins per channel
	# parameters for calcHist are image, channel indexes, image mask, bin count, range
	hist = cv2.calcHist([image], [0, 1, 2], mask, bins, [0, 180, 0, 256, 0, 256])
	# normalize the histogram if we are using OpenCV 2.4
	if imutils.is_cv2():
		hist = cv2.normalize(hist).flatten()
	# otherwise handle for OpenCV 3+
	else:
		hist = cv2.normalize(hist, hist).flatten()
	# return the histogram
	return hist