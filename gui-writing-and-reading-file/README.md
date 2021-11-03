# CMPT 1105 Python Writing And Reading File GUI

## Lab A
Writing to a file.
```python
from tkinter import *
import tkinter.messagebox

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("600x400+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=480, height=300)
            this.frameA.place(x=10,y=10)

            # File Name
            this.fileNameLabel = Label(this.window, text="File Name", font=("Arial", 14))
            this.fileNameLabel.place(x=20,y=20)

            this.fileNameEntry = Entry(this.frameA, width=20, font=16)
            this.fileNameEntry.place(x=120, y= 10)
            ###

            # Scientist A
            this.scientistALabel = Label(this.window, text="Scientist A", font=("Arial", 14))
            this.scientistALabel.place(x=20,y=60)

            this.scientistAEntry = Entry(this.frameA, width=20, font=16)
            this.scientistAEntry.place(x=120, y=50)
            ###

            # Scientist B
            this.scientistBLabel = Label(this.window, text="Scientist B", font=("Arial", 14))
            this.scientistBLabel.place(x=20,y=100)

            this.scientistBEntry = Entry(this.frameA, width=20, font=16)
            this.scientistBEntry.place(x=120, y=90)
            ###

            # Scientist C
            this.scientistCLabel = Label(this.window, text="Scientist C", font=("Arial", 14))
            this.scientistCLabel.place(x=20,y=140)

            this.scientistCEntry = Entry(this.frameA, width=20, font=16)
            this.scientistCEntry.place(x=120, y=130)
            ###

            # Scientist D
            this.scientistDLabel = Label(this.window, text="Scientist D", font=("Arial", 14))
            this.scientistDLabel.place(x=20,y=180)

            this.scientistDEntry = Entry(this.frameA, width=20, font=16)
            this.scientistDEntry.place(x=120, y=170)
            ###

            # Save Button
            this.saveButton = Button(this.frameA, text="Save", font=("Arial", 14), command=this.saveFile)
            this.saveButton.place(x=10, y=210)
            
            mainloop()

        def saveFile (this):
                directory = 'C:\\temp\\';
                fileToSave = open(directory + this.fileNameEntry.get(), 'w')
                fileToSave.write(this.scientistAEntry.get() + '\n')
                fileToSave.write(this.scientistBEntry.get() + '\n')
                fileToSave.write(this.scientistCEntry.get() + '\n')
                fileToSave.write(this.scientistDEntry.get() + '\n')
                fileToSave.close()
                
                tkinter.messagebox.showinfo("Save", "The file: " + this.fileNameEntry.get() + "is saved to: " + directory)             
gui = GUI()
```

Reading
```python
from tkinter import *
import tkinter.messagebox

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("600x400+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=480, height=300)
            this.frameA.place(x=10,y=10)

            # File Name
            this.fileNameLabel = Label(this.window, text="File Name", font=("Arial", 14))
            this.fileNameLabel.place(x=20,y=20)

            this.fileNameEntry = Entry(this.frameA, width=20, font=16)
            this.fileNameEntry.place(x=120, y= 10)
            ###

            # Ouput Label
            this.outputText = StringVar()
            
            this.outputLabel = Label(this.window, textvariable=this.outputText, font=("Arial", 14))
            this.outputLabel.place(x=20,y=60)
            ###

            # Read Button
            this.readButton = Button(this.frameA, text="Read", font=("Arial", 14), command=this.readFile)
            this.readButton.place(x=350, y=0)
            
            mainloop()

        def readFile (this):
                directory = 'C:\\temp\\';
                fileToRead = open(directory + this.fileNameEntry.get(), 'r')
                content = fileToRead.read();
                fileToRead.close()

                this.outputText.set(content)
                
                
gui = GUI()
```

