from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import urllib


def showHelp(arg=None):
        root = tk.Toplevel()
        info = open('help.txt' , 'r').read()

        # Krijimi i titullit
        root.title('Help Guide')

        # Krijimi i ikones(logo)
        root.iconbitmap('img/logo.ico')

        # Bllokimi i zgjerimit te madhesise se dritares(Window)
        root.resizable(width=False, height=False)
        
        ''' Perfundimi i dritares(Window)'''
        
        # Shtimi i scrollbar ne dritare(window)
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Perdorimi i widget text per te shfaqur permbajtjen scraped
        text = Text(root, yscrollcommand=scrollbar.set, wrap = WORD)
        text.insert(INSERT, info)
        text.pack()

        # Scroll bar
        scrollbar.config(command=text.yview)
        
def Scrape(arg=None):
    
    # Kontrollimi i url-se nese eshte e zbrazet
    if url_entry.get() == '':
        ms.showerror('Gabim', 'Shenoni nje URL valide !!!')
        
    else:
        try:
            ''' Fillon metoda Scraping '''
            # Dhenja e url-se
            url = url_entry.get()
            
            # Leximi i tere permbajtjes
            content = urllib.request.urlopen(url).read()
            
            # Kalimi i permbajtjes tek funksioni
            soup = BeautifulSoup(content, features="lxml")

            # Ruajtja e html ne nje variabel
            info = soup.prettify()
            '''Perfundimi i metodes Scrape '''

            '''Startimi i dritares(Window)'''
            # Krijimi i nje Dritareje(Window) te re
            root = tk.Toplevel()

            # Krijimi i titullit
            root.title('Falemnderit qe perdoret sherbimin tone !!!!')

            # Krijimi i ikones(logo)
            root.iconbitmap('img/logo.ico')

# Bllokimi i zgjerimit te madhesise se dritares(Window)
            root.resizable(width=False, height=False)
            
            ''' Perfundimi i dritares(Window)'''
            
            # Shtimi i scrollbar ne dritare(window)
            scrollbar = Scrollbar(root)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Perdorimi i widget text per te shfaqur permbajtjen scraped
            text = Text(root, yscrollcommand=scrollbar.set, wrap = WORD)
            text.insert(INSERT, info)
            text.pack()

            # Scroll bar
            scrollbar.config(command=text.yview)

        except ValueError:
            ms.showerror('Gabim', 'Shenoni nje URL valide !!!')
    
'''Startimi i dritares(Window)'''
# Krijimi Widget
crawler = tk.Tk()

# Krijimi i madhesise se dritares(Window)
crawler.geometry('500x500')

# Bllokimi i madhesise se dritares(Window)
crawler.resizable(width=False, height=False)

# Krijimi i titullit
crawler.title('URL and structure crawling ')

# Menu
crawler_menu = Menu(crawler)
crawler.config(menu=crawler_menu)

# mundesia per te zgjedhur ne menu-n
choose_menu = Menu(crawler_menu)
help_menu = Menu(crawler_menu)

# objektet ne menu
crawler_menu.add_cascade(label="File" , menu=choose_menu)
choose_menu.add_command(label="URLs" , command=Scrape)
choose_menu.add_command(label="Exit" , command=crawler.destroy)

crawler_menu.add_cascade(label="Help" , menu=help_menu)
help_menu.add_command(label="Show" , command=showHelp)

# Krijimi i ikones(logo)
crawler.iconbitmap('img/logo.ico')
''' Perfundimi i dritares(Window) '''

# Korniza(Frame) Kryesore
top_frame = Label(crawler, text='WEB CRAWLER',font = ('Cosmic', 25, 'bold'), bg='cyan', fg='black', relief='groove',padx=500, pady=30, bd='5')
top_frame.pack(side='top')

''' Startimi i fotos ne prapavije(background)'''
# Kalibrimi i madhesise se fotos
canvas = Canvas(crawler, width=500, height=500)

# Hapja e fotos
image = ImageTk.PhotoImage(Image.open('img/bg6.jpg'))

# Pozicionimi i fotos
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()
'''Perfundimi i fotos ne prapavije(background)'''

# Krijimi i Kornizes(Frame)
frame = LabelFrame(crawler, padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Etiketa(Label)
url_add = tk.Label(frame, text = 'Shenoni nje URL ose Web Address',font=('Arial',10, 'bold'),bg='white', fg='green').pack()

# Hyrja ose Inputi
url_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='lightgray', width='30')

# Kthimi i nje vlere tek funksioni
url_entry.bind('<Return>', Scrape)

# Fokuso tek inputi
url_entry.focus_set()

# Vendosja e butonit
url_entry.pack()

# Etiketa(Label) per ndarjen e butonave
label = Label(frame, bg='white').pack()

# Krijimi i butonit Submit dhe pozicionimi i tij
crawl = tk.Button(frame, text = "Kerko", width="10", bd = '3', command = Scrape, font = ('Times', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='5').pack()

# Krijimi i dritares(window) vetem nje here
crawler.mainloop()
