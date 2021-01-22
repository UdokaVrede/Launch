'''this proggram accepts input as website name and url
then stores it into a dictionary and at 8am or system startup
launches all programs
'''

#! /usr/bin/python3

import webbrowser
from tkinter import *
  
def appLook():
    url = name_text.get()
    store = 'https://www.'+url
    urlStore = open('urlStore.txt','a')
    urlStore.writelines(store+'\n')
    urlStore.close()
        
def extractor():
    openStore=open('urlStore.txt','r')
    for i in openStore:
        webbrowser.open_new_tab(i)

app= Tk()

name_text = StringVar()

def gui():
    name_label = Label(app, text = 'Name', font=('bold',14))
    name_label.pack()
    #text entry box
    name_entry = Entry(app,textvariable=name_text)
    name_entry.pack()

    add_btn=Button(app, text='Add url', width=11, command=appLook)
    add_btn.pack()

    run_btn=Button(app, text='open urls', width=11, command=extractor)
    run_btn.pack()

    exit_btn= Button(app, text='exit', command=exit)
    exit_btn.pack()

    app.title('launch') 
    app.geometry('300x200')
    app.mainloop()


gui()