# ProductiveFlow - A Productivity App
# By: Sohan Kyatham



# Imports
from tkinter import *
from tkinter import ttk
import calendar
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkfont
import pickle
import time
import webbrowser



# Create Window
root = Tk()


# Set up Geometry and Center the Window
Window_Width = 600
Window_Height = 600

# Get Screen Width and Height
Screen_Width = root.winfo_screenwidth()
Screen_Height = root.winfo_screenheight()

# Calculate the Screen_x and Screen_y Coordinate Positions
x = (Screen_Width / 2) - (Window_Width / 2)
y = (Screen_Height / 2) - ((Window_Height / 2) + 50)

# Place the Window in the Center of the Screen
root.geometry("%dx%d+%d+%d" % (Window_Width, Window_Height, x, y))


root.title("ProductiveFlow")
root.resizable(False, False)



# Notes: Global OpenFileName - used for finding name/status of opened file and using it later in code for functions such as saving a file and etc
OpenFileName = False


# Notes: Global SelectedText - used for storing any selected text and then pasting that text into the TextBoxForNotes
SelectedText = False


# Stopwatch: Global StopwatchRunningStatus - used for checking if the Stopwatch is running or not
StopwatchRunningStatus = False


# Stopwatch: Global Hours, Minutes, and Seconds - used for Reseting Time on Stopwatch
Stopwatch_Hours = 0
Stopwatch_Minutes = 0
Stopwatch_Seconds = 0


# Timer: Global TimerRunningStatus - used for checking if the Timer is running or not
TimerRunningStatus = False


# Timer: Global Hours, Minutes, and Seconds
Timer_Hours = StringVar()
Timer_Minutes = StringVar()
Timer_Seconds = StringVar()

Timer_Hours.set("00")
Timer_Minutes.set("00")
Timer_Seconds.set("00")



'''
Functions for MenuBar Options
'''



# Calendar: Show Calendar Function
def ShowCalendarFunc():
    CalendarMonth = int(MonthSpinbox.get())
    CalendarYear = int(YearSpinbox.get())
    CalendarOutput = calendar.month(CalendarYear, CalendarMonth)

    CalendarDisplay.insert('end', CalendarOutput)


# Calendar: Clear Calendar Function
def ClearCalendarFunc():
    pass



# FileMenu: New File Function
def NewFileFunc(*args):
    global OpenFileName

    OpenFileName = False
    TextBoxForNotes.delete("1.0", END)  

root.bind('<Control-Key-n>', NewFileFunc)


# FileMenu: Open File Function
def OpenFileFunc(*args):
    # Open File Dialog Asking User Which File They Want to Open
    FilePath = filedialog.askopenfilename(title="Open a File", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"),("JavaScript Files", "*.js"), ("Python Files", "*.py"), ("All Files", "*.*")))
    print(FilePath)
    
    # FilePath is the name of the file and has details corresponding to the file
   
    # Find the Name/Status of the File & use it later in code for other functions such as saving files and saving them as
    if FilePath:
        global OpenFileName
        OpenFileName = FilePath
    

    # Open File and Insert File Content into Editor
    FilePath = open(FilePath, 'r')
    FileContent = FilePath.read()
    TextBoxForNotes.delete("1.0", END)
    TextBoxForNotes.insert(END, FileContent)
    FilePath.close()
root.bind('<Control-Key-o>', OpenFileFunc)


# FileMenu: Save File Function
def SaveFileFunc(*args):
    global OpenFileName

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
    FilePath = filedialog.asksaveasfilename(defaultextension=".*", title="Save File As", filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("JavaScript Files", "*.js"), ("Python Files", "*.py")))
    if FilePath:
        # Save the File
        FilePath = open(FilePath, "w")
        FilePath.write(TextBoxForNotes.get(1.0, END))
        FilePath.close()
root.bind('<Control-Shift-S>', SaveAsFunc)


# FileMenu: Declare Auto Save Function
def DeclareAutoSaveFunc():
    global OpenFileName
    # Declare the Auto Save function - write code for what the Auto Save function is supposed to do
    if OpenFileName:
        FileContentData = TextBoxForNotes.get("1.0", "end-1c")
        with open(OpenFileName, "w") as SaveContent:
            SaveContent.write(FileContentData)


