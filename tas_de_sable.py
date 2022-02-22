
######################################################
# groupe MI TD01
# Anis
# Lilya
# Amira
# https://github.com/uvsq22104720/Projet_TasDeSable
######################################################


import tkinter as tk


# Fonction 
def change_ColorCanvas():
    caneva.config(bg='purple')


# création des widgets
fenetre = tk.Tk()
fenetre.title("Generateur Couleur")
fenetre.geometry("900x900")
caneva = tk.Canvas(fenetre, bg='#8FB1CE', width=600, height=600, highlightthickness=10, highlightbackground="black")
button = tk.Button(fenetre, text="Change Color", font=("Century Gothic", 20), fg='black', command=change_ColorCanvas)


#positionnement des widgets
caneva.grid()
button.grid()

#liaison du clic
#caneva.bind("<Button-1>", "fonction")


# boucle principal
fenetre.mainloop()