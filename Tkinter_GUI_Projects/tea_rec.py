"""
File: tea_rec.py
----------------
After working in a tea shop and being an avid tea drinker for years, both customers and I have had 
the issue of not knowing what tea to drink. This program is intended to narrow a tea drinker's options
down by asking a series of questions.

Disclaimer: The teas that are linked are my personal favorites of each type! Multiple options are
included for some, and as such mutltiple web browser windows will open when a button is pressed.
"""

# imports tkinter and ttk libraries and webbrowser libraries
from tkinter import *
from tkinter import ttk
import webbrowser

# each function follows a similar method, the ones with a button command that leads to a webpage will have a
# command that opens a webbrowser
def decaf():
    # inputs the question to be asked into the window
    flavor = ttk.Label(mainframe, text='Fruity or herbal?')
    # packs the question into the window
    flavor.pack()
    # creates the button to put into the window
    fruity = ttk.Button(mainframe, text='Fruity', command=fruit)
    # packs the button into the window
    fruity.pack()
    herbal = ttk.Button(mainframe, text='Herbal', command=mint)
    herbal.pack()

def caffeine():
    gb = ttk.Label(mainframe, text='Green or black tea?')
    gb.pack()
    green = ttk.Button(mainframe, text='Green', command=gt)
    green.pack()
    black = ttk.Button(mainframe, text='Black', command=bt)
    black.pack()

# creates the root window
root = Tk()
# puts a title at the top of the window
root.title('Tea Recommendation')
# creates a frame in the root window with space around the text
mainframe = ttk.Frame(root, padding="6 6 12 12")
# creates the initial question
label = ttk.Label(mainframe, text='Would you like caffeinated tea or not?')
label.pack()
caf = ttk.Button(mainframe, text='Caffeine', command=caffeine)
caf.pack()
nocaf = ttk.Button(mainframe, text='No caffeine', command=decaf)
nocaf.pack()
# packs the frame into the root window
mainframe.pack()


def bt():
    bt_type = ttk.Label(mainframe, text='Do you want flavored or unflavored black tea?')
    bt_type.pack()
    flav_bt = ttk.Label(mainframe, text='Flavored', command=flavored_b)
    flav_bt.pack()
    unflav_bt = ttk.Label(mainframe, text='Unflavored', command=trad_bt)
    unflav_bt.pack()

# this function prints the question and buttons into the mainframe, but instead of leading to
# another question with more buttons in this case, each button opens a different webpage based
# on the user's preferences
def flavored_b():
    what_flav_bt = ttk.Label(mainframe, text='Do you want a dessert-y, fruity, or spicy/chai-like black tea?')
    what_flav_bt.pack()
    dessert = ttk.Button(mainframe, text='Desserty',
                         command=lambda: webbrowser.open('https://shop.tgtea.com/Salty-Cream-Caramel-001629-100/7322/'))
    dessert.pack()
    fruit_bt = ttk.Button(mainframe, text='Fruity',
                          command=lambda: webbrowser.open('https://shop.tgtea.com/Pineapple-Mango-00988-100/5262/'))
    fruit_bt.pack()
    chai_bt = ttk.Button(mainframe, text='Chai',
                         command=lambda: webbrowser.open('https://shop.tgtea.com/Indian-Chai-00780-100/5140/'))
    chai_bt.pack()


def trad_bt():
    strength = ttk.Label(mainframe, text='Do you want a stronger, more robust black tea or something more smooth?')
    strength.pack()
    strong = ttk.Button(mainframe, text='Strong',
                        command=lambda: webbrowser.open('https://shop.tgtea.com/Assam-Heeleakah-Second-Flush-00145-100/4946/'))
    strong.pack()
    smooth = ttk.Button(mainframe, text='Smooth',
                        command=lambda: webbrowser.open('https://shop.tgtea.com/China-Golden-Yunnan-Organic-00570-100/5079/'))
    smooth.pack()


def gt():
    flav = ttk.Label(mainframe, text='Do you want flavored or unflavored green tea?')
    flav.pack()
    flav_gt = ttk.Button(mainframe, text='Flavored', command=flavored_g)
    flav_gt.pack()
    unflav_gt = ttk.Button(mainframe, text='Unflavored', command=trad_gt)
    unflav_gt.pack()


