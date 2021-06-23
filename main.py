import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter.font import Font

main = Tk()
main.config(background='#4d4949')
main.title('Grade Calculator')

#Fonts
bigFont = Font(
    family="Microsoft YaHei",
    size=24
)

# --- VARS ---
GradeBox1 = tkinter.DoubleVar()
GradeBox2 = tkinter.DoubleVar()
GradeBox3 = tkinter.DoubleVar()

# --- FUNCTIONS ---

def delete():
    label.destroy()
    label.destroy()

def program():
    try:
        global label
        label = Label(main, text=round(((GradeBox3.get() - (GradeBox1.get() * (1 - GradeBox2.get()))) / GradeBox2.get())))
        label.pack(fill=BOTH, expand=TRUE, side=TOP)
        label.config(background='#4d4949', fg='white', font=bigFont)
        clear_text()
    except Exception as exception:
        global error
        tkinter.messagebox.showerror('Oops!', "ERROR")


def clear_text():
    Box1.delete(0, 'end')
    Box2.delete(0, 'end')
    Box3.delete(0, 'end')


# --- MAIN ---


frame = Frame(main)
frame.pack(fill=BOTH, expand=FALSE, side=BOTTOM)
frame.config(background='#4d4949')

#Current grade
Currentlabel = Label(main, text="Current Grade")
Currentlabel.pack(fill=BOTH, expand=TRUE, side=TOP)
Currentlabel.config(background='#4d4949', fg='white', font=bigFont)

#Box1
Box1 = Entry(main, textvariable=GradeBox1, justify=CENTER)
Box1.pack(fill=BOTH, expand=TRUE, side=TOP, padx=200, pady=10)
Box1.config()

#Gradeweight
Weightlabel = Label(main, text='Weight of exam (ex: .30)')
Weightlabel.pack(fill=BOTH, expand=TRUE, side=TOP)
Weightlabel.config(background='#4d4949', fg='white', font=bigFont)

#Box2
Box2 = Entry(main, textvariable=GradeBox2, justify=CENTER)
Box2.pack(fill=BOTH, expand=TRUE, side=TOP, padx=200, pady=10)
Box2.config()

#Desired garde label
Desiredlabel = Label(main, text='Desired grade')
Desiredlabel.pack(fill=BOTH, expand=TRUE, side=TOP)
Desiredlabel.config(background='#4d4949', fg='white', font=bigFont)

#Box3
Box3 = Entry(main, textvariable=GradeBox3, justify=CENTER)
Box3.pack(fill=BOTH, expand=TRUE, side=TOP, padx=200, pady=10)
Box3.config()

#Button
mybutton = Button(main, text='Get your grade!', command=program)
mybutton.pack(side=TOP, pady=10)
mybutton.config(background='#191a19', fg='white', font=bigFont, bd=0)

delete_button = Button(main, text='Clear', command=delete)
delete_button.pack(side=BOTTOM)
delete_button.config(background='#191a19', fg='white', font=bigFont, bd=0)




main.mainloop()
