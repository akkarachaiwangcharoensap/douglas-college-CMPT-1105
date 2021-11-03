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
