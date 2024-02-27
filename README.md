A foray into practical applications of Python, learning along the way. 

This project is a self-organisation tool which emails at a customisable time each day, presumably the morning, with relevant information, such as weather, motivational quotes,
single-time tasks, reccurent tasks, and future tasks. It will include a GUI for ease of use.



----------------------------
## Screenshots of application at this stage
<sub>_Graphics design is my passion_ :shipit: : </sub>

![image](https://github.com/itssojoever/Emailinator/assets/144183809/ecf0343c-3e93-46ef-bf48-f539ede9e64d)

<sub> _always helpful_ : </sub> 

![image](https://github.com/itssojoever/Emailinator/assets/144183809/e1f2ca77-1903-4882-9f48-598600e10e43)

<sub>Feedback in the CLI : </sub>

![image](https://github.com/itssojoever/Emailinator/assets/144183809/cf5c5a9e-4612-4586-854a-de57bf7a6bfc)

<sub>The email is received rapidly. Unfortunately I forgot to rstrip the whitespace after the input, which is a future improvement to be made : </sub>

![image](https://github.com/itssojoever/Emailinator/assets/144183809/76decf8c-e7d3-4da8-90d5-58dec0ee02a7)

----------------------------
## Functionality

The program works. It takes two email addresses, verifies that they match, takes a given time, and accepts text into two text boxes placed instead the above tabs. Upon saving, this information is assigned to variables and the program then subsequently creates a JSON file and writes the information assigned to the variables to it. The use of if/else statements allows for the user to be kept informed of if the program has worked or not, whilst a try except json.JSONDecodeError statements skirts around the problem created at first initialisation where the JSON file is created but not populated with key value pairs. I'm sure there's a better way to write this part of the code but as a learning experience with the application designed for just my use, it's okay for the time being, but I intend to rewrite this.

With respect to main.py, the code which reads the JSON file, converts the time integers into a datetime, creates a connection to an email API, and uses APScheduler to send an email at a specified time; I am happy that this code works well. I think there are improvements to be made with respect to the length of the program, there are likely areas that would be redundant if programmed in a more concise manner, but for the time being, as a learning experience, it works well. At present main.py is ran in a python terminal on my computer, but if the program is expanded further and has a practical application to myself, then I envisage to look into how to host it in a more stable manner

-----------------------------
## Improvements?

At the moment it's relatively barebones. While it does what I intended it to do, it's missing a lot of functions I'd like to add, and it certainly wouldn't win any prizes for interface design. Future improvements, then, would be focused on adding more functions to it, moving it onto a dedicated server to avoid the instability of running it on my personal laptop (would need higher uptime %), improving the design, and tidying up the code.

-----------------------------
## Conclusion

As a personal project to apply what I've learnt to a usable application with real-world use, I'm very satisfied with it. In the process of coding it I've learnt more about TKinter, smtplib, APSscheduler, JSON, and Python in general. With the intended addition of further features, the tidying up of the design, and the potential to deploy it on a dedicated server there is much more that can be learnt from coding this simple program
