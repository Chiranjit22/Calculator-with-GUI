from tkinter import *
root = Tk()
root.geometry("360x500")
root.title("Calculator by Chiranjit Roy")
root.config(background="#333333")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text == "⌫":
        current = scvalue.get()
        scvalue.set(current[:-1])
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font = "lucida 40 bold")
screen.pack(fill = X, ipadx = 4, padx = 5, pady = 5)


f0 = Frame(root, bg = "grey")
b = Button(f0, text ="+",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f0, text ="-",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f0, text ="C",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f0, text ="⌫",padx = 9, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
f0.pack()


f1 = Frame(root, bg = "grey")
b = Button(f1, text ="9",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f1, text ="8",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f1, text ="7",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f1, text ="*",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
f1.pack(padx = 9,pady = (6,0))


f2 = Frame(root, bg = "grey")
b = Button(f2, text ="6",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f2, text ="5",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f2, text ="4",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f2, text ="/",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
f2.pack(padx = 9,pady = (6,0))


f3 = Frame(root, bg = "grey")
b = Button(f3, text ="3",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f3, text ="2",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f3, text ="1",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f3, text =".",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
f3.pack(padx = 9, pady = (6,0))


f4 = Frame(root, bg = "grey")
b = Button(f4, text ="0",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f4, text ="00",padx = 18, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
b = Button(f4, text ="=",padx = 52, pady = 11, font = "lucida 17 bold")
b.pack(side = LEFT, padx = 9, pady = 6)
b.bind("<Button-1>", click)
f4.pack(padx = 9, pady = (6,0))



root.mainloop()