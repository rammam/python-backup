#!/usr/bin/env python3

import argparse
import shutil
import tarfile, glob
from datetime import datetime

# Arguments (backup-auto.py [dossier/à/sauvegarder] [dossier/de/destination] (--name NomPersonnalisé)

parser = argparse.ArgumentParser(description="Effectue une sauvegarde d'un dossier choisi.")
parser.add_argument("src_dir", help="Chemin du dossier à sauvegarder")
parser.add_argument("dst_dir", help="Chemin du dossier de stockage de la sauvegarde")
parser.add_argument("-n","--name", help="Nom d'archive de backup personnalisé")
args = parser.parse_args()

# Variables :
#src_dir="dossier/à/sauvegarder"
#dst_dir="dossier/de/destination"
#name="NomPersonnalisé" (Optionnel)

src_dir=args.src_dir
dst_dir=args.dst_dir
name=str(args.name)

if name == "None":
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    #Remplacer ".tar.gz" par ".tar.bz2" pour utiliser bzip2
    
    dst_archive = "backup_"+ date +".tar.gz"
    
else:
    #Remplacer ".tar.gz" par ".tar.bz2" pour utiliser bzip2
    
    dst_archive = name + ".tar.gz"

#Remplacer "x:gz" par "x:bz2" pour utiliser bzip2

tar = tarfile.open(dst_archive,"x:gz")
for file in glob.glob(src_dir+"/**",recursive=True):
    tar.add(file, recursive=False)
       
# Déplacement de l'archive tar vers le dossier de destination

shutil.move(dst_archive,dst_dir)

quit()
