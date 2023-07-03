from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
from PIL import Image, ImageTk
import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')



def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses =0
    
    the_word=random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
	global numberOfGuesses
	if numberOfGuesses<11:	
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					messagebox.showinfo("Hangman","You guessed it!")
                    

		else:
			numberOfGuesses += 1
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses==11:
					messagebox.showwarning("Hangman","Game Over")





if __name__ == '__main__':
   
	
    root = ctk.CTk()
    root.title('Hangman')
    root.resizable(0,0)
   

    word_list= ['MOMENTUM','STROM','BOOLEAN','HYDROGEN','AMRABAT','CHANNEL','CREATE','STUART','JUNE','JUPITAR','PRAYER','ATOMIC','RIGID',
            'LUCKNOW','LIVELY','GUAGUALADA','ANAMBRA','ARCANE','PHEONIX','PANTA','TRINIDAD','AGRA','GRAB','MEMORIAL','RATTLE','VERNICE','SINGARPOR',
            'RAIPUR','ZAMBIA','PARTY']

    photos = [PhotoImage(file="hang0.png"), PhotoImage(file="hang1.png"), PhotoImage(file="hang2.png"),
	PhotoImage(file="hang3.png"), PhotoImage(file="hang4.png"), PhotoImage(file="hang5.png"),
	PhotoImage(file="hang6.png"), PhotoImage(file="hang7.png"), PhotoImage(file="hang8.png"),
	PhotoImage(file="hang9.png"), PhotoImage(file="hang10.png"), PhotoImage(file="hang11.png")]

    
    frame2 = ctk.CTkFrame(root)
    frame2.grid(row = 0, column = 0)
    imgLabel=Label(frame2)
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

    
    lblWord = StringVar()
    Label(frame2, textvariable  =lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)




    frame3 = ctk.CTkFrame(root)
    frame3.grid(row = 1 , column = 0)

    n=0
    for c in ascii_uppercase:
        
        first_butt=ctk.CTkButton(master=frame3, text=c ,command=lambda c=c: guess(c), font=('Helvetica', 18),fg_color="black", border_spacing=10,border_width=2,bg_color="blue", width=40, height=40).grid(row=1+n//9,column=n%9)
        n+=1

    second_butt=ctk.CTkButton(master=frame3, text="Restart", command=lambda:newGame(),  width=40, height=40,font=("Helvetica" ,10, "bold")).grid(row=3, column=8)






    
    newGame()
    root.mainloop()    
