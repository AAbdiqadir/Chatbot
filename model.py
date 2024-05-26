# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:47:31 2023

@author: Ahmed Abdiqadir
"""

import tensorflow as tf

import matplotlib.pyplot as plt
from tensorflow import keras

import cv2
import imghdr
import os

class model:
 
    
 
    index = 0
    # default constructor
    def __init__(self , x):
        self.x = x
 
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
 
 
    def func(self):
    
        modelmine = keras.models.load_model("mycnnmodel.h5")
        
        
        
        try:
            
            img = keras.preprocessing.image.load_img(
                self.x, target_size=(360,360)
            )
            
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)  # Create batch axis
            
            predictions = modelmine.predict(img_array)
           # print(predictions)
            score = (predictions[0])
            scors = max(score)
            index = 0;
            
            for i in score:
                if i != scors:
                    index = index+1;
                  
                else:
                    break;
        

            class_names=['Elephant', 'Lion', 'zebra']
            
            print("The image is likely to be a", class_names[index])
            plt.figure(figsize=(10, 10))
        
            ax = plt.subplot(3, 3,  5)
           
            plt.imshow(img)
            
            plt.title(class_names[index])
            plt.show()
            
        except (FileNotFoundError, EOFError) as e:
                 print("No such file or directory: ", self.x)
        

    #obj.func2()
