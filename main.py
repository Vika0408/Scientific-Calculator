from tkinter import *
import math

#window creator
root = Tk()
root.title("Scientific Calculator")
root.config(bg="dodgerblue3")
root.resizable(width=False, height=False)
root.geometry("651x475+450+90")

#making entry field
entryfield = Entry(root,
                   font=('arial', 20, 'bold'),
                   bg='black',
                   fg='white',
                   width=25,
                   bd=10,
                   relief=SUNKEN)
entryfield.grid(row=0, column=0, columnspan=8)
entryfield.config(justify="right")

#logo image

#all butttons
button_text_list = [
  "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ", "1", "2", "3", "-", "2π",
  "cosh", "tanh", "sinh", "4", "5", "6", "*",
  chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9",
  chr(247), "ln", "deg", "rad", "e", "0", ".", "%", "=", "log₁₀", "(", ")",
  "x!"
]


#functioning of keys
def click(value):
  ex = entryfield.get()
  answer = ''
  try:
    if value == 'C':
      ex = entryfield.get()  #as a string
      ex = ex[0:len(ex) - 1]
      entryfield.delete(0, END)
      entryfield.insert(0, ex)
      return

    elif value == 'CE':
      entryfield.delete(0, END)
      return

    elif value == '√':
      answer = math.sqrt(eval(ex))

    elif value == 'π':
      answer = math.pi
      entryfield.insert(END, answer)
      return
    elif value == "cosθ":
      answer = math.cos(math.radians(eval(ex)))
    elif value == "sinθ":
      answer = math.sin(math.radians(eval(ex)))
    elif value == "tanθ":
      answer = math.tan(math.radians(eval(ex)))
    elif value == "cosh":
      answer = math.cosh(eval(ex))
    elif value == "sinh":
      answer = math.sinh(eval(ex))
    elif value == "tanh":
      answer = math.tanh(eval(ex))
    elif value == "2π":
      answer = 2 * math.pi
    elif value == chr(8731):
      answer = eval(ex)**(1 / 3)
    elif value == "x\u02b8":
      entryfield.insert(END, '**')
      return
    elif value == "x\u00B3":
      answer = eval(ex)**(3)
    elif value == "x\u00B2":
      answer = eval(ex)**(2)
    elif value == "ln":
      answer = math.log(eval(ex), 2.718281828459045)
    elif value == "log₁₀":
      answer = math.log10(eval(ex))
    elif value == "deg":
      answer = math.degrees(eval(ex))
    elif value == "rad":
      answer = math.radians(eval(ex))
    elif value == "x!":
      answer = math.factorial(eval(ex))
    elif value == 'e':
      answer = math.e
    elif value == '=':
      answer = eval(ex)
    elif value == chr(247):
      entryfield.insert(END, '/')
      return
    else:
      entryfield.insert(END, value)
      return
  except SyntaxError:
    pass
  entryfield.delete(0, END)
  entryfield.insert(0, answer)


button_list = []
j = 1
k = 0
for i in button_text_list:
  button = Button(root,
                  width=3,
                  height=2,
                  font=('arial', 18, 'bold'),
                  bg='black',
                  fg='white',
                  bd=2,
                  relief=SUNKEN,
                  activebackground='dodgerblue3',
                  text=i,
                  command=lambda button=i: click(button))
  button.grid(row=j, column=k, pady=1)
  button_list.append(button)
  k = k + 1
  if k > 7:
    j = j + 1
    k = 0
root.mainloop()