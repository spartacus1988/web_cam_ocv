


# """
# Simply display the contents of the webcam with optional mirroring using OpenCV 
# via the new Pythonic cv2 interface.  Press <esc> to quit.
# """


# import cv2


# def show_webcam(mirror=False):
# 	cam = cv2.VideoCapture(0)
# 	while True:
# 		ret_val, img = cam.read()
# 		if mirror: 
# 			img = cv2.flip(img, 1)
# 		cv2.imshow('my webcam', img)
# 		if cv2.waitKey(1) == 27: 
# 			break  # esc to quit
# 	cv2.destroyAllWindows()


# def main():
# 	show_webcam(mirror=True)


# if __name__ == '__main__':
# 	main()


import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    # Display the resulting frame
    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         eyes = eye_cascade.detectMultiScale(roi_gray)
         for (ex,ey,ew,eh) in eyes:
             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()