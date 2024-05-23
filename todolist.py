import tkinter
from tkinter import *
root=Tk()
root.title("to-do-list")
root.geometry("400x650+400+100")
root.resizable(False,False)
task_list=[]
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task != '\n':
               task_list.append(task)
               listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
Image_icon=PhotoImage(file="c:\\Users\\USER\\Desktop\\Image\\Image/task.png")
root.iconphoto(False,Image_icon)
heading=Label(root,text="ALL TASK",font="arial 10 bold",fg="white",bg="black")
heading.place(x=130,y=20)
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=50)
task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=5,y=4)
button=Button(frame,text="Add",font="arial 20 bold",width=6,bg="black",fg="white",bd=0,command=addTask)
button.place(x=300,y=0)
frame1=Frame(root,bd=3,width=500,height=280,bg="black")
frame1.pack(pady=(100,0))
listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg="green",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
openTaskFile()
Delete_icon=PhotoImage(file="c:\\Users\\USER\\Desktop\\Image\\Image/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=10)


root.mainloop()