# FileMenu: Initialize Auto Save Function
def InitAutoSave():
    if AutoSave_CheckMark.get():
        DeclareAutoSaveFunc()
        TextBoxForNotes.after(100, InitAutoSave)
    else: 
        # Undeclare the Python Function - Turn OFF the AutoSave Feature
        AutoSave_CheckMark.set(False)


# FileMenu: Exit App Function 
def ExitFunc(*args):
    global OpenFileName

    # Open Prompt Asking User whether they wanna save their work before closing 
    ExitTitle = "Do you want to save the changes you made to this file?"
    ExitMessage = "Your changes will be lost if you don't save this file. Are you sure you still want to exit this application?"

    if OpenFileName:
        ExitConfirmation = messagebox.askquestion(ExitTitle, ExitMessage)
        
        if ExitConfirmation == "yes":
            root.destroy()
        else:
            pass
root.bind("<Alt-Key-F4>", ExitFunc)



# ToolsMenu: Declare Word Count and Character Count Function
def DeclareWordCount():
    # Get Content from TextBoxForNotes - Turn String Into a Number: of characters and words
    TextContent_ForWordCount = TextBoxForNotes.get("1.0", END)
    # String to Number 
    CharactersInTextBoxForNotes = len(TextContent_ForWordCount)    
    WordsInTextBoxForNotes = len(TextContent_ForWordCount.split())
    # Config in Status Bar
    StatusBar.config(text=str(CharactersInTextBoxForNotes-1) + " Characters, " + str(WordsInTextBoxForNotes) + " Words, ")


# ToolsMenu: Initialize Word Count Function
def InitWordCount():
    # Check if the function is already active, if it is, then turn of word count
    if WordCount_CheckMark.get():
        DeclareWordCount()
        StatusBar.after(100, InitWordCount)
    else: 
        WordCount_CheckMark.set(False)
        StatusBar.config(text="")


# ToolsMenu: Toggle Word Wrap Function
def ToggleWordWrap(*args):

    # If there is no word wrap then add word wrap
    if TextBoxForNotes.cget("wrap") == "none":
        TextBoxForNotes.configure(wrap="word")
        # Turn on Check Mark if the Function is called 
        WordWrap_CheckMark.set(True)

    # If there is word wrap then take out word wrap
    elif TextBoxForNotes.cget("wrap") == "word":
        TextBoxForNotes.configure(wrap="none")
        # Turn off Check Mark if the Function is disabled
        WordWrap_CheckMark.set(False)
root.bind("<Alt-Key-z>", ToggleWordWrap)



# EditMenu: Cut Text Function
def CutText(e):
    global SelectedText
    # Check to see if keyboard shortcut was used
    if e:
        SelectedText = root.clipboard_get()
    else:
        # Grab selected text - then copy that text and remove it from TextBoxForNotes
        if TextBoxForNotes.selection_get():
            SelectedText = TextBoxForNotes.selection_get()
            TextBoxForNotes.delete("sel.first", "sel.last")
            # If copy option is used from edit menu and clear clipboard
            root.clipboard_clear()
            root.clipboard_append(SelectedText)
root.bind("<Control-Key-x>", CutText)


# EditMenu: Copy Text Function
def CopyText(e):
    global SelectedText
    # Check to see if the keyboard shortcut was used
    if e:
        SelectedText = root.clipboard_get()
    # Check to see if there is selected text - if there is then copy it
    if TextBoxForNotes.selection_get():
        SelectedText = TextBoxForNotes.selection_get()
        # If copy option is used from edit menu and clear clipboard
        root.clipboard_clear()
        root.clipboard_append(SelectedText)
root.bind("<Control-Key-c>", CopyText)


# EditMenu: Paste Text Function
def PasteText(e):
    global SelectedText
    # Check to see if shortcut is used
    if e:
        SelectedText = root.clipboard_get()
    else:
        # Paste the Selected Text into the Cursor Position
        if SelectedText:
            CursorPosition = TextBoxForNotes.index(INSERT)
            TextBoxForNotes.insert(CursorPosition, SelectedText)
