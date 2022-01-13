import shutil
import os
import sys
import tkinter as tk
from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter.ttk import Progressbar

def clear_text():
    text.delete(0,END)

def CreateWidgets():
    link_Label = Label(root, text="Select The File/folder To Copy : ")
    link_Label.grid(row=1, column=0, pady=5, padx=5)
	
    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)
	
    source_browseButton = Button(root, text ="Browse", command = SourceBrowse, width = 15)
    source_browseButton.grid(row = 1, column = 3, pady = 5, padx = 5)
	
    destinationLabel = Label(root, text ="Select The Destination : ")
    destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5)
	
    root.destinationText = Entry(root, width = 50, textvariable = destinationLocation)
    root.destinationText.grid(row = 2, column = 1, pady = 5, padx = 5, columnspan = 2)
	
    dest_browseButton = Button(root, text ="Browse", command = DestinationBrowse, width = 15)
    dest_browseButton.grid(row = 2, column = 3, pady = 5, padx = 5)
	
    copyButton = Button(root, text ="Copy File", command = CopyFile, width = 15)
    copyButton.grid(row = 3, column = 1, pady = 5, padx = 5)
	
    moveButton = Button(root, text ="Move File", command = MoveFile, width = 15)
    moveButton.grid(row = 3, column = 2, pady = 5, padx = 5)

    clearButton = Button(root, text ="Exit", command = quit, width = 15)
    clearButton.grid(row = 3, column = 3, pady = 5, padx = 5)

    bar_Label = Label(root, text="Progress Bar...... : ")
    bar_Label.grid(row=4, column=0, pady=5, padx=5)

def SourceBrowse():
    
    root.files_list = filedialog.askdirectory(initialdir="/", title="Select file")
    root.sourceText.insert('1', root.files_list)
    
def DestinationBrowse():

    root.destinationdirectory = filedialog.askdirectory(initialdir ="This PC")
    root.destinationText.insert('1', root.destinationdirectory)
	
def CopyFile():

    percentLabel = Label(root,textvariable=percent)
    percentLabel.grid(row=4, column=1, pady=5, padx=5)
    
    bar = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
    bar.grid(row=4, column=2, pady=5, padx=5)

    files_list = root.files_list
    
    KB = len(files_list)
    download = 0
    speed = 0.08
    while(download<KB):
        bar['value']+=(speed/KB)*100
        download+=speed
        percent.set(str(int((download/KB)*100))+'%')
        root.update_idletasks()
        
    root.destination_location = destinationLocation.get()

    src = str(root.files_list)
    dst = str(root.destination_location)
    try:
        shutil.copytree(src, dst, dirs_exist_ok = True)
    except:
        print('Sorry...')
    messagebox.showinfo("SUCCESSFUL")

def MoveFile():
    
    files_list = root.files_list
    destination_location = destinationLocation.get()
    for f in files_list:
        shutil.move(f, destination_location)
    messagebox.showinfo("SUCCESSFUL")

root = tk.Tk()
	
root.geometry("830x220")
root.title("Copy-Move GUI")

sourceLocation = StringVar()
destinationLocation = StringVar()
percent = StringVar()
text = StringVar()

CreateWidgets() 
	
root.mainloop()
