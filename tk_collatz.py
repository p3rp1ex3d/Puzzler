from tkinter import *
from tkinter import messagebox
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

yellow="#fcf4e3"

root=Tk()
root.title('Collatz Plotting')
root.configure(bg=yellow)
at=open("collatz rules.txt").read()

l=[]
def collatz(n):
    l.clear()
    i = 0
    old_n = n
    while n!=1:
        l.append(n)
        if n%2 == 0: 
            n = n//2
        else:
            n = 3*n+1
        i += 1
        old_n = n
    l.append(1)

def main(event):
    if (inp_ut.get().isnumeric()==False or eval(inp_ut.get())<2) or type(eval(inp_ut.get()))!=int:
        messagebox.showerror(title='Error',message='Please enter only integers greater than 1 in the box')
    
    n=eval(inp_ut.get())
    if n>1 and type(n)==int:
        collatz(n)

        output1.delete('1.0',END)
        output1.insert(END,l)
        output2.config(text='')
        output2.config(text='ITERATIONS : '+str(len(l)-1))

        f = Figure(figsize = (5,2), dpi = 100)                  
        a = f.add_subplot(1,1,1)
        a.plot(l,marker='.',color='g',markersize=3)
        canvas = FigureCanvasTkAgg(f, root)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 6, column = 0)         
        canvas._tkcanvas.grid(row = 6, column = 0,padx=40)

def about():
    about=messagebox.showinfo('About',at)


lbl1 = Label(root, width = 30,pady=10, text = "Type in a number & press Enter",font=("Arial",15),bg=yellow)
lbl1.grid(row = 7, column = 0, )
lbl2 = Label(root, width = 30, height=2, text = "THE COLLATZ CONJECTURE",font=("STENCIL",20),bg=yellow)
lbl2.grid(row = 0, column = 0)



k=Button(root,text ="About", bd=7, command = about,bg='#e6eaf0')
k.grid(row=1,column=0)
k.pack

inp_ut = Entry(root, width = 20, bg = "#e6eaf0",bd=5)
inp_ut.grid(row = 8, column=0)
inp_ut.get()
inp_ut.bind("<Return>", main)


output1 = Text(root, width = 70, height = 6, bg ="#e6eaf0") 
output1.grid(row = 11, column = 0)
output1.pack
output2 = Label(root, width = 70,height = 1, bg = "#a3e5ff",font=("Ariel",10))
output2.grid(row = 10, column = 0,pady=10)
output2.pack

root.mainloop()
