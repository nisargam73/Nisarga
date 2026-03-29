import cv2
img=cv2.imread(r"C:\Users\91701\Pictures\Screenshots\Screenshot (217).png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("Blurred Image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
