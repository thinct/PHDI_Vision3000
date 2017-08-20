# coding=utf-8
import Tkinter
import tkMessageBox
 
def show():
    tkMessageBox.showinfo(title='测试', message='出厂设置')
 
def creatfram():
    root = Tkinter.Tk()
    b = Tkinter.Button(root, text="测试", command=show)
    b.pack()
    root.mainloop()
 
creatfram()

