# converting random numbers into ASCII for Password
# without space etc. so everything before ASCII 32
# and 126 DEL is left out


# GUI toolkit
from tkinter import *
from tkinter import messagebox

# needed for random numbers
from random import randint

# GUI
root = Tk()
root.title('Strong Password Generator')
root.geometry("500x300")


# generate new random password
def new_rand():
    # pass statement to construct a body that does nothing
    # pass

    # clear Entry Box
    pass_entry.delete(0, END)

    # Get Password length coverted to int
    pass_length = int(length_entry.get())

    # variable for password
    var_pass = ''

    if int(length_entry.get()) < 12:
        messagebox.showinfo("Error", "A strong Password should be at least 12 characters long!")
    else:
        # loop through pass length
        for x in range(pass_length):
            # random int between 33 and 126
            # cast to char
            # add to empty var_pass
            var_pass += chr(randint(33, 126))

        # output password to pass_entry
        pass_entry.insert(0, var_pass)


# copy to clipboard
def clipboard():
    # clear clipboard
    root.clipboard_clear()
    # copy to clipboard
    root.clipboard_append(pass_entry.get())

    # info message
    messagebox.showinfo("Copied", "Copied to clipboard!")


# box for insert length
lf = LabelFrame(root, text=" How many Characters do you want for the Password? ")
# pack() method declares the position of widgets in relation to each other
lf.pack(pady=20)

length_entry = Entry(lf, font=("Helvetica", 24))
length_entry.pack(pady=20, padx=20)

# box for generated password
pass_entry = Entry(root, text='', font=("Helvetica", 24), bd=0)
pass_entry.pack(pady=20)

# create frame for button
btn_frame = Frame(root)
btn_frame.pack(pady=20)

# create btn
button = Button(btn_frame, text="Generate Strong", command=new_rand)
button.grid(row=0, column=0, padx=10)

clipboard_btn = Button(btn_frame, text="Copy to Clipboard", command=clipboard)
clipboard_btn.grid(row=0, column=1, padx=10)

# start GUI
root.mainloop()
