import os
import customtkinter as ctk
import tkinter as tk
import random
import string

root = ctk.CTk()
root.title("Générateur de Mot de Passe")

label_longueur = ctk.CTkLabel(root, text="Longueur du mot de passe :")
label_longueur.grid(row=0, column=0, padx=5, pady=5)
entry_longueur = ctk.CTkEntry(root)
entry_longueur.grid(row=0, column=1, padx=5, pady=5)

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def generer_mot_de_passe_et_afficher():
    longueur = int(entry_longueur.get())
    mot_de_passe = generer_mot_de_passe(longueur)
    label_mot_de_passe.config(text="Mot de passe généré : " + mot_de_passe)
    
bouton_generer = ctk.CTkButton(root, text="Générer", command=generer_mot_de_passe_et_afficher)
bouton_generer.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

label_mot_de_passe = tk.Label(root, text="")
label_mot_de_passe.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()