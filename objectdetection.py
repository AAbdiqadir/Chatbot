# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:45:33 2023

@author: Ahmed Abdiqadir
"""

import tensorflow as tf


import matplotlib.pyplot as plt

import cv2
import imghdr
import os

import tensorflow_hub as hub
import pandas as pd

# Loading model directly from TensorFlow Hub

detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

class detectmodel:
 
    
 
    index = 0
    # default constructor
    def __init__(self , x):
        self.x = x
 

    def func(self):
        
        width = 800
        height = 800
        #detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")
        #Load image by Opencv2
        try:
            img = cv2.imread(self.x)
            if img is None:
                raise Exception(f"{self.x} is not a valid image file.")
        
            else:
                inp = cv2.resize(img, (width , height ))

#Convert img to RGB
                rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
                # COnverting to uint8
                rgb_tensor = tf.convert_to_tensor(img, dtype=tf.uint8)
        
                #Add dims to rgb_tensor
                rgb_tensor = tf.expand_dims(rgb_tensor , 0)
        
                
                #print(labels)
                # Loading csv with labels of classes
                label =["-","person","bicycle", "car" ,"motorcycle",  "airplane" ,"bus","train",
                "truck","boat","traffic light","fire hydrant","-","stop sign","parking meter","bench","bird","cat","dog",
                "horse","sheep","cow","elephant","bear","zebra","giraffe","-","backpack","umbrella","-","-","handbag",
                "tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard",
                "tennis racket","bottle","-","wine glass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli",
                "carrot","hot dog","pizza","donut","cake","chair","couch","potted plant","bed","-","dining table","-","-",
                "toilet","-","tv","laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink","refrigerator",
                "-","book","clock","vase","scissors","teddy bear","hair drier","toothbrush","hair brush"]
        
                boxes, scores, classes, num_detections = detector(rgb_tensor)
        
                pred_labels = classes.numpy().astype('int')[0] 
                pred_labels = [label[i] for i in pred_labels]
                pred_boxes = boxes.numpy()[0].astype('int')
                pred_scores = scores.numpy()[0]
                # Putting the boxes and labels on the image
                for score, (ymin,xmin,ymax,xmax), label in zip(pred_scores, pred_boxes, pred_labels):
                    if score < 0.5:
                        continue
        
                    score_txt = f'{100 * round(score)}%'
                    img_boxes = cv2.rectangle(rgb,(xmin, ymax),(xmax, ymin),(0,255,0),2)      
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img_boxes, label,(xmin, ymax-10), font, 1.5, (255,0,0), 2, cv2.LINE_AA)
                    cv2.putText(img_boxes,score_txt,(xmax, ymax-10), font, 1.5, (255,0,0), 2, cv2.LINE_AA)
        
                plt.imshow(img_boxes)
                plt.show()
        except Exception as e:
            print("Error:", e)
        
