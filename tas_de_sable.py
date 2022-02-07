
######################################################
# groupe MI TD01
# Anis
# Lilya
# Amira
# https://github.com/uvsq22104720/Projet_TasDeSable
######################################################


import tkinter as tk

# creer une fenetre
fenetre = tk.Tk()


# perso fenetre
fenetre.title("Generateur Couleur")
fenetre.geometry("850x850")

# Creer un Canevas
caneva = tk.Canvas(fenetre, bg='#8FB1CE', width=500, height=800)
caneva.pack()


# Ajouter un Bouton
color_button = tk.Button('', text="Change Color", font=("Courrier", 11), fg='black',)
color_button.pack


# afficher
fenetre.mainloop()