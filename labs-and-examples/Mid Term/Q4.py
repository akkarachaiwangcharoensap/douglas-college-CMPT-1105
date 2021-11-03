from tkinter import *
import tkinter.messagebox

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("400x120+200+100")

            # Windows title
            this.window.title("Latin To English")

            # Frame A
            this.frameA = Frame(this.window, width=400, height=200)
            this.frameA.place(x=10,y=10)

            # Sinister button
            this.sinisterButton = Button(this.frameA, text="Sinister", font=("Arial", 14), command=this.sinisterToEnglish)
            this.sinisterButton.place(x=10, y=20)

            # Dexter button
            this.dexterButton = Button(this.frameA, text="Dexter", font=("Arial", 14), command=this.dexterToEnglish)
            this.dexterButton.place(x=100, y=20)

            # Medium button
            this.mediumButton = Button(this.frameA, text="Medium", font=("Arial", 14), command=this.mediumToEnglish)
            this.mediumButton.place(x=180, y=20)

            # Exit button
            this.exitButton = Button(this.frameA, text="Exit", font=("Arial", 14), command=this.window.destroy)
            this.exitButton.place(x=270, y=20)

            mainloop()

        # Sinister translation function
        def sinisterToEnglish (this):
                message = "In English, it means: Left"
                tkinter.messagebox.showinfo("Latin To English ", message)

        # Dexter translation function
        def dexterToEnglish (this):
                message = "In English, it means: Right"
                tkinter.messagebox.showinfo("Latin To English ", message)

        # Medium translation function
        def mediumToEnglish (this):
                message = "In English, it means: Center"
                tkinter.messagebox.showinfo("Latin To English ", message)

gui = GUI()
