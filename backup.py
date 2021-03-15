#!/usr/bin/env python3

import shutil
import tarfile, glob
import subprocess
from datetime import datetime


while 1 == 1:

    backup=input("Faire un backup? (Y/N) : ")
    
    # Choix de faire un backup
    if backup == "y" or backup == "Y":
        
        # Récupération de la date et de l'heure
        date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        src_dir=input("Dossier à sauvegarder : ")
        dst_dir=input("Dossier de destination : ")

        while 1 == 1:
            
            custom=input("Donner un nom particulier à l'archive? (Y/N) : ")
            
            if custom == "y" or custom == "Y":
            
                # Nom d'archive personnalisé
                
                name=input("Nom de l'archive : ")
                dst_archive = name + ".tar.gz"
                break
                
            elif custom == "n" or custom == "N":
            
                # Nom d'archive automatique avec la date et l'heure
                
                dst_archive = "backup_"+ date +".tar.gz"
                break
                
            else:
                print("Veuillez répondre par Y ou N")
                
        # Création de l'archive tar et ajout de tous
        # les fichiers et sous-dossiers du dossier choisi
        
        tar = tarfile.open(dst_archive,"x:gz")
        for file in glob.glob(src_dir+"/**",recursive=True):
            tar.add(file, recursive=False)
        
        # Déplacement de l'archive tar vers le dossier de destination
        
        shutil.move(dst_archive,dst_dir)
    
        quit()
    
    # Choix de ne pas faire de backup
    elif backup == "n" or backup == "N":
        
        while 1 == 1:
            
            restore=input("Restaurer un backup? (Y/N) : ")
            
            # Restauration de backup
            
            if restore == "y" or restore == "Y":
                
                archive = input("Archive du backup : ")
                dst_dir = input("Dossier de destination : ")
                
                # Ouverture et extraction des fichiers et sous-dossiers
                # du backup vers le dossier de destination
                
                subprocess.run(["tar","-xvf",archive,"-C" + dst_dir,"--strip-components=1", "--overwrite"])
                
                quit()
                
            elif backup == "n" or backup == "N":
                quit()
            
            else:
                print("Veuillez répondre par Y ou N")
    else:
        print("Veuillez répondre par Y ou N")
