from tkinter import *
from googletrans import Translator


def tran():
    text = t.get('1.0', END)
    a = translator.translate(text, dest='en')
    t1.delete('1.0', END)
    t1.insert('1.0', a.text)



root = Tk()
root.geometry('573x450')
root.title('Переводчик')
root.resizable(width=False, height=False)
root['bg'] = '#00008B'
translator = Translator()


icon = PhotoImage(file="2.png")


label = Label(root, fg='white', bg='#00008B', font='Arial 15 bold', text='Переводчик')
label.place(relx=0.5, y=30, anchor=CENTER)

t = Text(root, width=20, height=19, font='Arial 12 bold')
t.place(x=30, y=50,)

btn = Button(root, width=64, height=64, image=icon, bg="#00008B", command=tran, relief=FLAT)
btn.place(y=190, x=250)

t1 = Text(root, width=20, height=19, font='Arial 12 bold')
t1.place(y=50, x=360)

root.mainloop()

