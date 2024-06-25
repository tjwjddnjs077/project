import tkinter
import tkinter.font
window = tkinter.Tk()
window.title('음식계산기')
window.geometry('600x400+100+100')

def func1():
    price = 0
    if cv1.get() == 1:
        price+=5000
    if cv1.get() == 1:
        price+=6000
    if cv1.get() == 1:
        price+=7000
    if cv1.get() == 1:
        price+=12000
result.config(text= ' 가격: '+str(price)+'원')

title_font = tkinter.font.Font(family='맑은 고딕',size=20)
title = tkinter.Label(window, text = '음식 계산기',font=title_font)
title.grid(row=0, column=0,columnspan=4)

image1= tkinter.PhotoImage(file='1.PNG')
image2= tkinter.PhotoImage(file='d.PNG')
image3= tkinter.PhotoImage(file='dddd.PNG')
image4= tkinter.PhotoImage(file='캡처.PNG')

label1= tkinter.Label(window, image=image1)
label2= tkinter.Label(window, image=image2)
label3= tkinter.Label(window, image=image3)
label4= tkinter.Label(window, image=image4)

cv1 = tkinter.IntVar()
ckb1 =  tkinter.Checkbutton(window, text= '5000원',variable=cv1, command=func1)

cv2 = tkinter.IntVar()
ckb2 =  tkinter.Checkbutton(window, text= '6000원',variable=cv2, command=func1)

cv3 = tkinter.IntVar()
ckb3 =  tkinter.Checkbutton(window, text= '7000원',variable=cv3, command=func1)

cv4 = tkinter.IntVar()
ckb4 =  tkinter.Checkbutton(window, text= '12000원',variable=cv4, command=func1)

result = tkinter.Label(window,text= ' 가격 :5000원', font=title_font)
result.grid(row=3, column=0.columnspan=4)

label1.grid(row=1, column=0)
label2.grid(row=1, column=1)
label3.grid(row=1, column=2)
label4.grid(row=1, column=3)
ckb1.grid(row=2, column=0)
ckb2.grid(row=2, column=1)
ckb3.grid(row=2, column=2)
ckb4.grid(row=2, column=3)
window.mainloop()
