from Tkinter import *


class Sign_in:
    def __init__(self, master):
        self.master = master
        self.my_login_data = StringVar()
        self.my_pass_data = StringVar()
        self.label2 = Label(master, text="Username", fg="Blue")
        self.label2.grid()
        self.Login = Entry(master, text='', textvariable=self.my_login_data)
        self.Login.grid()
        self.label3 = Label(master, text="Password", fg="Blue")
        self.label3.grid()
        self.Password = Entry(master, text='', textvariable=self.my_pass_data, show="*")
        self.Password.grid()

        self.askPrecisionBtn = Button(master, text='Login')
        self.askPrecisionBtn.grid()

        self.setBind()

    def setBind(self):
        self.Login.bind('<Return>', self.getPrecision)
        self.Password.bind('<Return>', self.getPrecision)
        self.askPrecisionBtn.bind('<Return>', self.getPrecision)
        self.askPrecisionBtn.bind('<Button-1>', self.getPrecision)

    def getPrecision(self, master):
        global my_pass_data
        global my_login_data
        my_passdata = self.my_pass_data.get()
        my_logindata = self.my_login_data.get()
        if (my_logindata.__len__() == 0) or (my_passdata.__len__() == 0):
            self.askPrecisionBtn['bg'] = '#ff0000'
        else:
            my_pass_data = self.my_pass_data.get()
            my_login_data = self.my_login_data.get()
            self.master.destroy()


def main():
    root = Tk()
    gui = Sign_in(root)
    root.mainloop()


if __name__ == '__main__':
    main()

