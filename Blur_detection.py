
# import the necessary packages
from imutils import paths
import argparse
import cv2
	# method
#imagePath = r
image = cv2.imread(r"C:\Users\CHETAN\Desktop\blurimage.jpg")
#image = cv2.imread(r"C:\Users\CHETAN\Desktop\Gull_portrait_ca_usa.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = cv2.Laplacian(gray, cv2.CV_64F).var()
text = "Not Blurry"
# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
threshold = 50
if fm < threshold:
    text = "Blurry"
# show the image
cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("Image", image)
key = cv2.waitKey(0)




