from tkinter import *

root = Tk()
root.geometry('500x600')
root.title("Navbar Tutorial")
root.configure(bg='#555555')

nav_frame = Frame(root,
                bg='#158aff',
                highlightbackground='white',
                highlightthickness=1)

toggle_btn = Button(
    nav_frame, 
    text='≣', 
    bg='#158aff', 
    fg='white',
    font=('Bold', 20)
    )

nav_frame.pack(side = TOP, fill=X)
nav_frame.pack_propagate(False)
nav_frame.configure(height=50)

# Widgets
#--------

home_label = Label(
    nav_frame,
    text='Home',
    bg = '#158aff',
    fg='white'
    )

contact_label = Label(
    nav_frame,
    text='Contact',
    bg = '#158aff',
    fg='white'
    )

about_label = Label(
    nav_frame,
    text='About',
    bg = '#158aff',
    fg='white'
    )

hash_label = Label(
    nav_frame,
    text='#',
    bg = '#158aff',
    fg='white'
    )

null_label = Label(
    nav_frame,
    text='Null',
    bg = '#158aff',
    fg='white'
    )

# Placing 

home_label.grid(row = 1, column = 0,columnspan = 1)

contact_label.grid(row = 2, column = 0)

about_label.grid(row = 3, column = 0)

hash_label.grid(row = 4, column = 0)

null_label.grid(row = 5, column = 0)



root.mainloop()
