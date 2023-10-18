# import os
# import glob
# import shutil
#
# home_path = r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Udemy\LaFormationCompletePython\TrierDesFichiersSelonLeurType"
# search_path = r'C:\Users\MOTTIER LUCIE\Documents\GitHub\Udemy\LaFormationCompletePython\TrierDesFichiersSelonLeurType' \
#               r'\**'
#
# directory_list = ['Musique', 'Videos', 'Images', 'Documents']
#
# # Creation des repertoires pour stocker les images
# for directory in directory_list:
#     directory_path = os.path.join(home_path, directory)
#     os.makedirs(directory_path, exist_ok=True)
#
#     # Recupertation de tous les fichiers dans une liste:
#     files = glob.glob(search_path)
#
#     if directory == 'Musique':
#         for file in files:
#             if file.endswith(".mp3") or file.endswith(".wav"):
#                 directory_path = os.path.join(home_path, "Musique")
#                 shutil.move(file, directory_path)
#     elif directory == 'Videos':
#         for file in files:
#             if file.endswith(".mp4"):
#                 directory_path = os.path.join(home_path, "Videos")
#                 shutil.move(file, directory_path)
#     elif directory == 'Images':
#         for file in files:
#             if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
#                 directory_path = os.path.join(home_path, "Images")
#                 shutil.move(file, directory_path)
#     elif directory == 'Documents':
#         for file in files:
#             if file.endswith(".pdf"):
#                 directory_path = os.path.join(home_path, "Documents")
#                 shutil.move(file, directory_path)

# Correction
import os
from glob import glob
import shutil

chemin = r"C:\Users\MOTTIER LUCIE\Documents\GitHub\Udemy\LaFormationCompletePython\TrierDesFichiersSelonLeurType"

extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents"}

fichiers = glob(os.path.join(chemin, "*"))
for fichier in fichiers:
    extension = os.path.splitext(fichier)[-1]
    dossier = extensions.get(extension)
    if dossier:
        chemin_dossier = os.path.join(chemin, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)
        shutil.move(fichier, chemin_dossier)