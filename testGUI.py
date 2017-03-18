from Tkinter import *


def getPrecision(self):
    global my_pass_data
    global my_login_data
    my_pass_data = my_pass_data.get()
    my_login_data = my_login_data.get()
    root.destroy()

root = Tk()
my_login_data = StringVar()
my_pass_data = StringVar()
label2 = Label(root, text = "Username", fg="Blue")
label2.grid()
Login = Entry(root, text = '', textvariable=my_login_data)
Password = Entry(root, text = '', textvariable=my_pass_data,show="*")
Login.grid()
label3 = Label(root, text = "Password", fg="Blue")
label3.grid()
Password.grid()

askPrecisionBtn = Button(root, text='Login')
askPrecisionBtn.bind('<Return>', getPrecision)
askPrecisionBtn.bind('<Button-1>', getPrecision)
askPrecisionBtn.grid()


def main():

    root.mainloop()

if __name__ == '__main__':
    main()