## Lab B
Reading
```python
from tkinter import *
import tkinter.messagebox

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("600x400+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=480, height=300)
            this.frameA.place(x=10,y=10)

            # File Name
            this.fileNameLabel = Label(this.window, text="File Name", font=("Arial", 14))
            this.fileNameLabel.place(x=20,y=20)

            this.fileNameEntry = Entry(this.frameA, width=20, font=16)
            this.fileNameEntry.place(x=120, y= 10)
            ###

            # Name A
            this.nameALabel = Label(this.window, text="Name A", font=("Arial", 14))
            this.nameALabel.place(x=20,y=60)

            this.nameAEntry = Entry(this.frameA, width=20, font=16)
            this.nameAEntry.place(x=120, y=50)
            ###

            # Birthday A
            this.birthdayALabel = Label(this.window, text="Birthday A", font=("Arial", 14))
            this.birthdayALabel.place(x=20,y=100)

            this.birthdayAEntry = Entry(this.frameA, width=20, font=16)
            this.birthdayAEntry.place(x=120, y=90)
            ###

            # Name B
            this.nameBLabel = Label(this.window, text="Name B", font=("Arial", 14))
            this.nameBLabel.place(x=20,y=140)

            this.nameBEntry = Entry(this.frameA, width=20, font=16)
            this.nameBEntry.place(x=120, y=130)
            ###

            # Birthday B
            this.birthdayBLabel = Label(this.window, text="Birthday B", font=("Arial", 14))
            this.birthdayBLabel.place(x=20,y=180)

            this.birthdayBEntry = Entry(this.frameA, width=20, font=16)
            this.birthdayBEntry.place(x=120, y=170)
            ###

            # Save Button
            this.saveButton = Button(this.frameA, text="Save", font=("Arial", 14), command=this.saveFile)
            this.saveButton.place(x=10, y=210)
            
            mainloop()

        def saveFile (this):
                directory = 'C:\\temp\\';
                fileToSave = open(directory + this.fileNameEntry.get(), 'w')
                fileToSave.write(this.nameAEntry.get() + '\n')
                fileToSave.write(this.birthdayAEntry.get() + '\n')
                fileToSave.write(this.nameBEntry.get() + '\n')
                fileToSave.write(this.birthdayBEntry.get() + '\n')
                fileToSave.close()
                
                tkinter.messagebox.showinfo("Save", "The file: " + this.fileNameEntry.get() + " is saved to: " + directory)
                
gui = GUI()
```

Writing
```python
from tkinter import *
import tkinter.messagebox

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("600x400+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=480, height=300)
            this.frameA.place(x=10,y=10)

            # File Name
            this.fileNameLabel = Label(this.window, text="File Name", font=("Arial", 14))
            this.fileNameLabel.place(x=20,y=20)

            this.fileNameEntry = Entry(this.frameA, width=20, font=16)
            this.fileNameEntry.place(x=120, y= 10)
            ###

            # Ouput Label
            this.outputText = StringVar()
            
            this.outputLabel = Label(this.window, textvariable=this.outputText, font=("Arial", 14))
            this.outputLabel.place(x=20,y=60)
            ###

            # Read Button
            this.readButton = Button(this.frameA, text="Read", font=("Arial", 14), command=this.readFile)
            this.readButton.place(x=350, y=0)
            
            mainloop()

        def readFile (this):
                directory = 'C:\\temp\\';
                fileToRead = open(directory + this.fileNameEntry.get(), 'r')
                nameA = fileToRead.readline().rstrip()
                birthdayA = fileToRead.readline().rstrip()
                nameB = fileToRead.readline().rstrip()
                birthdayB = fileToRead.readline().rstrip()

                ageA = 2020 - int(birthdayA)
                ageB = 2020 - int(birthdayB)

                content = nameA + ' is ' + str(ageA) + ' years old.' + '\n' + str(nameB) + ' is ' + str(ageB) + ' years old'
                this.outputText.set(content)
                fileToRead.close()
                
                
gui = GUI()
```
