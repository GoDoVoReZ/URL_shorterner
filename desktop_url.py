import tkinter as tk 

from url_short_main import  short_url
from url_db import *

class App(tk.Tk):

    def __init__(self):
        super().__init__()


        self.title('URL SHORT')
        self.iconbitmap('env/w_ico.ico')
        self.geometry('300x300')
        self.config(bg='black')

        db_create()


        self.label = tk.Label(
            self,
            text='Short URL here',
            fg='orange',
            bg='black',
            font='Helvetica 14')

        self.entry = tk.Entry(
            self,
            width='30',
            fg='orange',
            bg='black',
            font='Helvetica 12')

        def show_sh_url():
            sh_url = short_url(self.entry.get())
            self.entry1 = tk.Entry(
                self,
                width='30',
                fg='orange',
                bg='black',
                font='Helvetica 12')
            self.entry1.insert(0, sh_url)
            self.entry1.pack()

        self.btn = tk.Button(
            self,
            text='SHORT',
            fg='orange',
            bg='black',
            activebackground='orange',
            activeforeground='black',
            padx='10',
            pady='5',
            font='Helvetica 16',
            command=show_sh_url)






        self.label.pack()
        self.entry.pack()
        self.btn.pack()




if __name__ == '__main__':
    app = App()
    app.mainloop()