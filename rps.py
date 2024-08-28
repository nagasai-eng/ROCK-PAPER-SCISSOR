import tkinter as tk
from tkinter import messagebox
import random
def play(user_chioce):
    choice=['Rock','Paper','Scissor']
    computer_choice=random.choice(choice)
    if user_chioce==computer_choice:
       result="it is a tie!"
    elif (user_chioce=='Rock'and computer_choice=='Scissors')or\
          (user_chioce=='Paper'and computer_choice=='Rock')or \
          (user_chioce=='Scissors'and computer_choice=='paper'):
      result="you win!"
    else:
      result="computer wins!"
    messagebox.showinfo("Result",f"computer chosen:{computer_choice}\nyou chosen :{user_chioce}\n{result}")
  

root=tk.Tk()
root.title("Rock-paper-scissor")
rock_photo=tk.PhotoImage(file="rock.gif")
paper_photo=tk.PhotoImage(file="paper.gif")
scissors_photo=tk.PhotoImage(file="scissor2.gif")

def create_button(image,command,row,column):
  canvas=tk.Canvas(root,width=500,height=700)
  canvas.grid(row=row,column=column,padx=20,pady=20)
  canvas.create_image(200,200,image=image)
  canvas.bind("<Button-1",lambda event:command())

create_button(rock_photo,lambda:play('Rock'),0,0)
create_button(paper_photo,lambda:play('paper'),0,1)
create_button(scissors_photo,lambda:play('scissors'),0,2)
root.mainloop()
