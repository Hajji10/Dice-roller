import tkinter 
from PIL import Image, ImageTk
import random

# Widget, that represents the main window
root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice roller')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

HeadingLabel = tkinter.Label(root, text="Hej!", fg="black", bg="white", font="Helvetica 16 bold italic")
HeadingLabel.pack()

# Billeder
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# Simulere terningen tilfældigt mellm 0 til 6 samt billeder
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Konstruere et label widget for billederne
ImageLabel = tkinter.Label(root, image=image1)
ImageLabel.image = image1

ImageLabel.pack(expand=True)

# Knap for at simulere terningen
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # Opdatere billedet
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage

button = tkinter.Button(root, text='Roll the dice', fg='red', command=rolling_dice)
button.pack(expand=True)

# Kalder mainloop af Tk og
# Holder vinduet åbent
root.mainloop()
