# CMPT 1105 | GUI Starter Pack

```python
from tkinter import *

class GUI:
        def __init__(this):
            this.myWindow = Tk()
            mainloop()

gui = GUI()
```
`------------------------`
```python
from tkinter import *

class GUI:
        def __init__(this):
            this.window = Tk()

            this.label = Label(this.window, text="Hello World")
            this.label.place(x=20,y=20)
            
            mainloop()

gui = GUI()
```
`------------------------`
```python
from tkinter import *

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("500x300+200+100")
            
            this.label = Label(this.window, text="Hello World")
            this.label.place(x=100,y=100)
            
            mainloop()

gui = GUI()
```
`------------------------`
```python
from tkinter import *

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("500x300+200+100")

            # Frame A
            this.frameA = Frame(this.window, width=280, height=140, bg="yellow")
            this.frameA.place(x=10,y=10)

            # Frame B
            this.frameB = Frame(this.window, width=280, height=140, bg="green")
            this.frameB.place(x=10,y=150)
            
            this.label = Label(this.window, text="Hello World", bg="green")
            this.label.place(x=100,y=100)
            
            mainloop()

gui = GUI()
```
`------------------------`
```python
from tkinter import *

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("500x300+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=280, height=140, bg="yellow")
            this.frameA.place(x=10,y=10)

            # Frame B
            this.frameB = Frame(this.window, width=280, height=140, bg="green")
            this.frameB.place(x=10,y=150)
            
            this.label = Label(this.window, text="Hello World", bg="green")
            this.label.place(x=100,y=100)
            
            mainloop()

gui = GUI()
```
`------------------------`
```python
from tkinter import *

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("500x300+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=280, height=140, bg="yellow")
            this.frameA.place(x=10,y=10)
            
            this.label = Label(this.window, text="Hello World", bg="green", fg="green", font=("Arial", 16))
            this.label.place(x=20,y=20)

            this.button = Button(this.frameA, text="Click", bg="red", fg="blue", font=("Arial", 16))
            this.button.place(x=20, y=50)
            
            mainloop()

gui = GUI()
```
`------------------------`
```python
from tkinter import *

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("500x300+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=280, height=140, bg="yellow")
            this.frameA.place(x=10,y=10)
            
            this.label = Label(this.window, text="Hello World", bg="green", fg="green", font=("Arial", 16))
            this.label.place(x=20,y=20)

            this.button = Button(this.frameA, text="Click", bg="red", fg="blue", font=("Arial", 16), command=this.functionA)
            this.button.place(x=20, y=50)
            
            mainloop()

        def functionA (this):
                print("Clicked...")
                
gui = GUI()
```
`------------------------`
```python
from tkinter import *
import tkinter.messagebox

class GUI:
        def __init__(this):
            this.window = Tk()

            # Determine the size and location of the main window
            this.window.geometry("500x300+200+100")

            # Windows title
            this.window.title("Douglas College")

            # Frame A
            this.frameA = Frame(this.window, width=280, height=140, bg="yellow")
            this.frameA.place(x=10,y=10)
            
            this.label = Label(this.window, text="Hello World", bg="green", fg="green", font=("Arial", 16))
            this.label.place(x=20,y=20)

            this.button = Button(this.frameA, text="Click", font=("Arial", 16), command=this.functionA)
            this.button.place(x=20, y=50)

            this.exitButton = Button(this.frameA, text="Exit", font=("Arial", 16), command=this.window.destroy)
            this.exitButton.place(x=20, y=100)
            
            mainloop()

        def functionA (this):
                tkinter.messagebox.showinfo("Response", "Clicked...")
                
gui = GUI()
```
`------------------------`

GUI - Capital Cities
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
            this.frameA = Frame(this.window, width=280, height=300, bg="green")
            this.frameA.place(x=10,y=10)
            
            this.label = Label(this.window, text="Hello World", bg="red", fg="white", font=("Capital Cities", 16))
            this.label.place(x=20,y=20)

            this.countryAButton = Button(this.frameA, text="Canada", font=("Arial", 16), command=this.canadaCapitalCity)
            this.countryAButton.place(x=10, y=50)

            this.countryBButton = Button(this.frameA, text="United State of America", font=("Arial", 16), command=this.usCapitalCity)
            this.countryBButton.place(x=10, y=100)

            this.countryCButton = Button(this.frameA, text="England", font=("Arial", 16), command=this.englandCapitalCity)
            this.countryCButton.place(x=10, y=150)

            this.exitButton = Button(this.frameA, text="Exit", font=("Arial", 16), command=this.window.destroy)
            this.exitButton.place(x=10, y=200)
            
            mainloop()

        def canadaCapitalCity (this):
                tkinter.messagebox.showinfo("Response", "Ottawa")

        def usCapitalCity (this):
                tkinter.messagebox.showinfo("Response", "Washinton, D.C.")

        def englandCapitalCity (this):
                tkinter.messagebox.showinfo("Response", "London")
                
