import cv2
import numpy as np
import argparse
import datetime

parser = argparse.ArgumentParser(description='Webcam timelapse utility\n Esc to exit')
parser.add_argument('-o','--output', help='Output filename', required=False,default='output.avi')
parser.add_argument('-w','--webcam', help='Webcam id 0-100', required=False,default=0)
parser.add_argument('-i','--interval', help='Interval (seconds) between frames', required=False,default=1)
parser.add_argument('-f','--fps', help='Frames per second to use in output file', required=False,default=60.0)
parser.add_argument('-p','--preview', help='Show preview (toggle with ''p'')', action='store_true', required=False,default=False)
parser.add_argument('-t','--timestamp', action='store_true',help='Timestamp output file', default=False)
args = parser.parse_args()


if args.timestamp:
	file_name=datetime.datetime.now().strftime("%d%B%Y%I%M%p-")+args.output
else:
	file_name=args.output
print "Saving to ",file_name

preview_enabled=args.preview
cv2.namedWindow("timelapse (saving)")
cv2.resizeWindow("timelapse (saving)",200,100)

cap = cv2.VideoCapture(int(args.webcam))
#define codec to save video (fourcc format)
fourcc= cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
w=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH ))
h=int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT ))
out = cv2.VideoWriter(file_name,fourcc, args.fps, (w,h))



while cap.isOpened():
	ret,frame=cap.read()
	if ret==True:
		out.write(frame)
	else:
		break

	if args.preview and preview_enabled:
		cv2.imshow('timelapse (saving)',frame)

	key_code=cv2.waitKey(int(args.interval)*1000)	
	if key_code==27 or key_code==ord('q'):#esc
		break
	if key_code==ord('p'):
		if not args.preview:
			args.preview=True
		preview_enabled=not preview_enabled
		print "Image preview is set to ", preview_enabled," \n(Still saving)"
	
print "Closing"
cap.release()
out.release()
cv2.destroyAllWindows()