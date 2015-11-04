import cv2
import numpy as np



cap = cv2.VideoCapture(0)


#define codec to save video (fourcc format)
fps=60.0
fourcc= cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
out = cv2.VideoWriter('output.avi',fourcc, fps, (w,h))



while cap.isOpened():
	ret,frame=cap.read()
	if ret==True:

		out.write(frame)
		print "save"
		cv2.imshow('frame',frame)
	else:
		break
	if cv2.waitKey(1000) == 27:#esc
		break

print "releasing"
cap.release()
out.release()
cv2.destroyAllWindows()