from tkinter import *

root = Tk()
root.title("PyCalculator")
# title() function defines the text of the window

e = Entry(root, width=23, borderwidth=5, font=("Helvetica", 25))
# borderwidth defines the visual effect of the border
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
# columnspan defines the number of columns the button will span to

def button_click(number):
    current = e.get()
    # saves the entry state at the moment
    e.delete(0, END)
    # deletes what was entered in the Entry field
    e.insert(0, str(current) + str(number))
    # put the numbers together as they are clicked (previous + new one)
    # needs to be converted to string to insert in the field

def button_clear():
    e.delete(0, END)
# deletes from the first position "0" to the last "END"

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

# define buttons

button_1 = Button(root, text="1", padx=50, pady=20, command=lambda: button_click(1)) # gets the number as integer
button_2 = Button(root, text="2", padx=50, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=50, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=50, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=50, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=50, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=50, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=50, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=50, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=50, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=50, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=109, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=97, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=51, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=53, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=51, pady=20, command=button_divide)
# we have to use lambda to use functions with arguments

# put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
# the columnspan argument sets the elements to be uniform
# columnspan=2 occupies 2 columns

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()