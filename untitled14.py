from tkinter import*
from PIL import ImageTk , Image
root= Tk()

root.title("Pokemon Card Game")
root.geometry("600x500")
root.configure(background="red")

pikachu= ImageTk.PhotoImage(Image.open("pikachu.jpg"))
lucario= ImageTk.PhotoImage(Image.open("lucario.jpg"))
darkrai= ImageTk.PhotoImage(Image.open("darkrai.png"))
mewtwo= ImageTk.PhotoImage(Image.open("mewtwo.png"))
persion= ImageTk.PhotoImage(Image.open("persion.jpg"))
jigglypuff= ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
nidoking= ImageTk.PhotoImage(Image.open("nidoking.jpg"))
zoroark= ImageTk.PhotoImage(Image.open("zoroark.jpeg"))
inceneroar= ImageTk.PhotoImage(Image.open("inceneroar.jpg"))
ivysour= ImageTk.PhotoImage(Image.open("Ivysour.jpg"))

button= ImageTk.PhotoImage(Image.open("button.jpg"))

player1= Label(root,text= "Player 1", bg="red", fg="blue")
player1.place(relx= 0.1, rely= 0.5, anchor= CENTER)

player2= Label(root,text= "Player 2", bg="blue", fg="red")
player2.place(relx= 0.9, rely= 0.5, anchor= CENTER)

player1_score= Label(root, bg= "green", fg= "yellow")
player1_score.place(relx= 0.1, rely= 0.3, anchor= CENTER)

player2_score= Label(root, bg= "green", fg= "yellow")
player2_score.place(relx= 0.9, rely= 0.4, anchor= CENTER)

random_card_label= Label(root, bg= "blue", fg= "white")
random_card_label.place(relx= 0.5, rely= 0.5, anchor= CENTER)

root.mainloop()