import csv
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.config(bg='white')
root.title('CSV Modifier')
root.resizable(False, False)
root.geometry('375x210')
img = PhotoImage(file="icon.png")
label = Label(root,image=img)
label.place(x=0, y=0)



def select_file():
    filetypes = (('csv files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Upload CSV file',initialdir='/',filetypes=filetypes)
    text=open(filename,'r')
    with open(filename,'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        for line in csv_reader:
            print('-', end='')
        text = ''.join([i for i in text])
        
    showinfo(title='File Uploaded Successfully',message=filename)
    date=simpledialog.askstring(title='Search',prompt='Enter the Date (YYYY-MM-DD)')
    text = text.replace('No,','No,'+ date)
    text = text.replace('GB,','GB,'+ date)
    x=open('Terrena_VM-'+ date+'.csv','w')
    x.writelines(text)
    x.close()
    showinfo(title='Your File is saved',message=x)
    root.destroy()


# open button
style = Style()
style.configure('W.TButton', font =('Arial', 10, 'bold'),foreground = 'green')
open_button = ttk.Button(root,text='Upload CSV File',command=select_file, style = 'W.TButton')
open_button.pack(expand=True)
open_button.place(x=245, y=15)

# run the application
root.mainloop()
