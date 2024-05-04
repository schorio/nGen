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

label_mot_de_passe = tk.Label(root, text="")
label_mot_de_passe.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()