from tkinter import *
import tkinter.messagebox

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("300x120+200+100")

            # Windows title
            this.window.title("Conversion")

            # Frame A
            this.frameA = Frame(this.window, width=280, height=300)
            this.frameA.place(x=10,y=10)

            # Pounds Label
            this.poundsLabel = Label(this.frameA, text="Pounds")
            this.poundsLabel.place(x=10, y=10)

            # Pounds Input
            this.poundsInput = Entry(this.frameA, width=20, font=16)
            this.poundsInput.place(x=80, y= 10)

            # Convert to gram button
            this.clickButton = Button(this.frameA, text="Convert to Grams", command=this.convert)
            this.clickButton.place(x=10, y=40)

            # Exit button
            this.exitButton = Button(this.frameA, text="Exit", command=this.window.destroy)
            this.exitButton.place(x=120, y=40)

            mainloop()

        # Convert function
        def convert (this):
                pounds = float(this.poundsInput.get())
                poundsToGram = pounds * 454

                message = str(pounds) + " pounds" + " = " + format(poundsToGram, "0.1f") + " grams"
                tkinter.messagebox.showinfo("Pounds to Grams ", message)

gui = GUI()
