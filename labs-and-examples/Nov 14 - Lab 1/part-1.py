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
