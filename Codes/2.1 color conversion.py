import cv2          #importing the opencv library

img=cv2.imread('Samples 1/flower.jpg')

print(img.shape)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(gray.shape)

cv2.imshow('GRAY',gray)
