#updated file. 

from tkinter import *  
import tkinter as tk   
from tkinter import ttk
import os
from csv import DictWriter
from tkinter import messagebox as m_box

win=tk.Tk()
win.title('Gui App')

name_label=ttk.Label(win,text="Name: ").grid(row=0,column=0,sticky=tk.W,padx=4,pady=4)
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1,sticky=tk.W,padx=4,pady=4)


age_label=ttk.Label(win,text="Age: ").grid(row=1,column=0,sticky=tk.W,padx=4,pady=4)
age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1,sticky=tk.W,padx=4,pady=4)


gender_label=ttk.Label(win,text="Gender: ").grid(row=2,column=0,sticky=tk.W,padx=4,pady=4)
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=13,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Select','Male','Female')
gender_combobox.grid(row=2,column=1,sticky=tk.W,padx=4,pady=4)
gender_combobox.current(0)


contact_label=ttk.Label(win,text="Contact: ").grid(row=3,column=0,sticky=tk.W,padx=4,pady=4)
contact_var=tk.StringVar()
contact_entrybox=ttk.Entry(win,width=16,textvariable=contact_var)
contact_entrybox.grid(row=3,column=1,sticky=tk.W,padx=4,pady=4)

email_label=ttk.Label(win,text="Email: ").grid(row=4,column=0,sticky=tk.W,padx=4,pady=4)
email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=4,column=1,sticky=tk.W,padx=4,pady=4)

def action():
    name=name_var.get()
    gender=gender_var.get()
    age=age_var.get()
    contact=contact_var.get()
    email=email_var.get()
            
    if name=='' or age=='' or gender=="Select":
        m_box.showwarning('Warning','Plz Enter Name,Age,Gender')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showwarning('Error','Enter Valid Age.')
        else:
            with open("Data.csv","a",newline='') as f:
                dict_writer=DictWriter(f,fieldnames=['Name','Age','Gender','Contact','Email'])
                if os.stat('Data.csv').st_size==0:
                    dict_writer.writeheader()
                dict_writer.writerow({
                        'Name':name,
                        'Age':age,
                        'Gender':gender,
                        'Contact':contact,
                        'Email':email
                        })
            m_box.showinfo("Success","Form Submited Succesfully.")
            name_entrybox.delete(0,END)
            age_entrybox.delete(0,END)
            email_entrybox.delete(0,END)
            contact_entrybox.delete(0,END)
submit_button=ttk.Button(win,text="Submit",width=16,command=action).grid(row=5,column=0,sticky=tk.E,padx=4,pady=4,columnspan=2)



win.mainloop()



