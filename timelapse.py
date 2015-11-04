import cv2
import numpy as np



#params
output_file='output.avi'
fps=60.0
interval_seconds=1
show_img=True
img_enabled=True
if show_img:
	cv2.namedWindow("timelapse")


cap = cv2.VideoCapture(0)
#define codec to save video (fourcc format)
fourcc= cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
out = cv2.VideoWriter(output_file,fourcc, fps, (w,h))



while cap.isOpened():
	ret,frame=cap.read()
	if ret==True:
		out.write(frame)
	else:
		break

	if img_enabled:
		cv2.imshow('frame',frame)

	key_code=cv2.waitKey(interval_seconds*1000)	
	if key_code==27 :#esc
		break
	if key_code==ord('s'):
		img_enabled= not img_enabled
		print "Image preview", img_enabled

	
print "releasing"
cap.release()
out.release()
cv2.destroyAllWindows()