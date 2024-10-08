from bs4 import BeautifulSoup as bs
import requests
from tkinter import*
from tkinter import messagebox
from time import strftime

fenetre=Tk()
fenetre.title('Scrap')
fenetre['bg']='gray'

texte=StringVar()
saisie=Entry(fenetre)
saisie.configure(textvariable=texte)
saisie.pack()



bouton=Button(fenetre)
bouton.configure(text='Executer')
bouton.pack()

def Scrap(event):
    execute=texte.get()    
    url=execute
    response = requests.get(url)
    html = response.content
    soup = bs(html, 'html.parser')

    fait = Label(fenetre, text = "Fait : %s" % url)
    fait.pack()
    with open("sortie.html", "w") as file:  
        file.write(str(soup.prettify()))
bouton.bind('<ButtonPress-1>',Scrap)


fenetre.mainloop()
