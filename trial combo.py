from guizero import App, Text, PushButton, Combo, Waffle, TextBox, Picture
from random import randint
import random
import time

#  random word generation

#def initialise (word):
    
wordList = ["raspberry", "picademy", "codeclub", "coderdojo",
           "educator", "debugging", "process", "belfast", "boston",
          "foundation"]
x = randint(0,9)
#print (x)
word = wordList[x]
#letters_list = list(word)
score = 0

#functions

def scramble():
    x = randint(0,9)
    #print (x)
    #word = wordList[x]
    letters_list = list(word)
    #print("o")
    #button.bg = "green"
    random.shuffle(letters_list)
    text.value = letters_list
    return

def compare():
    if combo.value == word:
        text = Text(app, text="correct", size=50, color="green",grid=[1,0])
        score = text2.value
        text =Text(app,text = "score is ", grid=[5, 0])
        text =Text(app,text = score)
    else:
        text = Text(app, text="wrong", size=50, color="red",grid=[1,3])

def counter():
    text2.value = int(text2.value) + 1
    


#main body   
app = App(title = "countdown conundrum",width=300,height=600)
text = Text(app,grid =[50,50])
waffle = Waffle(app, color = "blue", align = "bottom",
                command=scramble, height=5,pad=1,width=5
                ,grid=[10,10])
waffle.bg = "green"

waffle.set_pixel(2, 2, "red")
#button = PushButton(app, command=scramble, text="Start")
combo = Combo(app, options=[" ","raspberry", "picademy", "codeclub", "coderdojo",
           "educator", "debugging", "process", "belfast", "boston",
          "foundation"],command=compare,grid=[15,20])
text2 = Text(app, text="1", grid=[25,0])
text2.repeat(1000, counter)  # Schedule call to counter() every 1000ms
my_cat = Picture(app, image="download.jfif",grid = [5,5])
app.display()

# score



#print(word)

