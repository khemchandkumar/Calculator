from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())

            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
            
    elif text=="C":
        scvalue.set("")
        screen.update()
    elif text=="DEL":
        current=scvalue.get()
        scvalue.set(current[:-1])
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("500x500")
root.title("Calculator")
root.wm_iconbitmap("1.ico")
root.configure(background="#333333")

# Create a screen for the calculator
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="Lucida 40 bold")
screen.pack(fill=X, ipadx=20, pady=20, padx=10)

#create frame to add buttons
f = Frame(root, bg="#333333")
b = Button(f, text="C",font="Lucida 20 bold",padx=25,pady=10, bg="powder blue",fg="red")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="=",font="Lucida 20 bold",padx=25,pady=10, bg="powder blue",fg="red")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="DEL", font="Lucida 20 bold", padx=25, pady=10, bg="powder blue")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="00", font="Lucida 20 bold", padx=25, pady=10, bg="powder blue")
b.pack(side=LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="#333333")
b = Button(f, text="+",font="Lucida 20 bold",padx=21,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="-",font="Lucida 20 bold",padx=23,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="*",font="Lucida 20 bold",padx=23,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="/",font="Lucida 20 bold",padx=23,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text=".",font="Lucida 20 bold",padx=21,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="#333333")
b = Button(f, text="9",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="8",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="7",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="6",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="5",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="#333333")
b = Button(f, text="4",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="3",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="2",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text="1",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
b = Button(f, text= "0",font="Lucida 20 bold",padx=20,pady=10, bg="powder blue")
b.pack(side=LEFT,padx=10, pady=10)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()