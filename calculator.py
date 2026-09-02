import tkinter

button_values = [
    ["A", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "x", "-", "+", "="]
top_symbols = ["A", "+/-", "%", "÷"]

row_count = len(button_values)
column_count = len(button_values[0])

color_dark_blue ="#17171C"
color_light_blue = "#2C2C35"
color_sky_blue = "#FFFFFF"
color_purple = "#4B5061"
color_white = "#FFFF26"
colour_black="#000000"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(True, True)
window.configure(background=colour_black,borderwidth=15,relief="sunken")


frame=tkinter.Frame(window)
label = tkinter.Label(frame, text="0", anchor="e", font=("Arial",45,"bold"), background=color_light_blue,
                      foreground=color_sky_blue,width=column_count,borderwidth=15,relief="sunken")
label.grid(row=0,column=0,columnspan=column_count,sticky="nsew",padx=3,pady=3)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button=tkinter.Button(frame, text=value, font=("arial",25),
                                width=column_count - 1, height=-1,
                                command=lambda value=value: button_clicked(value),)
        if value in top_symbols:
            button.configure(background=colour_black, foreground=color_sky_blue,borderwidth=12,relief="raised")
        elif value in right_symbols:
            button.configure(background=colour_black, foreground=color_sky_blue,borderwidth=12,relief="raised")
        else:
            button.configure(background=color_sky_blue, foreground=colour_black,borderwidth=12,relief="raised")
        button.grid(row=row +1, column=column)


frame.pack()
A="0"
operator=None
B=None

def clear_all():
    global A ,B,operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num%1==0:
         num=int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label,A,B,operator

    if value in right_symbols:
        if value=="=":
            if A is not None and operator is not None:
                B=label["text"]
                numA=float(A)
                numB=float(B)

                if operator=="+":
                    label["text"]=remove_zero_decimal(numA+numB)
                elif operator=="-":
                    label["text"]=remove_zero_decimal(numA-numB)
                elif operator=="x":
                    label["text"]=remove_zero_decimal(numA*numB)
                elif operator=="÷":
                    label["text"]=remove_zero_decimal(numA/numB)

                clear_all()
        elif value in "+-x÷":
            if operator is None:
                A=label["text"]
                label["text"]="0"
                B="0"

            operator=value
    elif value in top_symbols:
        if value=="A":
            clear_all()
            label["text"]="0"
        elif value=="+/-":
            result=float(label["text"])*-1
            label["text"]=remove_zero_decimal(result)
        elif value=="%":
            result=float(label["text"])/100
            label["text"]=remove_zero_decimal(result)
    else:
        if value==".":
            if value not in label["text"]:
                label["text"]+=value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"]=value
            else:
                label["text"]+=value
window.mainloop()

