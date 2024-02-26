#This is a beginning project, of a trial-and-error nature (but isn't all coding?), to build a system that sends, 
#at a set daily interval, presumably early in the morning, information that would be useful for the rest of the day
#for example: weather, tasks to do, traffic conditions on the way to a set destination, a motivational quote, and so on.
#It could also be made to open up daily programs and websites that are frequently used, although on this I'm not definitively set.
#The end goal is to have a GUI in which to set what can be customised.

#task one: set up GUI in which email address can be entered

import tkinter #for the GUI
import email #self-explanatory

#root

root = tkinter.Tk()
root.geometry("500x500")
root.title("Emailinator")
root.iconname()

#frames

programFrame1 = tkinter.LabelFrame(root)
programFrame1.grid(row=0, column=0)

#widgets

l1 = tkinter.Label(programFrame1, text="Please enter email address")

emailInput = tkinter.Entry(programFrame1, text="email", width=50, borderwidth=5)

#Layout

emailInput.grid(row=0, column=1, padx=10, pady=10)
l1.grid(row=0, column=0)




root.mainloop()