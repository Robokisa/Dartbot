import cv2
import numpy as np

def img_crop(img_in)
	img = cv2.imread(img_in)
	crop_img = img[y:y+h, x:x+w]
	cv2.imshow("cropped", crop_img)
	return crop_img

def pos_det(img_in)
	img = cv2.imread(img_in)
	# Set our filtering parameters 
	# Initialize parameter settiing using cv2.SimpleBlobDetector 
	params = cv2.SimpleBlobDetector_Params() 

	# Set filtering parameters 
	params1.filterByArea = True
	params1.minArea = 100
	params1.filterByCircularity = True 
	params1.minCircularity = 0.9
	params1.filterByConvexity = True
	params1.minConvexity = 0.2
	params1.filterByInertia = True
	params1.minInertiaRatio = 0.0001
	detector1 = cv2.SimpleBlobDetector_create(params) 
		  
	params2 = cv2.SimpleBlobDetector_Params() 
	
	# Set filtering parameters 
	params2.filterByArea = True
	params2.minArea = 100
	params2.filterByCircularity = True 
	params2.minCircularity = 0.9
	params2.filterByConvexity = True
	params2.minConvexity = 0.2
	params2.filterByInertia = True
	params2.minInertiaRatio = 0.001
	detector2 = cv2.SimpleBlobDetector_create(params) 
	
	# Detect blobs
	det_1 = detector1.detect(img) 
	det_2 = detector2.detect(img)
	
	while len(det_1) > 0 and len(det_2) == 0:
		# Moving Function Here
	
	if len(det_2) > 0:
		return
				
	# Draw blobs on our image as red circles 
	blank = np.zeros((1, 1))  
	blobs1 = cv2.drawKeypoints(image, det_1, (0, 0, 255), 2)
	blobs2 = cv2.drawKeypoints(image, det_2, (0, 0, 255), 2)
	cv2.imshow("Test window 1", blobs1)
	cv2.imshow("Test window 2", blobs2)
	
def dist_det(x, y, PA):
	# Add This to Main Code setServoAngle() Function:
	# if servo == 2:
	# 	# Get Servo Position
	# 	self._check_range(us, us_min, us_max)
	# 	servo_range = us_max - us_min
	# 	angle = (float(us - us_min) / float(servo_range)) * 130.0		
	# 	PA = int(round(angle, 0)) - 65

	while PA > 0:
		# Rotate Bot
		
	while PA < 0:
		# Rotate Bot

	while x < 138 and y < 97:
		# Move Back
		
	while x > 145 and y > 105:
		# Move Forward
