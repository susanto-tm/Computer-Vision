import tensorflow as tf
from tensorflow import keras
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import serial

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('img', img)
    cv.imshow('gray', gray)

    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
