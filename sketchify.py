import cv2

filename = 'profile.jpg'
img = cv2.imread(filename)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
inverted_gray = cv2.bitwise_not(gray_img)
blurred = cv2.GaussianBlur(inverted_gray,(21,21),0)
inverted_blurred = cv2.bitwise_not(blurred)

pencil=cv2.divide(gray_img,inverted_blurred,scale=256.0)

cv2.imwrite('Capture_sketch.jpg',pencil)
