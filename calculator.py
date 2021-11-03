import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Caluladora')
root.geometry("300x140")
root.maxsize(width=300,height=140)
root.configure(bg='Black')
exp= " "

###
def press(num):
    global exp 
    exp += str(num)
    equation.set(exp)
def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = " "
    except:
        equation.set('erro')
        exp = " "
def clear ():
    global exp
    exp = " "
    equation.set(" ")


equation = tk.StringVar()
dis_entry = ttk.Entry(root,width=10,state = 'readonly',background='red',textvariable = equation)
dis_entry.grid(row = 0, column = 0 , columnspan= 4,ipadx =120, ipady= 10)
dis_entry.focus()

#Botoes
num1 = ttk.Button(root,text= 1,width= 12, command= lambda:press(1))
num2 = ttk.Button(root,text= 2,width= 12, command= lambda:press(2))
num3 = ttk.Button(root,text= 3,width= 12, command= lambda:press(3))
num4 = ttk.Button(root,text= 4,width= 12, command= lambda:press(4))
num5 = ttk.Button(root,text= 5,width= 12, command= lambda:press(5))
num6 = ttk.Button(root,text= 6,width= 12, command= lambda:press(6))
num7 = ttk.Button(root,text= 7,width= 12, command= lambda:press(7))
num8 = ttk.Button(root,text=8,width= 12, command= lambda:press(8))
num9 = ttk.Button(root,text= 9,width= 12, command= lambda:press(9))
num0 = ttk.Button(root,text= 0,width= 12, command= lambda:press(0))
menos = ttk.Button(root,text='-',width =8,command= lambda: press('-'))
mais= ttk.Button(root,text='+',width =8,  command= lambda: press('+'))
multi= ttk.Button(root,text='x',width =8,  command= lambda: press('x'))
dividir= ttk.Button(root,text='÷',width =8,  command= lambda: press('/'))
cl= ttk.Button(root,text='cl',width =12,  command= lambda: clear())
igual= ttk.Button(root,text='=',width =12,  command= lambda: equalpress())



num1.grid(row=1, column = 0 )
num2.grid(row=1, column = 1 )
num3.grid(row=1, column = 2 )

num4.grid(row=2, column = 0 )
num5.grid(row=2, column = 1 )
num6.grid(row=2, column = 2)

num7.grid(row=3, column = 0 )
num8.grid(row=3, column = 1 )
num9.grid(row=3, column = 2 )

num0.grid(row=4, column = 0 )
cl.grid(row=4, column = 1)
igual.grid(row=4, column = 2 )


multi.grid(row = 3, column = 3)
menos.grid(row = 1, column = 3)
mais.grid(row = 2, column = 3)
dividir.grid(row = 4, column = 3)
root.mainloop()
