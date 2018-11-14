from tkinter import *
window = Tk()
window.title('Lucky Number Picker')
window.resizable(0,0)

img = PhotoImage(file = 'power.gif')

imgLbl = Label(window, image = img)
label1 = Label(window, relief = 'groove', width = 2)
label2 = Label(window, relief = 'groove', width = 2)
label3 = Label(window, relief = 'groove', width = 2)
label4 = Label(window, relief = 'groove', width = 2)
label5 = Label(window, relief = 'groove', width = 2)
label6 = Label(window, relief = 'groove', width = 2)
getBtn = Button(window)
resBtn = Button(window)

imgLbl.grid(row =1, column =1, rowspan =2)
label1.grid(row =1, column =2, padx =10)
label2.grid(row =1, column =3, padx =10)
label3.grid(row =1, column =4, padx =10)
label4.grid(row =1, column =5, padx =10)
label5.grid(row =1, column =6, padx =10)
label6.grid(row =1, column =7, padx =10)
getBtn.grid(row =2, column =2, columnspan =4)
resBtn.grid(row =2, column =6, columnspan =2)

getBtn.configure(text = 'Get My Lucky Numbers')
resBtn.configure(text = 'Reset')

from random import sample

def pick():
    nums = sample(range(1,70),5)
    ball = sample(range(1,27),1)
    label1.configure(text = nums[0])
    label2.configure(text = nums[1])
    label3.configure(text = nums[2])
    label4.configure(text = nums[3])
    label5.configure(text = nums[4])
    label6.configure(text = ball[0])
    getBtn.configure(state = DISABLED)
    resBtn.configure(state = NORMAL)
    
def reset():
    label1.configure(text ='...')
    label2.configure(text ='...')
    label3.configure(text ='...')
    label4.configure(text ='...')
    label5.configure(text ='...')
    label6.configure(text ='...')
    getBtn.configure(state = NORMAL)
    resBtn.configure(state= DISABLED)
	
getBtn.configure( command = pick)
resBtn.configure(command = reset)

window.mainloop()