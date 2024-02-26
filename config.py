#This is a beginning project, of a trial-and-error nature (but isn't all coding?), to build a system that sends, 
#at a set daily interval, presumably early in the morning, information that would be useful for the rest of the day
#for example: weather, tasks to do, traffic conditions on the way to a set destination, a motivational quote, and so on.
#It could also be made to open up daily programs and websites that are frequently used, although on this I'm not definitively set.
#The end goal is to have a GUI in which to set what can be customised.

#task one: set up GUI in which email address can be entered

import tkinter #for the GUI
import email #self-explanatory
from tkinter import messagebox #for throwing up messages
import json
import os

#root>

root = tkinter.Tk()
root.geometry("630x500")
root.title("Emailinator")
root.iconname()

#functions>

def loadData():
        if os.path.isfile("inputs.json"):
            print("JSON file found")
            with open("inputs.json", mode="r") as f:
                try:
                    data = json.load(f)
                    emailInput.insert(0, data["email_address"].capitalize())
                    confirmEmailInput.insert(0, data["email_address"].capitalize())
                    chosenTimeHourInput.delete(0, tkinter.END)
                    chosenTimeHourInput.insert(0, int(data["hour"]))
                    chosenTimeMinuteInput.delete(0, tkinter.END)
                    chosenTimeMinuteInput.insert(0, int(data["minutes"]))
                except json.JSONDecodeError:
                    print("JSON file exists but is empty. It will be populated later")
        else:
            print("No JSON file found, creating file")
            with open ("inputs.json", "w") as f:
                pass

def saveData():
    givenEmail = emailInput.get().upper().strip()
    givenEmail2 = confirmEmailInput.get().upper().strip()
    givenTimeH = int(chosenTimeHourInput.get())
    giventimeM = int(chosenTimeMinuteInput.get())

    information = {}
    information["email_address"] = givenEmail
    information["hour"] = givenTimeH
    information["minutes"] = giventimeM
    with open("inputs.json", "w") as f:
        json.dump(information, f)

    emailInput.delete(0, tkinter.END)
    confirmEmailInput.delete(0, tkinter.END)
    chosenTimeHourInput.delete(0, tkinter.END)
    chosenTimeMinuteInput.delete(0, tkinter.END)

#frames>

programFrame1 = tkinter.LabelFrame(root)
programFrame1.grid(row=0, column=0)

programFrame2 = tkinter.LabelFrame(root)
programFrame2.grid(row=1, column=0)

programFrame3 = tkinter.LabelFrame(root)
programFrame3.grid(row=2, column=0)

programFrame4 = tkinter.LabelFrame(root)
programFrame4.grid(row=3, column=0)

#widgets>

#frame1
l1 = tkinter.Label(programFrame1, font="helvetica, 12", text="Please enter email address: ")
emailInput = tkinter.Entry(programFrame1, font="helvetica", relief="sunken", width=50, borderwidth=5)

#frame2
confirmEmailInput = tkinter.Entry(programFrame2, font="helvetica", relief="sunken", width=50, borderwidth=5)
l2 = tkinter.Label(programFrame2, font="helvetica, 12", text="Re-enter email address: ")

#frame3
chosenTimeHourInput = tkinter.Spinbox(programFrame3, from_=0, to=24)
chosenTimeMinuteInput = tkinter.Spinbox(programFrame3, from_=0, to=59)
l3 = tkinter.Label(programFrame3, font="helvetica, 12", text="Select time to receive email.")
l4 = tkinter.Label(programFrame3, font="helvetica, 12", text="Hour:")
l5 = tkinter.Label(programFrame3, font="helvetica, 12", text="Minute: ")

#frame4
submitButton = tkinter.Button(programFrame4, text="Save settings", command=lambda: saveData())


#Layout>

#frame1
emailInput.grid(row=0, column=1, padx=10, pady=10,)
l1.grid(row=0, column=0)

#frame2
confirmEmailInput.grid(row=0, column=1, padx=12, pady=10,)
l2.grid(row=0, column=0, padx=12)

#frame3
chosenTimeHourInput.grid(row=0, column=2, padx=53)
chosenTimeMinuteInput.grid(row=0, column=4, padx=53, pady=10)
l3.grid(row=0, column=0)
l4.grid(row=0, column=1)
l5.grid(row=0, column=3)

#frame4
submitButton.grid(row=0, column=0, padx=12)

loadData()

root.mainloop()