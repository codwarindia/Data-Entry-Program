import tkinter as tk
from tkinter import ttk
import os
from csv import DictWriter


win=tk.Tk()
win.title('Gui App')

name_label=ttk.Label(win,text="Name: ").grid(row=0,column=0,sticky=tk.W)
name_var=tk.StringVar()
name_enterybox=ttk.Entry(win,width=16,textvariable=name_var).grid(row=0,column=1,sticky=tk.W)


age_label=ttk.Label(win,text="Age: ").grid(row=1,column=0,sticky=tk.W)
age_var=tk.StringVar()
age_enterybox=ttk.Entry(win,width=16,textvariable=age_var).grid(row=1,column=1,sticky=tk.W)


gender_label=ttk.Label(win,text="Gender: ").grid(row=2,column=0,sticky=tk.W)
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=13,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Select','Male','Female')
gender_combobox.grid(row=2,column=1,sticky=tk.W)
gender_combobox.current(0)


contact_label=ttk.Label(win,text="Contact: ").grid(row=3,column=0,sticky=tk.W)
contact_var=tk.StringVar()
contact_enterybox=ttk.Entry(win,width=16,textvariable=contact_var).grid(row=3,column=1,sticky=tk.W)

email_label=ttk.Label(win,text="Email: ").grid(row=4,column=0,sticky=tk.W)
email_var=tk.StringVar()
email_enterybox=ttk.Entry(win,width=16,textvariable=email_var).grid(row=4,column=1,sticky=tk.W)

def action():
    name=name_var.get()
    age=age_var.get()
    gender=gender_var.get()
    contact=contact_var.get()
    email=email_var.get()

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
submit_button=ttk.Button(win,text="Submit",command=action).grid(row=5,column=0,sticky=tk.E)



win.mainloop()