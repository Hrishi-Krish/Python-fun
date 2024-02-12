from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login Form")
window.geometry('500x400') # width and height default is 340x440
window.configure(bg = "#333333") # bg obviously stands for background color 

frame = Frame(bg = "#333333")

def Login():
    username = "Hrishikesh"
    password = "Hrishi"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Success", message="User Logged in Successfully")
    else:
        messagebox.showerror(title="Error", message="Wrong Username or Password")



'''

Styling
-------


Styling the widgets are done while creating, that is to say, if you have to edit some widget's attributes, look for 
where it is defined. 

bg = background color
fg = foreground color
Special note that foreground also controls the color of the text in cases of labels
pady = padding on y axis
padx = padding on x axis


'''


# Creating Widgets
#------------------

'''

Label is just a text or name
Entry is a textbox that allows the user to enter things
Button is button 

'''

login_label = Label( 
    frame,
    text='Login', 
    bg = "#333333", 
    fg='#ff3399', 
    font=("Arial", 30)
    ) 

username_label = Label(
    frame, 
    text= 'Username: ', 
    bg = "#333333", 
    fg='#ffffff',
    font=("Arial", 16)
    ) 

password_label = Label(
    frame,
    text= 'Password: ', 
    bg = "#333333", 
    fg='#ffffff',
    font=("Arial", 16)
    )

username_entry = Entry( 
    frame,
    font=('Arial', 16)
    ) 

password_entry = Entry(
    frame, 
    show = '*',
    font=('Arial', 16)
    )

login_button = Button( 
    frame, 
    text='Login', 
    bg='#ff3399', 
    fg='#ffffff',
    font=('Arial', 16),
    command=Login
    ) 



# Placing widgets on the screen
#------------------------------
'''
There are three ways to place widgets -> place, pack and grid.
We'll be using grid here and these are the ways to use grid


rowspan defines how many rows the label covers
columnspan 2 means it covers 2 columns worth of space
padx and pady only need to be done once for the entire row

'''

login_label.grid( 
    row=0, 
    column=0, 
    columnspan=2, 
    sticky='news',
    padx=40,
    pady=40
    ) 

username_label.grid(
    row=1, 
    column=0,
    padx=40,
    pady=10
    )

username_entry.grid(
    row=1, 
    column=1
    )

password_label.grid(
    row=2,
    column=0,
    padx=40,
    pady=10
    )

password_entry.grid(
    row=2, 
    column=1
    )

login_button.grid(
    row=3,
    column=0, 
    columnspan=2,
    padx=5,
    pady=30
    ) 

frame.pack()

window.mainloop() # infinite loop that runs until the app is closed --> This is in fact a loop
