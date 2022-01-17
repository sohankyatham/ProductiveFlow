# ProductiveFlow - A Productivity App
# By: Sohan Kyatham

# Imports
from tkinter import *
from tkinter import ttk


# Create Screen
root = Tk()
root.geometry("600x600")
root.title("ProductiveFlow")


'''
Functions for MenuBar Options
'''


# FileMenu: New File Function
def NewFileFunc():
    print("New File Created")


# FileMenu: Open File Function
def OpenFileFunc():
    print("Opening a file...")


# FileMenu: Save File Function
def SaveFileFunc():
    print("Saving file...")


# FileMenu: Save As Function
def SaveAsFunc():
    print("Saving file as...")


# FileMenu: Auto Save Function
def DeclareAutoSaveFunc():
    print("Auto saving...")


# FileMenu: Exit App Function 
def ExitFunc(*args):
    root.destroy()
root.bind("<Alt-Key-F4>", ExitFunc)


'''
MenuBar for Program
'''

# Menubar - Place for Placing Menu Options
MenuBar = Menu(root)
root.config(menu=MenuBar)


# File Menu Option
FileMenu = Menu(MenuBar, tearoff=False)
# Add the File Menu to the MenuBar
MenuBar.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="New File", accelerator="Ctrl+N", command=NewFileFunc)
FileMenu.add_command(label="Open File", accelerator="Ctrl+O", command=OpenFileFunc)
FileMenu.add_separator()
FileMenu.add_command(label="Save File", accelerator="Ctrl+S", command=SaveFileFunc)
FileMenu.add_command(label="Save As", accelerator="Ctrl+Shift S", command=SaveAsFunc)
FileMenu.add_separator()
FileMenu.add_command(label="Auto Save", command=DeclareAutoSaveFunc)
FileMenu.add_command(label="Exit Window", accelerator="Alt-F4", command=ExitFunc)


# Edit Menu Option
EditMenu = Menu(MenuBar, tearoff=False)
# Add the Edit Menu to the MenuBar
MenuBar.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=None)
EditMenu.add_command(label="Redo", accelerator="Ctrl+Y", command=None)
EditMenu.add_separator()
EditMenu.add_command(label="Cut", accelerator="Ctrl+X", command=None)
EditMenu.add_command(label="Copy", accelerator="Ctrl+C", command=None)
EditMenu.add_command(label="Paste", accelerator="Ctrl+V", command=None)
EditMenu.add_separator()
EditMenu.add_command(label="Select All", accelerator="Ctrl+A", command=None)


# Tools Menu Option
ToolsMenu = Menu(MenuBar, tearoff=False)
# Add the Tools Menu to the MenuBar
MenuBar.add_cascade(label="Tools", menu=ToolsMenu)
ToolsMenu.add_command(label="Word Count", command=None)
ToolsMenu.add_command(label="Toggle Word Wrap", accelerator="Alt+Z", command=None)


# Help Menu
HelpMenu = Menu(MenuBar, tearoff=False)
# Add the Help Menu to the MenuBar
MenuBar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="Documentation", command=None)
HelpMenu.add_command(label="Release Notes", command=None)
HelpMenu.add_separator()
HelpMenu.add_command(label="About", command=None)


# Tab Control - Place to Hold Tabs
TabControl = ttk.Notebook(root)
TabControl.pack()



"""
******************************************************************
Calendar Section
******************************************************************
"""

# Calendar Frame - A Frame to Place Calendar Program
CalendarFrame = Frame(TabControl, width="590", height="590", bg="#606060")
CalendarFrame.pack(fill="both", expand=1)


# Add Calendar Frame to Tab Control
TabControl.add(CalendarFrame, text="Calendar")


"""
******************************************************************
To-Do List Section
******************************************************************
"""


# To-Do List Frame - A Frame to Place To-do List Program
ToDoListFrame = Frame(TabControl, width="590", height="590", bg="blue")
ToDoListFrame.pack(fill="both", expand=1)


# Add To-Do List Frame to Tab Control
TabControl.add(ToDoListFrame, text="To-Do List")


"""
******************************************************************
Notes Section
******************************************************************
"""


# Notes Frame - A Frame to Place Notes Program
NotesFrame = Frame(TabControl, width="590", height="590", bg="#301030")
NotesFrame.pack(fill="both", expand=1)


# Add Notes Frame to Tab Control
TabControl.add(NotesFrame, text="Notes")


# Initialize Screen
root.mainloop()
