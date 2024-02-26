#This is a beginning project, of a trial-and-error nature (but isn't all coding?), to build a system that sends, 
#at a set daily interval, presumably early in the morning, information that would be useful for the rest of the day
#for example: weather, tasks to do, traffic conditions on the way to a set destination, a motivational quote, and so on.
#It could also be made to open up daily programs and websites that are frequently used, although on this I'm not definitively set.
#The end goal is to have a GUI in which to set what can be customised.

#task one: set up GUI in which email address can be entered

import tkinter #for the GUI
import email #self-explanatory

#root>

root = tkinter.Tk()
root.geometry("630x500")
root.title("Emailinator")
root.iconname()

#frames>

programFrame1 = tkinter.LabelFrame(root)
programFrame1.grid(row=0, column=0)

programFrame2 = tkinter.LabelFrame(root)
programFrame2.grid(row=1, column=0)

#widgets>

#frame1
l1 = tkinter.Label(programFrame1, font="helvetica, 12", text="Please enter email address: ")
emailInput = tkinter.Entry(programFrame1, font="helvetica", relief="sunken", width=50, borderwidth=5)

#frame2
confirmEmailInput = tkinter.Entry(programFrame2, font="helvetica", relief="sunken", width=50, borderwidth=5)
l2 = tkinter.Label(programFrame2, font="helvetica, 12", text="Re-enter email address: ")


#Layout>

#frame1
emailInput.grid(row=0, column=1, padx=10, pady=10,)
l1.grid(row=0, column=0)

#frame2
confirmEmailInput.grid(row=0, column=1, padx=12, pady=10,)
l2.grid(row=0, column=0, padx=12)



root.mainloop()