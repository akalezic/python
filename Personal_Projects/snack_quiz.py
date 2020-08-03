"""
File: snack_quiz.py
-------------------

"""

import tkinter as tk

FONT_SIZE = 18

def main():
    # create a window object
    window = tk.Tk()
    # create a label/text object that has a white background, black text, and specified font)
    greeting = tk.Label(text="What kind of snack should you have?",
                        foreground='black',
                        background='white',
                        font=('Helvetica',FONT_SIZE),
                        width=50)
    # places widget in the window and centers it because no other location specified
    greeting.pack()
    # creates a button that has specific text in these parameters
    button1 = tk.Button(text='Salty', foreground='limegreen', font=('Helvetica',FONT_SIZE), command=salty_q)
    # places button in center of window
    button1.pack()
    # creates button that has text in these parameters
    button2 = tk.Button(text='Sweet', foreground='magenta', font=('Helvetica',FONT_SIZE), command=sweet_q)
    # places button in center of window
    button2.pack()
    window.mainloop()

def sweet_q():
    sweet = tk.Label(text='Do you want something baked, cold/frozen, or a candy?',
                     foreground='black',
                     background='white',
                     font=('Helvetica',FONT_SIZE),
                     width=50)
    sweet.pack()
    buttonA = tk.Button(text='Baked', foreground='tan', font=('Helvetica',FONT_SIZE), command=baked)
    buttonA.pack()
    buttonB = tk.Button(text='Cold/Frozen', foreground='dodgerblue', font=('Helvetica',FONT_SIZE), command=cold)
    buttonB.pack()
    buttonC = tk.Button(text='Candy', foreground='deeppink', font=('Helvetica',FONT_SIZE), command=candy)
    buttonC.pack()

def salty_q():
    salty = tk.Label(text='Do you want something spicy, cheesy, or regular salty?',
                     foreground='black',
                     background='white',
                     font=('Helvetica',FONT_SIZE),
                     width=50)
    salty.pack()
    buttonD = tk.Button(text='Spicy', foreground='red', font=('Helvetica',FONT_SIZE), command=spicy)
    buttonD.pack()
    buttonE = tk.Button(text='Cheesy', foreground='darkorange', font=('Helvetica',FONT_SIZE), command=cheesy)
    buttonE.pack()
    buttonF = tk.Button(text='Regular Salty', foreground='darkgoldenrod', font=('Helvetica',FONT_SIZE), command=reg)
    buttonF.pack()

def baked():
    baked =  tk.Label(text='Do you want something chocolatey or not?',
                      foreground='black',
                      background='white',
                      font=('Helvetica', FONT_SIZE),
                      width=50)
    baked.pack()
    buttonG = tk.Button(text='Chocolatey', foreground='saddlebrown', font=('Helvetica',FONT_SIZE), command=choc)
    buttonG.pack()
    buttonH = tk.Button(text='Not', foreground='mediumblue', font=('Helvetica',FONT_SIZE), command=not_choc)
    buttonH.pack()

def cold():
    cold = tk.Label(text='Do you want something you eat with a spoon?',
                    foreground='black',
                    background='white',
                    font=('Helvetica', FONT_SIZE),
                    width=50)
    cold.pack()
    buttonI = tk.Button(text='Yes', foreground='black', font=('Helvetica', FONT_SIZE), command=spoon)
    buttonI.pack()
    buttonJ = tk.Button(text='No', foreground='black', font=('Helvetica', FONT_SIZE), command=no_spoon)
    buttonJ.pack()

def candy():
    candy = tk.Label(text='Do you want sweet or sour candy?',
                     foreground='black',
                     background='white',
                     font=('Helvetica', FONT_SIZE),
                     width=50)
    candy.pack()
    buttonK = tk.Button(text='Sweet', foreground='magenta', font=('Helvetica', FONT_SIZE), command=sweet_cand)
    buttonK.pack()
    buttonL = tk.Button(text='Sour', foreground='lime', font=('Helvetica', FONT_SIZE), command=sour_cand)
    buttonL.pack()

def cheesy():
    cheese = tk.Label(text='You should have a cheese plate!', foreground='black',
                     background='cornsilk',
                     font=('Helvetica', FONT_SIZE),
                     width=50)
    cheese.pack()

def spicy():
    chips = tk.Label(text='You should have chips and salsa!', foreground='black',
                     background='greenyellow',
                     font=('Helvetica', FONT_SIZE),
                     width=50)
    chips.pack()

def reg():
    reg = tk.Label(text='You should have your favorite kind of chips!',
                   foreground='black',
                   background='peachpuff',
                   font=('Helvetica', FONT_SIZE),
                   width=50)
    reg.pack()

def choc():
    choc = tk.Label(text= 'You should have a brownie!',
                    foreground='black',
                    background='saddlebrown',
                    font=('Helvetica', FONT_SIZE),
                    width=50)
    choc.pack()

def not_choc():
    notchoc = tk.Label(text='You should have a cookie!',
                       foreground='black',
                       background='sandybrown',
                       font=('Helvetica', FONT_SIZE),
                       width=50)
    notchoc.pack()

def spoon():
    spoon = tk.Label(text='Do you want a low calorie option?',
                     foreground = 'black',
                     background = 'white',
                     font = ('Helvetica', FONT_SIZE),
                     width = 50)
    spoon.pack()
    buttonM = tk.Button(text='Low-calorie', foreground='blue', font = ('Helvetica', FONT_SIZE), command=froyo)
    buttonM.pack()
    buttonN = tk.Button(text='Does not matter', foreground='limegreen', font = ('Helvetica', FONT_SIZE), command=cream)
    buttonN.pack()

def no_spoon():
    nospoon = tk.Button(text='You should have a milkshake!',
                        foreground = 'black',
                        background = 'linen',
                        font=('Helvetica', FONT_SIZE),
                        width = 50)
    nospoon.pack()

def sweet_cand():
    sweetc = tk.Button(text='You should have caramels!',
                       foreground = 'black',
                       background = 'burlywood',
                       font=('Helvetica', FONT_SIZE),
                       width=50)
    sweetc.pack()

def sour_cand():
    sourc = tk.Button(text='You should have sour gummies!',
                      foreground = 'black',
                      background = 'aqua',
                      font=('Helvetica', FONT_SIZE),
                      width=50)
    sourc.pack()

def froyo():
    froyo = tk.Label(text='You should have frozen yogurt!',
                     foreground = 'black',
                     background = 'mediumpurple',
                     font = ('Helvetica', FONT_SIZE),
                     width = 50)
    froyo.pack()

def cream():
    cream = tk.Label(text='You should have ice cream!',
                     foreground = 'black',
                     background = 'orchid',
                     font=('Helvetica', FONT_SIZE),
                     width=50)
    cream.pack()

if __name__ == '__main__':
    main()