def flavored_g():
    profile = ttk.Label(mainframe, text='Do you want something fruity, floral, or spicy like a chai?')
    profile.pack()
    frui_gt = ttk.Button(mainframe, text='Fruity',
                         command=lambda:[webbrowser.open('https://shop.tgtea.com/Marani-00953-100/5284/'), webbrowser.open('https://shop.tgtea.com/Cranberry-Mango-00920-100/5266/')])
    frui_gt.pack()
    flor_gt = ttk.Button(mainframe, text='Floral',
                         command=lambda: webbrowser.open('https://www.adagio.com/green/dragon_pearl.html'))
    flor_gt.pack()
    spi_gt = ttk.Button(mainframe, text='Spicy/chai',
                        command=lambda: webbrowser.open('https://shop.tgtea.com/Kashmir-Khali-Kahwa-00943-1000/5430/'))
    spi_gt.pack()


def trad_gt():
    region = ttk.Label(mainframe, text='Do you prefer roasted notes or more of a grassy, vegetal flavor?')
    region.pack()
    china = ttk.Button(mainframe, text='Roasted notes', command=china_type)
    china.pack()
    japan = ttk.Button(mainframe, text='Grassy, vegetal notes', command=jap_type)
    japan.pack()


def china_type():
    trad_profile = ttk.Label(mainframe, text='Do you want something sweeter or smokier?')
    trad_profile.pack()
    sweeter = ttk.Button(mainframe, text='Sweeter',
                         command=lambda:webbrowser.open('https://shop.tgtea.com/China-Lung-Ching-Organic-00519-100/5111/'))
    sweeter.pack()
    smoky = ttk.Button(mainframe, text='Smokier',
                       command=lambda: webbrowser.open('https://shop.tgtea.com/China-Gunpowder-Organic-00505-100/5103/'))
    smoky.pack()


def jap_type():
    jap_profile = ttk.Label(mainframe, text='Do you want a strong vegetal flavor, a toasty flavor, or something mild?')
    jap_profile.pack()
    strong_gt = ttk.Button(mainframe, text='Strong',
                           command=lambda: [webbrowser.open('https://shop.tgtea.com/Seogwang-Sencha-00591-500/6132/'), webbrowser.open('https://www.harney.com/collections/japanese-green-tea/products/organic-sencha')])
    strong_gt.pack()
    toasty = ttk.Button(mainframe, text='Toasty',
                        command=lambda: webbrowser.open('https://shop.tgtea.com/Japan-Genmaicha-Organic-00703-100/5128/'))
    toasty.pack()
    mild = ttk.Button(mainframe, text='Mild',
                      command=lambda: webbrowser.open('https://shop.tgtea.com/Japan-Gyokuro-Kukicha-00716-100/6932/'))
    mild.pack()


def fruit():
    kind = ttk.Label(mainframe, text='Citrus, berry or peach?')
    kind.pack()
    citrus = ttk.Button(mainframe, text='Citrus',
                        command=lambda: webbrowser.open('https://shop.tgtea.com/Blood-Orange-Fruit-Tea-001418-1000/7312/'))
    citrus.pack()
    berry = ttk.Button(mainframe, text='Berry',
                       command=lambda:[webbrowser.open('https://shop.tgtea.com/Summer-Romance-001444-100/5519/'), webbrowser.open('https://shop.tgtea.com/Strawberry-Moringa-001453-100/7205/')])
    berry.pack()
    peach = ttk.Button(mainframe, text='Peach',
                       command=lambda: webbrowser.open('https://shop.tgtea.com/Peachy-Green-Rooibush-001386-100/5663/'))
    peach.pack()


def mint():
    minty = ttk.Label(mainframe, text='Do you like mint?')
    minty.pack()
    love = ttk.Button(mainframe, text='Love it!',
                      command=lambda: webbrowser.open('https://www.adagio.com/herbal/peppermint.html'))
    love.pack()
    meh = ttk.Button(mainframe, text='Prefer to do without',
                     command=lambda: webbrowser.open('https://shop.tgtea.com/Sleep-tight-Tea-001254/238/'))
    meh.pack()

root.mainloop()
