import cv2

cap = cv2.VideoCapture(0)
counter = 0

while True:

	ret, frame = cap.read()

	cv2.imshow('frame',frame)

	if not ret:
		break
	
	k = cv2.waitKey(1)

	if k%256 == 27:
		#escape key
		break

	elif k%256 == 32:
		#space
		image_name = "test{}.png".format(counter)
		cv2.imwrite(image_name,frame)
		print('{} writtern'.format(image_name))
		counter+=1

cap.release()
cv2.destroyAllWindows()
	