gui = GUI()
```
`------------------------`
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
            this.frameA = Frame(this.window, width=280, height=300, bg="green")
            this.frameA.place(x=10,y=10)
            
            this.label = Label(this.window, text="Hello World", bg="red", fg="white", font=("Capital Cities", 16))
            this.label.place(x=20,y=20)

            this.entry = Entry(this.frameA, width=20, font=16)
            this.entry.place(x=10, y= 100)

            this.clickButton = Button(this.frameA, text="Click", font=("Arial", 16), command=this.entryInput)
            this.clickButton.place(x=10, y=150)
            
            this.exitButton = Button(this.frameA, text="Exit", font=("Arial", 16), command=this.window.destroy)
            this.exitButton.place(x=10, y=200)
            
            mainloop()

        def entryInput (this):
                text = this.entry.get()
                tkinter.messagebox.showinfo("Response", "You have entered " + text)
                
gui = GUI()
```
`------------------------`
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
            this.frameA = Frame(this.window, width=280, height=300, bg="green")
            this.frameA.place(x=10,y=10)
            
            this.label = Label(this.window, text="Hello World", bg="red", fg="white", font=("Capital Cities", 16))
            this.label.place(x=20,y=20)

            this.entry = Entry(this.frameA, width=20, font=16)
            this.entry.place(x=10, y= 100)

            this.enteredText = StringVar()
            this.enteredLabel = Label(this.frameA, textvariable=this.enteredText, font=16)
            this.enteredLabel.place(x=80, y= 150)

            this.clickButton = Button(this.frameA, text="Click", font=("Arial", 16), command=this.entryInput)
            this.clickButton.place(x=10, y=150)
            
            this.exitButton = Button(this.frameA, text="Exit", font=("Arial", 16), command=this.window.destroy)
            this.exitButton.place(x=10, y=200)
            
            mainloop()

        def entryInput (this):
                text = this.entry.get()
                this.enteredText.set(text)
                tkinter.messagebox.showinfo("Response", "You have entered " + text)
                
gui = GUI()
```

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
            this.frameA = Frame(this.window, width=280, height=300, bg="green")
            this.frameA.place(x=10,y=10)


           # Choice
            this.choice = StringVar()
            this.choice.set("Tea")

            this.teaRadio = Radiobutton(this.frameA, text="Tea", font=14, variable=this.choice, value="Tea")
            this.teaRadio.place(x=10, y=40)

            this.coffeeRadio = Radiobutton(this.frameA, text="Coffee", font=14, variable=this.choice, value="Coffee")
            this.coffeeRadio.place(x=10, y=75)

            this.hotChocolateRadio = Radiobutton(this.frameA, text="Hot Chocolate", font=14, variable=this.choice, value="Hot Chocolate")
            this.hotChocolateRadio.place(x=10, y=110)
           
            this.clickButton = Button(this.frameA, text="OK", font=("Arial", 16), command=this.selection)
            this.clickButton.place(x=10, y=150)

            this.exitButton = Button(this.frameA, text="Exit", font=("Arial", 16), command=this.window.destroy)
            this.exitButton.place(x=10, y=200)

            mainloop()

        def selection (this):
                message = "You like " + this.choice.get()
                tkinter.messagebox.showinfo("Selection ", message)

gui = GUI()
```

@credit goes to Anmol from our Discord group.
```python
from tkinter import *
import tkinter.messagebox
class myGUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("300x300+100+100")
        self.main_window.title("Douglas College")
        self.frame1 = Frame(self.main_window, width = 280, height = 240 )
        self.frame1.place(x = 10, y = 10)
        self.choice1 = IntVar()
        self.choice2 = IntVar()
        self.choice3 = IntVar()
        self.choice4 = IntVar()
        
        self.choice1.set(0)
        self.choice2.set(0)
        self.choice3.set(0)
        self.choice4.set(0)
        
        self.cb1 = Checkbutton(self.frame1,text="Oil Change - $35",font=14,
                               variable=self.choice1)
        self.cb1.place(x=40,y=40)

        self.cb2 = Checkbutton(self.frame1,text="Inspection - $50",font=14,
                               variable=self.choice2)
        self.cb2.place(x=40,y=75)

        self.cb3 = Checkbutton(self.frame1,text="Muffler Replacement - $100",font=14,
                               variable=self.choice3)
        self.cb3.place(x=40,y=110)

        self.cb4 = Checkbutton(self.frame1,text="Tire Rotation- $20",font=14,
                               variable=self.choice4)
        self.cb4.place(x=40,y=145)

        self.clickButton = Button(self.frame1, text="Total", font=("Arial", 16), command=self.do_this)
        self.clickButton.place(x=10, y=180)
        mainloop()
    def do_this(self):
        total = 0
        if self.choice1.get():
            total += 35
            
        if self.choice2.get():
            total += 50
              
        if self.choice3.get():
            total += 100
            
        if self.choice4.get():
            total += 20

        tkinter.messagebox.showinfo("Response", "Your Total is:$ " + str(total))
                
my_gui = myGUI()
```


