# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:46:30 2023

@author: Ahmed Abdiqadir
"""

#######################################################
from nltk.sem import Expression
from nltk.inference import ResolutionProver
from gingerit.gingerit import GingerIt
from nltk.tokenize import word_tokenize

import cv2
import imghdr
import os
import model

import matplotlib.pyplot as plt


from tkinter import *     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
read_expr = Expression.fromstring



import matplotlib.image as img
#######################################################
#  Initialise Knowledgebase. 
#######################################################
import pandas
import cameravid
import random
import objectdetection as od
kb=[]
data = pandas.read_csv('chatbot/kb (2).csv', header=None)
[kb.append(read_expr(row.lower())) for row in data[0]]

list1 = ["panda","elephant","cat","tiger","koalas","chameleon","anaconda","turtles","lizard",
"bullet ant","crickets","sloth","cockroaches","goat","chicken","grizzly","the peregrine falcon",
"hippopotamus","cheetah",
"mosquito","arctic whale","giraffe","dog","kangaroo" , "shark","octopus"]

# >>> ADD SOME CODES here for checking KB integrity (no contradiction), 
# otherwise show an error message and terminate

##adding the csv file questions
import temp2 #import the similarity checker
quiz_ans = pandas.read_csv('chatbot/quiz.csv', header = None, encoding_errors= 'replace')
questions = []
answers = []
animals= []
ans_wers = []
for i in quiz_ans[1]:
    answers.append(i)
for i in quiz_ans[0]:
    questions.append(i)
#######################################################
#  Initialise AIML agent
#######################################################
import aiml
# Create a Kernel object. No string encoding (all I/O is unicode)
kern = aiml.Kernel()
kern.setTextEncoding(None)
kern.bootstrap(learnFiles="chatbot/mybot-logic.xml")

#######################################################
# Welcome user
#######################################################
print("Welcome to this chat bot. Please feel free to ask questions from me!")

#######################################################
# Main loop
#######################################################
while True:
    #get user input
    try:
        userInput = input("> ")
    except (KeyboardInterrupt, EOFError) as e:
        print("Bye!")
        break
    #pre-process user input and determine response agent (if needed)
    responseAgent = 'aiml'
    #activate selected response agent
    if responseAgent == 'aiml':
        answer ="The input should contain alphabets"
        for i in userInput:
            if i.isalpha():
                answer = kern.respond(userInput)
                break
                #print("The input contains only expresions")
        #print(answer[0])
    #post-process the answer for commands
    if answer[0] == '#':
        params = answer[1:].split('$')
        cmd = int(params[0])
        if cmd == 0:
            print(params[1])
            break
       
        
        # Here are the processing of the new logical component:
            
        elif cmd == 29:
            def result():

                if((ans_wers[0]=="yes")and(ans_wers[1]=="yes")and(ans_wers[2]=="yes")and(ans_wers[3]=="yes")
                   and(ans_wers[4]=="no")):#1 
                 print("The animal you are thinking of might be a lion")
                
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="yes")and(ans_wers[2]=="yes")and(ans_wers[3]=="yes")
                   and(ans_wers[4]=="yes")):#1 
                
                 ans = ["Cheetah, Hyena"]
                 print("The animal you are thinking of might be a " , random.choice(ans))
                 
                elif((ans_wers[0]=="no")and(ans_wers[1]=="yes")and(ans_wers[2]=="yes")and(ans_wers[3]=="yes")
                   and(ans_wers[4]=="yes")):#1 
                 print("The animal you are thinking of might be a Leaopard")
                 
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="no")and(ans_wers[2]=="yes")and(ans_wers[3]=="yes")
                   and(ans_wers[4]=="yes")):#1 
                 ans = ["Girapphe, Antelope"]
                 print("The animal you are thinking of might be ",random.choice(ans))
                 
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="yes")and(ans_wers[2]=="no")and(ans_wers[3]=="no")
                   and(ans_wers[4]=="no")):#1 
                 ans = ["Crocodile, Aligator"]
                 print("The animal you are thinking of might be ",random.choice(ans))
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="yes")and(ans_wers[2]=="yes")and(ans_wers[3]=="no")
                   and(ans_wers[4]=="no")):#1 
                 ans = ["Killer whale, Sharks"]
                 print("The animal you are thinking of might be a ",random.choice(ans))
                
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="no")and(ans_wers[2]=="yes")and(ans_wers[3]=="yes")
                   and(ans_wers[4]=="no")):#1 
                 ans = ["Elephant, Buffalo", "Zebra"]
                 print("The animal you are thinking of might be ",random.choice(ans))
                 
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="no")and(ans_wers[2]=="yes")and(ans_wers[3]=="no")
                   and(ans_wers[4]=="no")):#1 
                 print("The animal you are thinking of might be a hippopotamus")
                
                elif((ans_wers[0]=="no")and(ans_wers[1]=="yes")and(ans_wers[2]=="no")and(ans_wers[3]=="no")
                   and(ans_wers[4]=="yes")):#1 
                 print("The animal you are thinking of might be a Snake")
                 
                elif((ans_wers[0]=="no")and(ans_wers[1]=="no")and(ans_wers[2]=="no")and(ans_wers[3]=="no")
                    and(ans_wers[4]=="no")):#1 
                  print("The animal you are thinking of might be a Frog")
                
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="no")and(ans_wers[2]=="yes")and(ans_wers[3]=="no")
                    and(ans_wers[4]=="yes")):#1 
                  print("The animal you are thinking of might be a Manatee")
                  
                elif((ans_wers[0]=="yes")and(ans_wers[1]=="yes")and(ans_wers[2]=="no")and(ans_wers[3]=="no")
                    and(ans_wers[4]=="no")):#1 
                  print("The animal you are thinking of might be a turtles")
                elif((ans_wers[0]=="no")and(ans_wers[1]=="no")and(ans_wers[2]=="no")and(ans_wers[3]=="no")
                    and(ans_wers[4]=="no")):#1 
                  print("The animal you are thinking of might be a jellyfish")
                elif((ans_wers[0]=="no")and(ans_wers[1]=="yes")and(ans_wers[2]=="yes")and(ans_wers[3]=="no")
                    and(ans_wers[4]=="no")):#1 
                  print("The animal you are thinking of might be a seal")
                else:
                    print("I cant think of an animal with this characteristics")
                  
               
                  
            def fun(): 
                
             try:
                 ans_wers.append(str(input("Do they live in groups(yes/no): ").lower())) 
                 ans_wers.append(str(input("Is it a carnivore(yes/no): ").lower())) 
                 ans_wers.append(str(input("Is it a mammal: ").lower())) 
                 ans_wers.append(str(input("Does it live on land(yes/no):: ").lower()))
                 ans_wers.append(str(input("Does it have spots: ").lower()))
             except (KeyboardInterrupt, EOFError) as e:
                print("Try again!")                  
             #print(ans_wers) 
             index = 0
             for i in ans_wers:
                 if i == "yes" or i == "no":
                    index= index +1
                    
                 else:
                     print("Wrong inputs TRY AGAIN!")
                     break
                 
             if index == (len(ans_wers)):
                 result()
                 ans_wers.clear()
             else:
                 ans_wers.clear()
                 fun()
            fun() 
        elif cmd == 31: # if input pattern is "I know that * is *"
            arguments =[]
            for argument in kb:
                constants = str(argument)
                if constants[0] =='(':
                    arguments.append(constants)
                
            consts =[]
            for row in arguments:
                x = word_tokenize(row)
                #print(x)
                for word in x:
                    if len(word) >1:   
                        consts.append(word.lower())    
            const =[]
            #x = word_tokenize(arguments[0])
            #print(x)
            for row in arguments:
                x = word_tokenize(row)
                #print(x)
                sentences = []
                for word in x:
                   if len(word) >1:  
                      sentences.append(word)
                   
                
                const.append(sentences)
            #print(const)  
            commands = []
            for arg in kb:
                constants = str(arg)
                if constants[0] =='(':
                    continue
                commands.append(constants)

            
            #print(params)
            object,subject=params[1].split(' is ')
            #print(object)
            expr =""
            present = []
            lenghtobj = word_tokenize(object)
            if len(subject) >1 and len(lenghtobj) ==1 :
                 expr=read_expr(subject.lower() + '(' + object.lower() + ')')
                 question = word_tokenize(str(expr))
                #print(xv)
                 for i in commands:
                    x = word_tokenize(i)
                    if x[2] == question[2] and question[0] in consts:
                        for a in const:
                            if x[0] == a[0]:
                                present.append(x[0])
                                print("I already know that " +question[2] +" is " + question[0])
                               # print("present")
                               # print("I know that ken is british")
                                break
                            elif x[0] == a[1]:
                                
                                present.append(x[0])
                                print("I already know that " +question[2] +" is " + question[0])
                                break
                            
                              #  print(x[0]+ xv[2])
                              
                            
                                
                            
                                
                    
                   
                 if  len(present) == 0 and question[0] in consts :
                     
                        kb.append(expr)
                        print("OK, I will remember that " +question[2] +" is " + question[0])
                        
                 elif len(present) == 0 and question[0] not in consts :
                    print("The format is not correct")
                    
            else:
                print("The format is not correct")
        elif cmd == 32: # if the input pattern is "check that * is *"
          
              arguments =[]
              for argument in kb:
                  constants = str(argument)
                  if constants[0] =='(':
                      arguments.append(constants)
                  
              consts =[]
              for row in arguments:
                  x = word_tokenize(row)
                  #print(x)
                  for word in x:
                      if len(word) >1:   
                          consts.append(word.lower())    
              const =[]
              #x = word_tokenize(arguments[0])
              #print(x)
              for row in arguments:
                  x = word_tokenize(row)
                  #print(x)
                  sentences = []
                  for word in x:
                     if len(word) >1:  
                        sentences.append(word)
                     
                  
                  const.append(sentences)
              #print(const)  
              commands = []
              for arg in kb:
                  constants = str(arg)
                  if constants[0] =='(':
                      continue
                  commands.append(constants)

              
              #print(params)
              object,subject=params[1].split(' is ')
              #print(object)
              expr =""
              present = []
              expr =""
              lenghtobj = word_tokenize(object)
              if len(subject) >1 and len(lenghtobj) ==1 :
                       expr=read_expr(subject.lower() + '(' + object.lower() + ')')
                       question = word_tokenize(str(expr))
                       if question[0] in consts:
                           answer=ResolutionProver().prove(expr, kb, verbose=False)   
                           if answer:
                               print("Correct")
                               
                           else:
                               print("incorrect")
                       else:
                           print("The query is not in line with the KB")
                      
                                  
                                      
                          
                       
                          
              else:
                      print("The format is not correct")
               

               # >> This is not an ideal answer.
               # >> ADD SOME CODES HERE to find if expr is false, then give a
          
             # definite response: either "Incorrect" or "Sorry I don't know." 
        elif cmd == 30:
            arguments =[]
            for argument in kb:
                constants = str(argument)
                if constants[0] =='(':
                    arguments.append(constants)
                
            consts =[]
            for row in arguments:
                x = word_tokenize(row)
                #print(x)
                for word in x:
                    if len(word) >1:   
                        consts.append(word.lower())    
            const =[]
            #x = word_tokenize(arguments[0])

            for row in arguments:
                x = word_tokenize(row)
                #print(x)
                sentences = []
                for word in x:
                   if len(word) >1:  
                      sentences.append(word)
                   
                
                const.append(sentences)
            #print(const)  
            commands = []
            for arg in kb:
                constants = str(arg)
                if constants[0] =='(':
                    continue
                commands.append(constants)

            #print(xv)
            for i in commands:
               x = word_tokenize(i)
               #if x[2] == question[2] and question[0] in consts:
               for a in const:
                   if x[0] == a[0]:
                       print("I know that "+x[2]+ " is " +x[0])
                       
                      #present.append(x[0])
                       #print("I already know that " +question[2] +" is " + question[0])
                      # print("present")
                      # print("I know that ken is british")
                       break
                   elif x[0] == a[1]:
                       print("I know that "+x[2]+ " is " +x[0])
                       #present.append(x[0])
                       #print("I already know that " +question[2] +" is " + question[0])
                       break
        elif cmd == 33:
        
            print("Yes!")
            print("Open the new window that pops up on your tool bar and click start video ")
            cameravid.revealface()
            
        elif cmd == 34:
            
            try:
                Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
                filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
                #print(filename)
        
                variab = filename  
                
               
                model_ = od.detectmodel(variab)
                model_.func()
                
                
            except (KeyboardInterrupt, EOFError) as e:
                print("No input file recognized !")
            
            
            
        elif cmd == 35:
            try:
                Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
                filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#                print(filename)
                try:
                    img = cv2.imread(filename)
                    if img is not None: 
                        variab = filename  
                        model_ = model.model(variab)
                        model_.func()
                        
                    else:
                        raise Exception(f"{filename} is not a valid image file.")
                        
                except Exception as e:
                    print(f"{filename} is not a valid image file.")    
                
                ##imagepath = input("input the image path> ")
            except (KeyboardInterrupt, EOFError) as e:
                print("No input file recognized!")
                
            
            
           
        elif cmd== 36:
           

            data_dir = "animals"

            img_extens= ['jpeg','jpg','png','bmp']

            database = os.listdir(data_dir)
            #print(database)
            ##
            if len(animals)==1:
            
             for i in database:
                animal,img_exten=i.split('.')
                if animal == animals[0]:
                    
                    testImage = img.imread("animals/"+i)
                    plt.imshow(testImage)
                    plt.show()
            else:
                print("Sorry there is no relevant topic to display")
               
                    
        elif cmd == 99:
            correct = GingerIt().parse(userInput)
            if len(answer) > 10:
                #correct = GingerIt().parse(example)
                temp2.similarity,data = temp2.tfidfcosine_similarity(correct["result"], questions)

                answer_ind = temp2.closest_match(data, temp2.similarity, len(data))
                if answer_ind[2] != 0:
                    
                    #print(answer_ind)
                    print(answers[answer_ind[1]-1])
                    
                    if answers[answer_ind[1]-1].lower() in list1:
                        animals.clear()
                        animals.append(answers[answer_ind[1]-1].lower())
                    else:
                        input_items = word_tokenize(answer_ind[0])
                        
                        for i in input_items:
                            if i.lower() in list1:
                                animals.clear()
                                animals.append(i)
                    #print(userInput)
                else:
                    print("I did not get that, please try again.")
            
            else:
             print("I did not get that, please try again.")
    else:
        input_items = word_tokenize(userInput)
        output_items = word_tokenize(answer)
        print(answer)
        for i in input_items:
            if i.lower() in list1:
                animals.clear()
                animals.append(i.lower())
                break
               
        for i in output_items:
            if i.lower() in list1:
                animals.clear()
                animals.append(i.lower())
                break
        
        