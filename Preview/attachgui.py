from tkinter import *

from Preview.tkinter102 import MyGui

main_win = Tk()
Label(main_win, text=__name__).pack()

popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
main_win.mainloop()
