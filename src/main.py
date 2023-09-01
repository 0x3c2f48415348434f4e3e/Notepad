try:
    import tkinter as t
    from tkinter.filedialog import asksaveasfile, SaveAs, askopenfile
    from tkinter import scrolledtext
except:
    print("Ensure that tkinter is installed")
import os
import sys
from io import TextIOWrapper

class Notepad():
    def __init__(self) -> None:
        global win
        global Text
        win = t.Tk() #This creates our main window
        #you should know how a notepad works
        '''
        For example, at the top, we have several tab, such as the file, etc and these allow us to do differnte things
        such as creating new files etc.
    

        For now, lets make it only support .txt file extensions
        '''
        win.geometry("500x500")
        win.title("NotePad")
        Files_tab = t.Label(win, text="File", width=10)
        Files_tab.bind("<Button-1>",Notepad.ForFIles)
        Files_tab.grid(row=0,column=0)

        Edit_tab = t.Label(win, text="Edit", width=10)
        Edit_tab.bind("<Button-1>",Notepad.ForFIles)
        Edit_tab.grid(row=0,column=1)

        #Lets create the entry
        global Text
        Text = scrolledtext.ScrolledText(win,width=300,height=300)
        Text.grid(row=1,column=0, columnspan=500)
        win.mainloop()
    
    @staticmethod
    def ForFIles(test):
        #Lets create a child window
        child = t.Toplevel(win)
        child.geometry("200x300")
        #lets add all the stuff like:
        #open file
        #save file
        #save as
        #new file
        #etc
        supportedFileTypes = {
            "Text file": ".txt"
        }
        childLable = t.Button(child,text="Save", command=asksaveasfile)
        childLable.grid(row=0, column=0)

        #Lets try to do the open command first
        '''So what we want is when the open button
        is clicked, the file exploere will open
        and user can select what file (Will only support .txt for now) they want to
        open and the contents will be displayed 
        on the text

        '''
        childLable1 = t.Button(child,text="open", command=Notepad.openFile)
        childLable1.grid(row=1, column=0)
        child.mainloop()

    @staticmethod
    def openFile():
        store = askopenfile("r")
        #store = io.open(askopenfile("r"),encoding='utf-8')
        value = TextIOWrapper.readlines(store)
        Text.insert('0.0', value)
if __name__ == '__main__':
    App = Notepad()