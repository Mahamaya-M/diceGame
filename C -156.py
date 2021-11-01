from tkinter import*
from PIL import ImageTk , Image
import random
    
root= Tk()
root.title("Endless dice game that will be ended")
root.geometry("400x400")
root.config(bg="yellow")


img1 =  ImageTk.PhotoImage(Image.open("one.png"))
img2 =  ImageTk.PhotoImage(Image.open("two.png"))
img3 =  ImageTk.PhotoImage(Image.open("three.png"))
img4 =  ImageTk.PhotoImage(Image.open("four.png"))
img5 =  ImageTk.PhotoImage(Image.open("five.png"))
img6 =  ImageTk.PhotoImage(Image.open("six.png"))

player1 = Label(root,text= "Player 1" , bg = "chocolate1" , fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor = CENTER)

player2 = Label(root,text= "Player 2" , bg = "chocolate1" , fg = "white")
player2.place(relx = 0.9, rely = 0.3 , anchor = CENTER)

player_1_score_label = Label(root, bg = "chocolate1" , fg = "white")
player_1_score_label.place(relx = 0.1, rely = 0.4 , anchor = CENTER)

player_2_score_label = Label(root , bg = "chocolate1" , fg = "white")
player_2_score_label.place(relx = 0.9, rely = 0.4 , anchor = CENTER)

random_dice_label = Label(root,bg= "firebrick" , fg = "white")
random_dice_label.place(relx = 0.5, rely = 0.5 , anchor = CENTER)

player1_score = 0
def player1():
     global player1_score
     random_no1 = random.randint(1,6)
     random_dice_label["text"] = "Player 1 dice Random number : " + str(random_no1)
     player1_score = player1_score + random_no1
     player_1_score_label["text"] = str(player1_score)
     if random_no1 == 1 :
         player_1_btn.config(image=img1)
     elif random_no1 == 2 :
         player_1_btn.config(image=img2)
     elif random_no1 == 3 :
         player_1_btn.config(image=img3)
     elif random_no1 == 4 :
         player_1_btn.config(image=img4)
     elif random_no1 == 5 :
         player_1_btn.config(image=img5)
     elif random_no1 == 6 :
         player_1_btn.config(image=img6)
     

     
player_1_btn = Button(root , image = img1 , command = player1)
player_1_btn.place(relx = 0.1, rely = 0.6 , anchor = CENTER)

player2_score = 0
def player2():
     global player2_score
     random_no2 = random.randint(1,6)
     random_dice_label["text"] = "Player 2 dice Random number : " + str(random_no2)
     player2_score = player2_score + random_no2
     player_2_score_label["text"] = str(player2_score)
     
     if random_no2 == 1 :
         player_2_btn.config(image=img1)
     elif random_no2 == 2 :
         player_2_btn.config(image=img2)
     elif random_no2 == 3 :
         player_2_btn.config(image=img3)
     elif random_no2 == 4 :
         player_2_btn.config(image=img4)
     elif random_no2 == 5 :
         player_2_btn.config(image=img5)
     elif random_no2 == 6 :
         player_2_btn.config(image=img6)
     
player_2_btn = Button(root , image = img1 , command = player2)
player_2_btn.place(relx = 0.9, rely = 0.6 , anchor = CENTER)

root.mainloop()