root.bind("<Control-Key-v>", PasteText)


# EditMenu: Select All Function
def SelectAll(e):
    TextBoxForNotes.tag_add("sel", 1.0, "end")
root.bind("<Control-Key-a>", SelectAll)



# HelpMenu: Documentation Function 
def DocumentationFunc(): # In the future create a new tab directly in the ProductivityFlow Application and include the link
    webbrowser.open("https://github.com/sohankyatham/ProductiveFlow/blob/main/Version%201.0.0/Documentation.md")


# HelpMenu: Release Notes Function
def ReleaseNotesFunc():
    webbrowser.open("www.google.com")


# HelpMenu: About Screen Function
def AboutScreenFunc():
    # About Screen Window
    AboutScreen = Toplevel(root)
    AboutScreen.title("About")
    AboutScreen.geometry("300x200")
    AboutScreen.resizable(0,0)

    # AboutHeader - Displays a Label called "ProductiveFlow"
    AboutHeader = Label(AboutScreen, text="ProductiveFlow", font=("Arial", 30))
    AboutHeader.pack(pady=5)

    # AboutHeaderAttribution
    AboutHeaderAttribtion = Label(AboutScreen, text="By: Sohan Kyatham", width=16, font=("Arial", 12))
    AboutHeaderAttribtion.pack()

    # AboutVersion
    AboutVersion = Label(AboutScreen, text="Version: 1.0.0", width=16, font=("Arial", 12))
    AboutVersion.pack()

    # Operating System Version
    AboutOSVersion = Label(AboutScreen, text="OS: Windows", width=16, font=("Arial", 12))
    AboutOSVersion.pack()

    # View README.md File Function
    def ViewREADMEFunc():
        webbrowser.open("https://github.com/sohankyatham/ProductiveFlow/blob/main/README.md")

    # View README.md Button
    ViewREADME = Button(AboutScreen, text="View README.md file on GitHub", width=26, font=("Arial", 12), bg="#26aceb", command=ViewREADMEFunc)
    ViewREADME.pack(pady=15)

    # Mainloop for AboutScreen
    AboutScreen.mainloop()



'''
Functions for To-Do List
'''



# To-Do List: Add Task Function
def AddTaskFunc():
    Task = EnterTaskEntry.get(1.0, END)
    
    # Add Task to ListBoxForTDList
    ListBoxForTDList.insert(END, Task)
    EnterTaskEntry.delete(1.0, END)


# To-Do List: Delete Task Function
def DeleteTaskFunc():
    try:
        TaskSelected = ListBoxForTDList.curselection()[0]
        ListBoxForTDList.delete(TaskSelected)
    except:
        messagebox.showwarning(title="No Task Selected!", message="There was no task selected. Please select a task.")


