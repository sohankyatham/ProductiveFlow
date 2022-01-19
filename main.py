# ProductiveFlow - A Productivity App
# By: Sohan Kyatham


# Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.font as tkfont


# Create Screen
root = Tk()
root.geometry("600x600")
root.title("ProductiveFlow")


# Global OpenFileName - used for finding name/status of opened file and using it later in code for functions such as saving a file and etc
global OpenFileName
OpenFileName = False



'''
Functions for MenuBar Options
'''



# FileMenu: New File Function
def NewFileFunc(*args):
    TextBoxForNotes.delete("1.0", END) 
root.bind('<Control-Key-n>', NewFileFunc)


# FileMenu: Open File Function
def OpenFileFunc(*args):
    # Open File Dialog Asking User Which File They Want to Open
    FilePath = filedialog.askopenfilename(initialdir="C:/gui/", title="Open a File", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"),("JavaScript Files", "*.js"), ("Python Files", "*.py"), ("All Files", "*.*")))
    print(FilePath)
    
    # FilePath is the name of the file and has details corresponding to the file
   
    # Find the Name/Status of the File & use it later in code for other functions such as saving files and saving them as
    if FilePath:
        global OpenFileName
        OpenFileName = FilePath
    
    TextBoxForNotes.delete("1.0", END)

    # Open File and Insert File Content into Editor
    FilePath = open(FilePath, 'r')
    FileContent = FilePath.read()
    TextBoxForNotes.insert(END, FileContent)
    FilePath.close()
root.bind('<Control-Key-o>', OpenFileFunc)


# FileMenu: Save File Function
def SaveFileFunc(*args):
    global OpenFileStatusName

    # If File has been opened then save
    if OpenFileName:
        FilePath = open(OpenFileName, "w")
        FilePath.write(TextBoxForNotes.get(1.0, END))
        FilePath.close()
    # If the file does not exist, then save this file as a file
    else:
        SaveAsFunc()
root.bind('<Control-Key-s>', SaveFileFunc)


# FileMenu: Save As Function
def SaveAsFunc(*args):
    FilePath = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title="Save File As", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("JavaScript Files", "*.js"), ("Python Files", "*.py")))
    if FilePath:
        # Save the File
        FilePath = open(FilePath, "w")
        FilePath.write(TextBoxForNotes.get(1.0, END))
        FilePath.close()
root.bind('<Control-Shift-S>', SaveAsFunc)


# FileMenu: Auto Save Function
def DeclareAutoSaveFunc():
    print("Auto saving...")


# FileMenu: Exit App Function 
def ExitFunc(*args):
    # Open Prompt Asking User whether they wanna save their work before closing 
    root.destroy()
root.bind("<Alt-Key-F4>", ExitFunc)



# HelpMenu: About Screen Function
def AboutScreenFunc():
    # About Screen Window
    AboutScreen = Toplevel(root)
    AboutScreen.title("About")
    AboutScreen.geometry("300x300")
    AboutScreen.resizable(0,0)

    # Mainloop for AboutScreen
    AboutScreen.mainloop()



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
HelpMenu.add_command(label="About", command=AboutScreenFunc)


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
ToDoListFrame = Frame(TabControl, width="590", height="590")
ToDoListFrame.pack(fill="both", expand=1)


# TitleLabel - Displays a Title on the Screen called "To-Do List"
TitleLabel = Label(ToDoListFrame, text="To-Do List", font=("Arial", 25, 'bold'))
TitleLabel.pack(side="top", fill=BOTH)


'''Add Tasks Sections'''

# AddTaskFrame - A Frame for Storing all the Widgets Regarding Add Tasks Functions
AddTaskFrame = Frame(ToDoListFrame, width=250, height=500, bg="lightblue")
AddTaskFrame.pack(side=LEFT, anchor=NE, pady=20)


# EnterTaskLabel - Displays a Label on the Screen called "Enter Your Task"
EnterTaskLabel = Label(AddTaskFrame, text="Enter Your Task:", font=("Arial", 18))
EnterTaskLabel.pack()


# EnterTaskEntry - Displays an Entry Widget Where User Can Enter Their Task
EnterTaskEntry = Entry(AddTaskFrame, font=("Arial", 12))
EnterTaskEntry.pack(pady=5)


# AddTaskButton - Displays a Button called "Add Task" Which Adds a Task into a list of Tasks 
AddTaskButton = Button(AddTaskFrame, text="Add Task", font=("Arial", 12), command=None)
AddTaskButton.pack(pady=5)


'''Tasks Section'''

# TasksFrame - A Frame for Storing all the Widgets Regarding Task Functions
TasksFrame = Frame(ToDoListFrame, width=350, height=500, bg="yellow")
TasksFrame.pack(side=RIGHT, anchor=NW)


# TasksLabel - Displays a Label on the Screen called "Tasks:"
TasksLabel = Label(TasksFrame, text="Tasks:", font=("Arial", 18))
TasksLabel.pack()


# ListBoxForTDList - Displays a Listbox Widget on the Screen or Showing the Tasks That the User Has Entered
ListBoxForTDList = Listbox(TasksFrame, width=55, height=30)
ListBoxForTDList.pack()


# Add To-Do List Frame to Tab Control
TabControl.add(ToDoListFrame, text="To-Do List")


"""
******************************************************************
Notes Section
******************************************************************
"""


# Notes Frame - A Frame to Place Notes Program
NotesFrame = Frame(TabControl, width="590", height="590")
NotesFrame.pack(fill="both", expand=1)


# StatusBar - For Displaying Word and Character Count
StatusBar = Label(NotesFrame, text="CHARACTER: WORD:", anchor=W)
StatusBar.config(bg="Dodgerblue")
StatusBar.pack(fill=X, side=BOTTOM, ipady=2)


# Vertical Scrollbar
VerticalScrollbar = Scrollbar(NotesFrame)
VerticalScrollbar.pack(side=RIGHT, fill=Y)


# Horizontal Scrollbar
HorizontalScrollbar = Scrollbar(NotesFrame, orient="horizontal")
HorizontalScrollbar.pack(side=BOTTOM, fill=X)


# TextBoxForNotes - Place for Writing Notes/Text
TextBoxForNotes = Text(NotesFrame, width=500, height=500, font=("DejaVu Sans Mono", 16), selectbackground="Skyblue", selectforeground="black", undo=True, wrap="none", yscrollcommand=VerticalScrollbar.set, xscrollcommand=HorizontalScrollbar.set)
TextBoxForNotes.pack()


# Set Default Tab Size (4 Spaces) for Text Box 
font = tkfont.Font(font=TextBoxForNotes['font'])
TabSize = font.measure("    ") # 4 Spaces
TextBoxForNotes.config(tabs=TabSize)


# Configure the Vertical and Horizontal Scrollbar
VerticalScrollbar.config(command=TextBoxForNotes.yview)
HorizontalScrollbar.config(command=TextBoxForNotes.xview)


# Add Notes Frame to Tab Control
TabControl.add(NotesFrame, text="Notes")


# Initialize Screen
root.mainloop()
