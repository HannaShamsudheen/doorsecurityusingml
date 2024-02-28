import cv2
import os
from collections import Counter

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
path="dataset\\"

recognizer = cv2.face.LBPHFaceRecognizer_create()
font = cv2.FONT_HERSHEY_SIMPLEX
def detection():
    li=[]
    recognizer.read("Trainner.yml")
    video_capture = cv2.VideoCapture(0)
    count=0

    while True:

        result, video_frame = video_capture.read()  # read frames from the video
        if result is False:
            break  # terminate the loop if the frame is not read successfully

    #     faces = detect_bounding_box(video_frame,name)  # apply the function we created to the video frame
        gray_image = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
        for (x, y, w, h) in faces:
                 Id, conf = recognizer.predict(gray_image[y : y + h, x : x + w])
                 if conf < 70:
                     count+=1
                     li.append(Id)
                     cv2.rectangle(video_frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
                     cv2.putText(
                            video_frame, str(Id), (x + h, y),font, 1, (255, 255, 0,), 4)
                 else:
                        Id = "Unknown"
                        tt = str(Id)
                        cv2.rectangle(video_frame, (x, y), (x + w, y + h), (0, 25, 255), 7)
                        cv2.putText(
                            video_frame, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                        )
    #                  cv2.imwrite(path+name+"\\"+str(count)+".jpg",face)
        cv2.imshow("My Face Detection Project", video_frame)
        if count==20:
            break# display the processed frame in a window named "My Face Detection Project"

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    counter = Counter(li)
    return counter.most_common(1)[0][0]