# To-Do List: Save Tasks Function
def SaveTasksFunc():
    UserFile_ToDoList = filedialog.asksaveasfilename(title="Save To-Do List As File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))

    if UserFile_ToDoList:
        if UserFile_ToDoList.endswith(".dat"):
            pass
        else:
            UserFile_ToDoList = f'{UserFile_ToDoList}.dat'

    # Get the Tasks from the ListBox and Open the File and Write/Save the Tasks
    ToDoList_Tasks = ListBoxForTDList.get(0, END)
    ToDoList_TasksForSaving = open(UserFile_ToDoList, "wb")
    pickle.dump(ToDoList_Tasks, ToDoList_TasksForSaving)



# To-Do List: Load Tasks Function
def LoadTasksFunc():
    UserFile_ToDoList = filedialog.askopenfilename(title="Open A To-Do List As A File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))

    # Open the File and Insert it Into ListBoxForTDList
    if UserFile_ToDoList:
        # Delete Everything in the To-Do List
        ListBoxForTDList.delete(0, END)
        # Open To-Do List File
        Open_ToDoListFile = open(UserFile_ToDoList, "rb")
        # Insert To-Do List into ListBoxForTDList
        ToDoList_Tasks = pickle.load(Open_ToDoListFile)
        for ToDoList_Task in ToDoList_Tasks:
            ListBoxForTDList.insert(END, ToDoList_Task)



'''
Functions for Stopwatch
'''



# Stopwatch: Start Stopwatch Function
def StartStopwatchFunc():
    global StopwatchRunningStatus

    # Start the Stopwatch
    if not StopwatchRunningStatus:
        UpdateStopwatchFunc()
        StopwatchRunningStatus = True

    # Disable StartStopwachBtn
    StartStopwatchBtn["state"] = "disabled"
    StopStopwatchBtn["state"] = "normal"
    ResetStopwatchBtn["state"] = "normal"
    

# Stopwatch: Pause Sopwatch Function
def StopStopwatchFunc():
    global StopwatchRunningStatus

    # Stop Running the Stopwatch
    if StopwatchRunningStatus:
        TimeLapsedLabel.after_cancel(UpdateStopwatchTime)
        StopwatchRunningStatus = False

    # Disable PauseStopwachBtn
    StartStopwatchBtn["state"] = "normal"
    StopStopwatchBtn["state"] = "disabled"
    ResetStopwatchBtn["state"] = "normal"


# Stopwatch: Reset Stopwatch Function
def ResetStopwatchFunc():
    global StopwatchRunningStatus
    global Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds

    # Stop Running the Stopwatch
    if StopwatchRunningStatus:
        TimeLapsedLabel.after_cancel(UpdateStopwatchTime)
        StopwatchRunningStatus = False
    
    # Reset Time and TimeLapsedLabel
    Stopwatch_Hours = 0
    Stopwatch_Minutes = 0
    Stopwatch_Seconds = 0

    TimeLapsedLabel.config(text='00:00:00')

    # Disable StartStopwachBtn
    StartStopwatchBtn["state"] = "normal"
    StopStopwatchBtn["state"] = "normal"
    ResetStopwatchBtn["state"] = "disabled"


# Stopwatch: Update Stopwatch Function
def UpdateStopwatchFunc():
    global Stopwatch_Hours, Stopwatch_Minutes, Stopwatch_Seconds
    global UpdateStopwatchTime

    # Update the Stopwatch
    Stopwatch_Seconds += 1

    if Stopwatch_Seconds == 60:
        Stopwatch_Minutes += 1
        Stopwatch_Seconds = 0
    if Stopwatch_Minutes == 60:
        Stopwatch_Hours += 1
        Stopwatch_Minutes = 0

    # Format the TimeLapsedLabel to Include Leading Zeros
    Hours_StringValue = f'{Stopwatch_Hours}' if Stopwatch_Hours > 9 else f'0{Stopwatch_Hours}'
    Minutes_StringValue = f'{Stopwatch_Minutes}' if Stopwatch_Minutes > 9 else f'0{Stopwatch_Minutes}'
    Seconds_StringValue = f'{Stopwatch_Seconds}' if Stopwatch_Seconds > 9 else f'0{Stopwatch_Seconds}'

    # Configure the TimeLapsedLabel
    TimeLapsedLabel.config(text=Hours_StringValue + ':' + Minutes_StringValue + ':' + Seconds_StringValue)

    # Update the TimeLapsedLabel after Every Second
    UpdateStopwatchTime = TimeLapsedLabel.after(1000, UpdateStopwatchFunc)



'''
Functions for Timer
'''



# Timer: Start Timer Function
def StartTimerFunc():
    global TimerRunningStatus

    TimerRunningStatus = True

    try:
        Timer_UserInput = int(Timer_Hours.get())*3600 + int(Timer_Minutes.get())*60 + int(Timer_Seconds.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while Timer_UserInput >-1 and TimerRunningStatus:
        mins,secs = divmod(Timer_UserInput,60) 

        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
	
        Timer_Hours.set("{0:2d}".format(hours))
        Timer_Minutes.set("{0:2d}".format(mins))
        Timer_Seconds.set("{0:2d}".format(secs))

	
        root.update()
        time.sleep(1)

	
        if (Timer_UserInput == 0):
            messagebox.showinfo("", "Time's Up")
		

        Timer_UserInput -= 1



# Timer: Stop Timer Function
def StopTimerFunc():
    global TimerRunningStatus
    TimerRunningStatus = False


# Timer: Reset Timer Function
def ResetTimerFunc():
    global TimerRunningStatus
    global Timer
    TimerRunningStatus = False

    Timer_Hours.set("00")
    Timer_Minutes.set("00")
    Timer_Seconds.set("00")



# Tab Control - Place to Hold Tabs (Calendar Tab, To-Do List Tab, Notes Tab, Stopwatch Tab, and Timer Tab)
TabControl = ttk.Notebook(root)
TabControl.pack()



"""
******************************************************************
Calendar Section
******************************************************************
"""


# Calendar Frame - A Frame to Place Calendar Program
CalendarFrame = Frame(TabControl, width="590", height="590", bg="#f5db6f")
CalendarFrame.pack(fill="both", expand=1)


# Calendar Setup Frame - A Frame to Place All Widgets to Set Up Calendar
CalendarSetupFrame = Frame(CalendarFrame, width=590, height=100, bg="#f5db6f")
CalendarSetupFrame.pack(pady=25)


'''Calendar: Months Section'''


# Month Label 
MonthLabel = Label(CalendarSetupFrame, text="Month: ", font=('Arial', 20), bg="#f5db6f")
MonthLabel.grid(row=0, column=0)


# Month Spinbox
MonthSpinbox = Spinbox(CalendarSetupFrame, from_=1, to=12, width=5, font=("Arial", 20))
MonthSpinbox.grid(row=0, column=1)


'''Calendar: Year Section'''


# Empty Frame
EmptyFrame = Frame(CalendarSetupFrame, width=36, bg="#f5db6f")
EmptyFrame.grid(row=0, column=2)


# Year Label 
YearLabel = Label(CalendarSetupFrame, text="Year: ", font=('Arial', 20), bg="#f5db6f")
YearLabel.grid(row=0, column=3)


# Year Spinbox
YearSpinbox = Spinbox(CalendarSetupFrame, from_=2022, to=3000, width=5, font=("Arial", 20))
YearSpinbox.grid(row=0, column=4)


'''Calendar: Calendar Display'''


# Calendar Display Text Widget
CalendarDisplay = Text(CalendarFrame, width=33, height=8, relief=RIDGE, borderwidth=2, font=("Courier", 16))
CalendarDisplay.pack()


'''Calendar: Buttons Section'''


# Calendar Buttons Frame - A Frame in CalendarFrame to Place Buttons
CalendarBtnsFrame = Frame(CalendarFrame, width=450, height=450, bg="#f5db6f")
CalendarBtnsFrame.pack(pady=30)


# Show Calendar Button
ShowCalendarBtn = Button(CalendarBtnsFrame, text="Show", width=10, font=("Arial", 16), bg="#15e650", bd=1, command=ShowCalendarFunc)
ShowCalendarBtn.pack(pady=5)


# Clear Calendar Button
ClearCalendarBtn = Button(CalendarBtnsFrame, text="Clear", width=10, font=("Arial", 16), bg="#e63030", bd=1, command=ClearCalendarFunc)
ClearCalendarBtn.pack(pady=5)


# Add Calendar Frame to Tab Control
TabControl.add(CalendarFrame, text="Calendar")


"""
******************************************************************
To-Do List Section
******************************************************************
"""


# To-Do List Frame - A Frame to Place To-do List Program
ToDoListFrame = Frame(TabControl, width="550", height="550", bg="lightgray")
ToDoListFrame.pack(fill="both", expand=1)


# TitleLabel - Displays a Title on the Screen called "To-Do List"
TitleLabel = Label(ToDoListFrame, text="To-Do List", font=("Arial", 36, 'bold'), bg="lightgray")
TitleLabel.pack(side="top", fill=BOTH)


'''Add Tasks Sections'''


# ManageTaskFrame - A Frame for Storing all the Widgets Regarding Adding/Deleting Tasks Functions
ManageTaskFrame = Frame(ToDoListFrame, width=250, height=500, bg="lightgray")
ManageTaskFrame.pack(side=LEFT, anchor=NE, pady=20)


# EnterTaskLabel - Displays a Label on the Screen called "Enter A Task"
EnterTaskLabel = Label(ManageTaskFrame, text="Enter A Task:", width=14, font=("Arial", 20, 'bold'), bg="#26aceb", fg="Whitesmoke")
EnterTaskLabel.pack(padx=5)


# EnterTaskEntry - Displays an Text Widget Where User Can Enter A Task
EnterTaskEntry = Text(ManageTaskFrame, width=16, height=1, bd=2, font=("Arial", 14))
EnterTaskEntry.pack(pady=10)


# AddTaskButton - Displays a Button called "Add Task" Which Adds a Task into a list of Tasks 
AddTaskButton = Button(ManageTaskFrame, text="Add Task", width=10, font=("Arial", 14), bg="#15e650", command=AddTaskFunc)
AddTaskButton.pack(pady=5)


# DeleteTaskBtn - Displays a Button called "Delete Task" Which Deletes a Task in the ListBoxForTDList
DeleteTaskBtn = Button(ManageTaskFrame, text="Delete Task", width=10, font=("Arial", 14), bg="#e63030", command=DeleteTaskFunc)
DeleteTaskBtn.pack()


# SaveTasksBtn - Displays a Button called "Save Tasks" Which Saves the Tasks to a File Which can be opened later
SaveTasksBtn = Button(ManageTaskFrame, text="Save Tasks", width=10, bg="#9b34eb", font=("Arial", 14), command=SaveTasksFunc)
SaveTasksBtn.pack(pady=5)


# LoadTasksBtn - Displays a Button called "Load Tasks" Which Loads the Tasks into the ListBoxForTDList
LoadTasksBtn = Button(ManageTaskFrame, text="Load Tasks", width=10, bg="#1E90FF", font=("Arial", 14), command=LoadTasksFunc)
LoadTasksBtn.pack()


'''Tasks Section'''


# TasksFrame - A Frame for Storing all the Widgets Regarding Task Functions
TasksFrame = Frame(ToDoListFrame, width=350, height=500, bg="#5856D6")
TasksFrame.pack(side=RIGHT, anchor=NW, pady=20)


# TasksLabel - Displays a Label on the Screen called "Tasks:"
TasksLabel = Label(TasksFrame, text="Tasks:", font=("Arial", 20, 'bold'), bg="#5856D6", fg="Whitesmoke")
TasksLabel.pack()


# ListBoxForTDList - Displays a Listbox Widget on the Screen or Showing the Tasks That the User Has Entered
ListBoxForTDList = Listbox(TasksFrame, width=55, height=30, bd=2)
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
StatusBar = Label(NotesFrame, text="", anchor=W)
StatusBar.config(bg="Dodgerblue")
StatusBar.pack(fill=X, side=BOTTOM, ipady=2)


# Vertical Scrollbar For Notes
VerticalScrollbar = Scrollbar(NotesFrame)
VerticalScrollbar.pack(side=RIGHT, fill=Y)


# Horizontal Scrollbar For Notes
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


"""
******************************************************************
Stopwatch Section
******************************************************************
"""


# Stopwatch Frame - A Frame to Place Stopwatch
StopwatchFrame = Frame(TabControl, width="590", height="590", bg="lightblue")
StopwatchFrame.pack(fill="both", expand=1)


# Current Time (Time Lapsed) Label
TimeLapsedLabel = Label(StopwatchFrame, text="00:00:00", font=("Arial", 65), bg="lightblue")
TimeLapsedLabel.pack()


# Stopwatch Buttons Frame - A Frame in StopwatchFrame to Place Buttons
StopwatchBtnsFrame = Frame(StopwatchFrame, width=450, height=450, bg="lightblue")
StopwatchBtnsFrame.pack(pady=40)


# Start Stopwatch Button
StartStopwatchBtn = Button(StopwatchBtnsFrame, text="Start", width=18, font=("Arial", 28), bg="#15e650", bd=1, command=StartStopwatchFunc)
StartStopwatchBtn.pack(pady=5)


# Stop Stopwatch Button
StopStopwatchBtn = Button(StopwatchBtnsFrame, text="Stop", width=18, font=("Arial", 28), background="#e63030", bd=1, command=StopStopwatchFunc)
StopStopwatchBtn.pack(pady=5)


# Reset Stopwatch Button
ResetStopwatchBtn = Button(StopwatchBtnsFrame, text="Reset", width=18, font=("Arial", 28), background="lightgray", bd=1, command=ResetStopwatchFunc)
ResetStopwatchBtn.pack(pady=5)


# Add Stopwatch Frame to Tab Control
TabControl.add(StopwatchFrame, text="Stopwatch")


"""
******************************************************************
Timer Section
******************************************************************
"""


# Timer Frame - A Frame to Place Timer
TimerFrame = Frame(TabControl, width="590", height="590", bg="#d4ccc3")
TimerFrame.pack(fill="both", expand=1)


# Timer Setup Frame - A Frame to Place All Widgets to Set Up Timer
TimerSetupFrame = Frame(TimerFrame, width=500, height=500, bg="#d4ccc3")
TimerSetupFrame.pack(pady=25)


'''Timer: Hours Section'''


# Timer Hours Setup Frame - A Frame to Place Label & Entry Boxes to Set Up Hours for Timer
TimerHoursSetupFrame = Frame(TimerSetupFrame, width=250, height=100, bg="#d4ccc3")
TimerHoursSetupFrame.grid(row=0, column=0, padx=10)


# Timer Hours Label
Timer_HoursLabel = Label(TimerHoursSetupFrame, text="Hours:", font=("Arial", 33), bg="#d4ccc3")
Timer_HoursLabel.grid(row=0, column=0)


# Timer Hours Entry
Timer_HoursEntry = Entry(TimerHoursSetupFrame, width=10, font=("Arial", 23), textvariable=Timer_Hours)
Timer_HoursEntry.grid(row=1, column=0)


'''Timer: Minutes Section'''


# Timer Minutes Setup Frame - A Frame to Place Entry Boxes to Set Up Minutes for Timer
TimerMinutesSetupFrame = Frame(TimerSetupFrame, width=250, height=100, bg="#d4ccc3")
TimerMinutesSetupFrame.grid(row=0, column=1, padx=10)


# Timer Minutes Label
Time_MinutesLabel = Label(TimerMinutesSetupFrame, text="Minutes:", font=("Arial", 33), bg="#d4ccc3")
Time_MinutesLabel.grid(row=0, column=1)


# Timer Minutes Entry
Timer_MinutesEntry = Entry(TimerMinutesSetupFrame, width=10, font=("Arial", 23), textvariable=Timer_Minutes)
Timer_MinutesEntry.grid(row=1, column=1)


'''Timer: Seconds Section'''


# Timer Seconds Setup Frame - A Frame to Place Entry Boxes to Set Up Seconds for Timer
TimerSecondsSetupFrame = Frame(TimerSetupFrame, width=250, height=100, bg="#d4ccc3")
TimerSecondsSetupFrame.grid(row=0, column=2, padx=10)


# Timer Seconds Label
Time_SecondsLabel = Label(TimerSecondsSetupFrame, text="Seconds:", font=("Arial", 33), bg="#d4ccc3")
Time_SecondsLabel.grid(row=0, column=1)


# Timer Seconds Entry
Timer_SecondsEntry = Entry(TimerSecondsSetupFrame, width=10, font=("Arial", 23), textvariable=Timer_Seconds)
Timer_SecondsEntry.grid(row=1, column=1)


'''Timer: Buttons Frame'''


# Timer Buttons Frame - A Frame to Place All Buttons for Timer
TimerBtnsFrame = Frame(TimerFrame, width=450, height=325, bg="#d4ccc3")
TimerBtnsFrame.pack(pady=40)


# Start Timer Button
StartTimerBtn = Button(TimerBtnsFrame, text="Start", width=14, font=("Arial", 25), bg="#16c93a", bd=1, command=StartTimerFunc)
StartTimerBtn.pack(pady=5)


# Stop Timer Button
StopTimerBtn = Button(TimerBtnsFrame, text="Stop", width=14, font=("Arial", 25), background="#e63030", bd=1, command=StopTimerFunc)
StopTimerBtn.pack(pady=5)


# Reset Timer Button
ResetTimerBtn = Button(TimerBtnsFrame, text="Reset", width=14, font=("Arial", 25), background="lightgray", bd=1, command=ResetTimerFunc)
ResetTimerBtn.pack(pady=5)


# Add Timer Frame to Tab Control
TabControl.add(TimerFrame, text="Timer")



'''
MenuBar for Program
'''



# Menubar - Place for Placing Menu Options
MenuBar = Menu(root)
root.config(menu=MenuBar)



# Check Marks for Options in FileMenu
AutoSave_CheckMark = BooleanVar()
AutoSave_CheckMark.set(False)


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
FileMenu.add_checkbutton(label="Auto Save", onvalue=1, offvalue=0, variable=AutoSave_CheckMark, command=InitAutoSave)
FileMenu.add_command(label="Exit Window", accelerator="Alt-F4", command=ExitFunc)


# Edit Menu Option
EditMenu = Menu(MenuBar, tearoff=False)
# Add the Edit Menu to the MenuBar
MenuBar.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=TextBoxForNotes.edit_undo)
EditMenu.add_command(label="Redo", accelerator="Ctrl+Y", command=TextBoxForNotes.edit_redo)
EditMenu.add_separator()
EditMenu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: CutText(False))
EditMenu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: CopyText(False))
EditMenu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: PasteText(False))
EditMenu.add_separator()
EditMenu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: SelectAll(True))



