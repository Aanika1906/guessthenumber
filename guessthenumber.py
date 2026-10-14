from tkinter import *
window=Tk()#creates window
window.geometry("500x500")#the measureemnts of the window
window.title("guessing number game ! ")
window.config(background="purple")

heading=Label(window,text="guess the number :)",font=("Arial",20),background="purple",foreground="black")
heading.place(x=120,y=40)
name=Label(window,text="NAME:",font=("Arial",17),background="purple",foreground="black")
name.place(x=100,y=120)
nameentry=Entry(window,foreground="black")
nameentry.place(x=180,y=125)
ok_button=Button(window,text="OK",command=None)
ok_button.place(x=310,y=125)

guess=Label(window,text="guess a number from 1-20",font=("Arial",17),background="purple",foreground="black")
guess.place(x=100,y=150)
guessentry=Entry(window,foreground="black")
guessentry.place(x=200,y=150)
submit_button=Button(window,text="OK",command=None)
submit_button.place(x=310,y=150)



window.mainloop()