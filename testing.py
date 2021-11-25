import numpy as np
import cv2

def Blur_detection(image):
    cap = cv2.VideoCapture(image if image else 0)

    # Define the codec and create VideoWriter object
    while True:
        ret, frame = cap.read()
        
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #print("frame" , frame)
        fr = cv2.Laplacian(frame, cv2.CV_64F).var()
        print(fr)
        if fr < 50:
            text = "Blurry"
            print(text)
        else:
            text = "Not Blurry"
            print(text)
    # show the image
        aa = cv2.putText(fr, "{}: {:.2f}".format(text, fr), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        #print(aa)
        #cv2.imshow("Image", fr)
        # write the flipped fr
        cv2.imshow('fr',fr)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()


image = r"C:\Users\CHETAN\Desktop\newdentvideo.mp4"
Blur_detection(image)