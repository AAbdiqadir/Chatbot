
"""
Created on Sun Mar 12 16:49:16 2023

@author: Ahmed Abdiqadir
"""
import cv2
from tkinter import *
from PIL import Image, ImageTk

cam_on = False
cap = None

def revealface():
        
        try: 
            mainWindow = Tk()
            mainFrame = Frame(mainWindow, height = 640, width = 810)
            mainFrame.place(x=350,y=0)
            
            cameraFrame = Frame(mainWindow, height = 640, width = 405)
            cameraFrame.place(x = 0, y = 0)
            
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   
            
            
            def show_frame():
            
                if cam_on:
                    
                    ret, frame = cap.read()    
            
                    if ret:
                        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
                        
                        # Apply face detection
                   
                        faces = face_cascade.detectMultiScale(cv2image, 1.1, 4)
                        # Draw the rectangle around each face
                        for (x, y, w, h) in faces:
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                            
                        #cv2.imshow('img', frame)
                        img = Image.fromarray( cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   ).resize((810,640))
                        
                        imgtk = ImageTk.PhotoImage(image=img)        
                        vid_lbl.imgtk = imgtk    
                        vid_lbl.configure(image=imgtk)    
                    
                    vid_lbl.after(10, show_frame)
            
            def start_vid():
                global cam_on, cap,st
                st = ""
                
                cam_on = True
                cap = cv2.VideoCapture(0) 
                show_frame()
            
            def stop_vid():
                global cam_on
                cam_on = False
                
                if cap:
                    cap.release()
            
            vid_lbl = Label(mainFrame)
            vid_lbl.grid(row=0, column=0)
            
            def close_app():
                global cam_on, cap
                stop_vid()
                mainWindow.destroy()
                cap.release()
            
            #Button
            ExitButton = Button(cameraFrame, text="Exit", bg = "red", command=close_app)
            ExitButton.place(x = 300, y = 00)
            
            #Buttons
            TurnCameraOn = Button(cameraFrame, text="start webcam", bg = "blue", command=start_vid)
            TurnCameraOn.place(x = 0, y = 0)
            TurnCameraOff = Button(cameraFrame, text="stop webcam", bg = "blue", command=stop_vid)
            TurnCameraOff.place(x = 0, y = 600)
           # 
        
            
            mainWindow.mainloop()
        except (KeyboardInterrupt, EOFError) as e:
            
         mainWindow.destroy()
            
         print("Bye!")
        
                
    
    
            
              
revealface()               
               
        

         
            
        
        #mainWindow.quit()
        
            
