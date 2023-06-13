import os

# Rechercher le fichier ".pt" dans le répertoire de travail actuel
for file in os.listdir():
    if file.endswith(".pt"):
        model_path = file
        break

# Vérifier si le fichier ".pt" a été trouvé
if model_path:
    print("Fichier .pt trouvé :", model_path)
else:
    print("Fichier .pt non trouvé.")
C:\Users\user\Desktop\projet\WhatsApp Image 2023-06-01 at 5.53.32 PM.jpeg