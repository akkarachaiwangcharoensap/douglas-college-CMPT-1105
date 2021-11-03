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

            # Monday
            this.mondayLabel = Label(this.window, text="Monday", font=("Arial", 14))
            this.mondayLabel.place(x=20,y=20)

            this.mondayEntry = Entry(this.frameA, width=20, font=16)
            this.mondayEntry.place(x=120, y= 10)
            ###

            # Tuesday
            this.tuesdayLabel = Label(this.window, text="Tuesday", font=("Arial", 14))
            this.tuesdayLabel.place(x=20,y=60)

            this.tuesdayEntry = Entry(this.frameA, width=20, font=16)
            this.tuesdayEntry.place(x=120, y=50)
            ###

            # Wednesday
            this.wednesdayLabel = Label(this.window, text="Wednesday", font=("Arial", 14))
            this.wednesdayLabel.place(x=20,y=100)

            this.wednesdayEntry = Entry(this.frameA, width=20, font=16)
            this.wednesdayEntry.place(x=120, y=90)
            ###

            # Thursday
            this.thursdayLabel = Label(this.window, text="Thursday", font=("Arial", 14))
            this.thursdayLabel.place(x=20,y=140)

            this.thursdayEntry = Entry(this.frameA, width=20, font=16)
            this.thursdayEntry.place(x=120, y=130)
            ###

            # Friday
            this.fridayLabel = Label(this.window, text="Friday", font=("Arial", 14))
            this.fridayLabel.place(x=20,y=180)

            this.fridayEntry = Entry(this.frameA, width=20, font=16)
            this.fridayEntry.place(x=120, y=170)
            ###

            # Calculate Button
            this.calculateButton = Button(this.frameA, text="Calculate", font=("Arial", 14), command=this.calculate)
            this.calculateButton.place(x=10, y=210)

            # Quit Button
            this.quitButton = Button(this.frameA, text="Quit", font=("Arial", 14), command=this.window.destroy)
            this.quitButton.place(x=120, y=210)
            
            mainloop()

        def calculate (this):
                monday = this.mondayEntry.get()
                tuesday = this.tuesdayEntry.get()
                wednesday = this.wednesdayEntry.get()
                thursday = this.thursdayEntry.get()
                friday = this.fridayEntry.get();

                weekday = [monday, tuesday, wednesday, thursday, friday]

                total = 0
                for day in weekday:
                        total = total + float(day)

                tkinter.messagebox.showinfo("Total Sales", "Total sales is " + "$" + format(total, '0.1f'))
                
gui = GUI()
