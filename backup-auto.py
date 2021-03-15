#!/usr/bin/env python3

import argparse
import shutil
import tarfile, glob
from datetime import datetime

parser = argparse.ArgumentParser(description="Effectue une sauvegarde d'un dossier choisi.")
parser.add_argument("src_dir", help="Chemin du dossier à sauvegarder")
parser.add_argument("dst_dir", help="Chemin du dossier de stockage de la sauvegarde")
parser.add_argument("-n","--name", help="Nom d'archive de backup personnalisé")
args = parser.parse_args()

src_dir=args.src_dir
dst_dir=args.dst_dir
name=str(args.name)

if name == "None":
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dst_archive = "backup_"+ date +".tar.gz"
    
else:
    dst_archive = name + ".tar.gz"
        
tar = tarfile.open(dst_archive,"x:gz")
for file in glob.glob(src_dir+"/**",recursive=True):
    tar.add(file, recursive=False)
       
# Déplacement de l'archive tar vers le dossier de destination
        
shutil.move(dst_archive,dst_dir)
    
quit()
