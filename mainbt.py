import tkinter as tk
import ttkbootstrap as ttk


task_list = []

def addTask():
     task_entry = []
     task = task_entry.get()
     task_entry.delete(0, END)

     if task:
        with open('taskfile.txt', 'a') as taskfile:
               taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def openingFile():
    filename = open('taskfile.txt', 'r')
    
    for file1 in filename:
          listbox.insert(0, file1)
          print(file1)
    filename.close()
     
     


def opentasklist():

    try:
        filename = open('taskfile.txt', 'x')
        filename.close()

        openingFile()


    except:
        openingFile()

        


window = tk.Tk()

frame1 = tk.Frame(window)
frame2 = tk.Frame(window, width=50, height=500)



#frame one 1 content starts here
entry = ttk.Entry(frame1, width=60)
entry.grid(row=1, column=1)

button = ttk.Button(frame1,text="enter", bootstyle="info")
button.grid(row=1, column=2)
#frame one 1 content ends here



#frame two 2 content starts here
title_Text = ttk.Label(frame2,text="Todo List")
title_Text.pack()

listbox = tk.Listbox(frame2, font=('arial', 14), width=40, height=16,foreground="#333", selectbackground="#ddd")
listbox.pack()


opentasklist()


frame1.pack(padx=30, pady=30)
frame2.pack()

window.mainloop()