# Check Marks for Options in ToolsMenu
WordCount_CheckMark = BooleanVar()
WordCount_CheckMark.set(True)

WordWrap_CheckMark = BooleanVar()
WordWrap_CheckMark.set(False)


# Tools Menu Option
ToolsMenu = Menu(MenuBar, tearoff=False)
# Add the Tools Menu to the MenuBar
MenuBar.add_cascade(label="Tools", menu=ToolsMenu)
ToolsMenu.add_checkbutton(label="Word Count", onvalue=1, offvalue=0, variable=WordCount_CheckMark, command=InitWordCount)
ToolsMenu.add_checkbutton(label="Toggle Word Wrap", accelerator="Alt+Z", onvalue=1, offvalue=0, variable=WordWrap_CheckMark, command=ToggleWordWrap)


# Stopwatch Menu
StopwatchMenu = Menu(MenuBar, tearoff=False)
# Add the Stopwatch Menu to the MenuBar
MenuBar.add_cascade(label="Stopwatch", menu=StopwatchMenu)
StopwatchMenu.add_command(label="Start Stopwatch", command=StartStopwatchFunc)
StopwatchMenu.add_separator()
StopwatchMenu.add_command(label="Stop Stopwatch", command=StopStopwatchFunc)
StopwatchMenu.add_separator()
StopwatchMenu.add_command(label="Reset Stopwatch", command=ResetStopwatchFunc)


# Timer Menu
TimerMenu = Menu(MenuBar, tearoff=False)
# Add the Timer Menu to the MenuBar
MenuBar.add_cascade(label="Timer", menu=TimerMenu)
TimerMenu.add_command(label="Start Timer", command=StartTimerFunc)
TimerMenu.add_separator()
TimerMenu.add_command(label="Stop Timer", command=StopTimerFunc)
TimerMenu.add_separator()
TimerMenu.add_command(label="Reset Timer", command=ResetTimerFunc)


# Help Menu
HelpMenu = Menu(MenuBar, tearoff=False)
# Add the Help Menu to the MenuBar
MenuBar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="Documentation", command=DocumentationFunc)
HelpMenu.add_command(label="Release Notes", command=ReleaseNotesFunc)
HelpMenu.add_separator()
HelpMenu.add_command(label="About", command=AboutScreenFunc)



# Word And Character Count
InitWordCount()


# Initialize Screen
root.mainloop()
