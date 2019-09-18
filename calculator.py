from tkinter import *

calc = Tk()
calc.geometry("360x500")
calc.title("Calculator")
calcLabel = Label(calc, text="Calculator", bg="light gray", font=("Corsica", 30, "bold"))
calc.config(background="dark grey")

eq = StringVar()
expression = ""


def numClick(num):
    global expression
    expression = expression + str(num)
    eq.set(expression)


def op():
    global expression
    add = str(eval(expression))
    eq.set(add)
    expression = ""


def op():
    global expression
    sub = str(eval(expression))
    eq.set(sub)
    expression = ""


def op():
    global expression
    mul = str(eval(expression))
    eq.set(mul)
    expression = ""


def op():
    global expression
    divide = str(eval(expression))
    eq.set(divide)
    expression = ""


def clear():
    eq.set("")


myCalc = Entry(calc, font=("Courier New", 12, 'bold'), textvar=eq, width=25, bd=5, bg='sky blue')
myCalc.pack()

but1 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(1), text="1",
              font=("Courier New", 16, 'bold'))
but1.place(x=10, y=100)

but2 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(2), text="2",
              font=("Courier New", 16, 'bold'))
but2.place(x=10, y=170)

but3 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(3), text="3",
              font=("Courier New", 16, 'bold'))
but3.place(x=10, y=240)

but4 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(4), text="4",
              font=("Courier New", 16, 'bold'))
but4.place(x=75, y=100)

but5 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=75, y=170)

but6 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(6), text="6",
              font=("Courier New", 16, 'bold'))
but6.place(x=75, y=240)

but7 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=140, y=100)

but8 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(8), text="8",
              font=("Courier New", 16, 'bold'))
but8.place(x=140, y=170)

but9 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(9), text="9",
              font=("Courier New", 16, 'bold'))
but9.place(x=140, y=240)

but0 = Button(calc, padx=14, pady=14, bd=4, bg='gray', command=lambda: numClick(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=10, y=310)

butdot = Button(calc, padx=47, pady=14, bd=4, bg='gray', command=lambda: numClick("."), text=".",
                font=("Courier New", 16, 'bold'))
butdot.place(x=75, y=310)

butpl = Button(calc, padx=14, pady=14, bd=4, bg='gray', text="+", command=lambda: numClick("+"),
               font=("Courier New", 16, 'bold'))
butpl.place(x=205, y=100)

butsub = Button(calc, padx=14, pady=14, bd=4, bg='gray', text="-", command=lambda: numClick("-"),
                font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=170)

butMl = Button(calc, padx=14, pady=14, bd=4, bg='gray', text="*", command=lambda: numClick("*"),
               font=("Courier New", 16, 'bold'))
butMl.place(x=205, y=240)

butDiv = Button(calc, padx=14, pady=14, bd=4, bg='gray', text="/", command=lambda: numClick("/"),
                font=("Courier New", 16, 'bold'))
butDiv.place(x=205, y=310)

butClear = Button(calc, padx=14, pady=119, bd=4, bg='gray', text="CE", command=clear,
                  font=("Courier New", 16, 'bold'))
butClear.place(x=270, y=100)

butEqual = Button(calc, padx=151, pady=14, bd=4, bg='gray', command=op, text="=", font=("Courier New", 16, 'bold'))
butEqual.place(x=10, y=380)
calc.mainloop()
