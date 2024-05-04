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

root.mainloop()