import cv2
import time

cap = cv2.VideoCapture(0)
counter = 0
t=0
n = int(input('enter number of pictures you want to click: '))
delay = int(input('delay timer: '))
while (t!=n):

	ret, frame = cap.read()

	cv2.imshow('frame',frame)

	if not ret:
		break
	
	k = cv2.waitKey(1)

	if k%256 == 27:
		#escape key
		break

	image_name = "test{}.png".format(counter)
	cv2.imwrite(image_name,frame)
	print('{} written'.format(image_name))
	counter+=1
	t=t+1
	time.sleep(delay)

cap.release()
cv2.destroyAllWindows()
	