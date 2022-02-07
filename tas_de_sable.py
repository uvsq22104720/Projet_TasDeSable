
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
color_button = tk.Button(fenetre, text="Change Color", font=("Century Gothic", 20), fg='black')
color_button.place(x=7, y=50)
color_button.pack


# afficher
fenetre.mainloop()