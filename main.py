'''File which should run uninterrupted in order to check conditions, email, and so forth.
This is my first real project so the code will be far from perfect, but as long as it works and provides a learning experience, it has done its job.'''

import json
import os
import time
import sys
import datetime
import email
import smtplib
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler #blockingscheduler waits at .start(), backgroundscheduler continues past it
from env import SMTPinfoE, SMTPinfoK, SMTPinfoP, SMTPinfoS

def main():
    if os.path.isfile("inputs.json"):
        print ("Configuration found")
        with open("inputs.json", "r") as f:
                try:
                    data = json.load(f)
                    global emailaddress
                    emailaddress = data["email_address"] 
                    timeH = data["hour"]
                    timeM = data["minutes"] #Extract settings from the JSON, assign them to variables
                    setTime = datetime.time(timeH, timeM) #Convert integers to a time.
                
                    print(f"The set email address is {emailaddress}")
                    print(f"The chosen time is {setTime}")

                    scheduler = BlockingScheduler()

                    job_1 = scheduler.add_job(emailClient, "cron", hour = timeH , minute=timeM )
                    scheduler.start()

                except json.JSONDecodeError:
                    print ("Configuration file exists, but is not complete. Please relaunch config.py and complete all fields")
                    time.sleep(10)
                    sys.exit()
    else:
        print("This program cannot run without having first been configured. Please run config.py")
        time.sleep(10)


def consolidation():
     pass
     


def emailClient():
    conn = smtplib.SMTP(SMTPinfoS, SMTPinfoP)

    conn.ehlo()

    conn.starttls()

    conn.login(SMTPinfoE, SMTPinfoK)

    conn.sendmail(SMTPinfoE, emailaddress, "Subject: testing testing 1 2 3 \n\nThis is a Python test.\n\n")

    print("Email sent")
    time.sleep(20)

    conn.quit()

main()