import cv2

gray = cv2.imread("meme.png", cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", thresh)
cv2.waitKey(3000)
cv2.destroyAllWindows()