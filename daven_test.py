
#test tkinter
import tkinter as tk
fenetre=tk.Tk()
fenetre.geometry('500x100')
fenetre.title('enrichi')
def nombre_de_points():
    fenetre.destroy()
    a=saisie.get
    fenetre2=tk.Tk()
    fenetre2.geometry('500x100')
    fenetre2.title('hehe')
    texte2 = tk.Label(fenetre, text=('ya :',a,'points'), fg='blue')
    texte2.pack(fenetre2)
texte1=tk.Label(fenetre,text='nombre de point? :', fg='blue')
texte1.pack()
saisie = tk.Entry(fenetre, bg='white', fg='black')
saisie.pack()

bouton1=tk.Button(fenetre, text='ciao',command=nombre_de_points)
bouton1.pack()
fenetre.mainloop()

#test permutation possible