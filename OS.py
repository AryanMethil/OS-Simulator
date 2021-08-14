from tkinter import *
from tkinter.ttk import *
import shutil
import os
import subprocess
from functools import partial
from threading import *
import time
import string
from math import *

def io():
    def readthread():
        print("Reading!!")
        time.sleep(10)

    def writethread():
        print("Writing!!")
        time.sleep(15)
        del writethreads[-1]

    def func():
        if not writethreads:
            th = Thread(target=readthread)
            threads.append(th)
            threads[-1].start()
        else:
            print("Writing in progress")

    def func2():
        if threads and threads[-1].is_alive() == True:
            print("Reading in progress")
        elif writethreads:
            print("One process is already writing!!")
        else:
            th2 = Thread(target=writethread)
            writethreads.append(th2)
            th2.start()

    t = Tk()
    t.geometry("1200x1200")
    threads = []
    writethreads = []
    b1=Button(t, text="Read",command=func)
    b1.pack()

    b2=Button(t, text="Write",command=func2)
    b2.pack()
    t.mainloop()

def encrypt_decrypt():
    t2 = Tk()
    t2.geometry("1200x1200")
    path = 'D:\\Projects\\OS'
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))
    y_coord = 50
    r = []
    v9 = StringVar(t2)
    v9.set("test")
    for f in files:
        r.append(Radiobutton(t2, text=f, variable=v9, value=f))
        r[-1].place(x=100, y=y_coord)
        y_coord += 25

    def encrypt():
        fn=v9.get()
        with open(fn,'r+')as f:
            s=f.read()
            f.truncate(0)
        a=string.ascii_lowercase
        key="german"
        b=s
        print(f"Value of b is: {b}")
        c=b.replace(' ','')
        d={}
        for letter in key:
            d[letter]=a.index(letter)
        l3=list(d.values())
        l4=sorted(l3)
        cols=len(key)
        l=[]
        ind=0
        print(f"Value of ind is: {ind}")
        while ind<len(b):
            l2=[]
            while len(l2)<cols :
                try:
                    if b[ind] == ' ':
                        ind += 1
                        continue
                    l2.append(b[ind])
                except:
                    l2.append('$')
                print(f"Current value of l2 list is: {l2}")
                ind+=1
            l.append(l2)
        s2=""
        for i in l4:
            i2=l3.index(i)
            for ele in l:
                try:
                    s2 += ele[i2]
                except:
                    pass

        print(s2)
        with open(fn,'r+') as f:
            f.write(s2)


    def decrypt():
        l5=[]
        fn=v9.get()
        with open(fn,'r+')as f:
            s4=f.read()
            f.truncate(0)
        a=string.ascii_lowercase
        key="german"
        b=s4
        c=b.replace(' ','')
        d={}
        for letter in key:
            d[letter]=a.index(letter)
        print(f"Value of dictionary d is: {d}")
        l3=list(d.values())
        l4=sorted(l3)
        cols=len(key)
        v=ceil(len(c)/len(key))
        for i in range(v):
            l6=[]
            for j in range(len(key)):
                l6.append('$')
            l5.append(l6)

        si=0
        for i in l4:
            i2=l3.index(i)
            for item in l5:
                if s4[si]!='$':
                    item[i2]=s4[si]
                si+=1
        decrypted_string=""
        for item in l5:
            decrypted_string+="".join(item)
            ds=decrypted_string.replace('$',"")
        with open(fn,'r+')as f:
            f.write(ds)

    Button(t2, text="Encrypt", command=encrypt).place(x=50, y=150)
    Button(t2, text="Decrypt", command=decrypt).place(x=150, y=150)


def fe():
    subprocess.Popen('explorer "D:\Projects\OS"')
def np():
    def save():
        i=t.get('1.0','end-1c')
        global memory_occ,fname,li,lenlist
        memory_occ+=len(i)
        print(len(i))
        print(memory_occ)
        lenlist.append(len(i))
        filename=chr(fname)+".txt"
        li.append(filename)
        fname+=1
        if memory_occ<=memory_buffer:
            with open(filename,'w') as f:
                f.write(i)


        else:
            while(memory_occ>memory_buffer):
                temp=li[0]
                src=r'D:/Projects/OS'+temp
                dest = r'D:/Projects/OS' + temp
                desti=shutil.copy(src,dest)
                os.remove(li[0])
                memory_occ-=lenlist[0]
                del li[0]
                del lenlist[0]

            with open(filename,'w') as f:
                f.write(i)

    t3 = Tk()
    t3.geometry("1200x1200")
    t3.configure(background='grey')
    t=Text(t3,height=40,width=100)
    t.pack()
    b=Button(t3,text='Save',command=save)
    b.pack()
def desktop():
    t1=Tk()
    t1.configure(background='blue')
    t1.geometry("1600x1600")
    p1=PhotoImage(file='fileexplorer.png')
    p2=PhotoImage(file='notepad.png')
    p3=PhotoImage(file='encrypt.png')
    p4 = PhotoImage(file='read_write.png')
    b1=Button(t1,image=p1,compound=TOP,command=fe)
    b1.image=p1
    b1.place(x=40,y=100)
    b2=Button(t1,image=p2,compound=TOP,command=np)
    b2.image=p2
    b2.place(x=400,y=100)
    b3=Button(t1,image=p3,compound=TOP,command=encrypt_decrypt)
    b3.image=p3
    b3.place(x=760,y=100)
    b4 = Button(t1, image=p4, compound=TOP, command=io)
    b4.image = p4
    b4.place(x=1120, y=100)

def command1():
    if entry1.get()=="admin" and entry2.get()=="pass@123":
        root.destroy()
        desktop()
    else:
        print("Invalid username or password")
        entry1.delete(0,END)
        entry2.delete(0, END)

memory_buffer=100
memory_occ=0
i=0
fname=65
li=[]
lenlist=[]

root=Tk()
root.geometry("1200x1200")
root.title("Login Page")
v=StringVar()
label1=Label(root,text="Username")
entry1=Entry(root)
label2=Label(root,text="Password")
entry2=Entry(root,show="*")
button=Button(root,text="Submit",command=command1)
label1.place(x=400,y=250)
label2.place(x=400,y=300)
entry1.place(x=500,y=250)
entry2.place(x=500,y=300)
button.place(x=450,y=350)
root.mainloop()
