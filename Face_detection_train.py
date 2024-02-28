import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import Image

haarcasecade_path="haarcascade_frontalface_default.xml"
trainimagelabel_path="Trainner.yml"
trainimage_path="dataset\\"


def getImagesAndLables(path):
    # imagePath = [os.path.join(path, f) for d in os.listdir(path) for f in d]
    newdir = [os.path.join(path, d) for d in os.listdir(path)]
    imagePath = [
        os.path.join(newdir[i], f)
        for i in range(len(newdir))
        for f in os.listdir(newdir[i])
    ]
    faces = []
    Ids = []
    print(imagePath)
    
    for imagePath in imagePath:
        pilImage = Image.open(imagePath).convert("L")
        imageNp = np.array(pilImage, "uint8")
        Id = int(imagePath.split("\\")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids
# Train Image
def TrainImage():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Id = getImagesAndLables(trainimage_path)
    recognizer.train(faces, np.array(Id))
    recognizer.save(trainimagelabel_path)
    res = "Image Trained successfully"  # +",".join(str(f) for f in Id)
#     message.configure(text=res)
#     text_to_speech(res)