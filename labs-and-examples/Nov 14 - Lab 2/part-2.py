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
