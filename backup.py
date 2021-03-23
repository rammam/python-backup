#!/usr/bin/env python3

import shutil
import argparse
import tarfile, glob
import subprocess
import sys
from datetime import datetime

# Arguments (backup-auto.py -a -s [dossier/à/sauvegarder] -d [dossier/de/destination] (--name NomPersonnalisé))
# les paramètres -s et -d deviennent obligatoires si le paramètre -a est présent

parser = argparse.ArgumentParser(description="Effectue une sauvegarde d'un dossier choisi.")
parser.add_argument("-a", "--auto", help="Chemin du dossier à sauvegarder", action="store_true", required=False)
parser.add_argument("-s", "--src_dir", help="Chemin du dossier à sauvegarder", required="-a" in sys.argv)
parser.add_argument("-d", "--dst_dir", help="Chemin du dossier de stockage de la sauvegarde", required="-a" in sys.argv)
parser.add_argument("-n","--name", help="Nom d'archive de backup personnalisé")
args = parser.parse_args()

# Si le paramètre --auto est spécifié, mais pas le dossier source ou celui de destination, envoyer une erreur

if args.auto and (not args.src_dir or not args.dst_dir):
	parser.error("Veuillez spécifier le dossier source et le dossier de destination.")
    
# Si le paramètre --name est spécifié, mais pas le paramètre --auto, envoyer une erreur
    
if args.name and (not args.auto):
    parser.error("Le paramètre --name ne s'utilise qu'en mode automatique.")

# Si le paramètre auto et les dossiers sont spécifiés, lancer le mode automatique

elif args.auto and (args.src_dir and args.dst_dir):

    # Donner aux variables la valeur des arguments entrés dans la commande

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

	#Remplacer "z" par "j" pour utiliser bzip2

	subprocess.run(["tar","-cvzf", dst_archive,"-C", src_dir ,"."])
	       
	# Déplacement de l'archive tar vers le dossier de destination

	shutil.move(dst_archive,dst_dir)

	quit()

# Si le paramètre --auto n'est pas présent

elif not args.auto:

	while 1 == 1:

		backup=input("Faire un backup? (Y/N) : ")
	    
		# Choix de faire un backup
	    
		if backup == "y" or backup == "Y":
		
		# Récupération de la date et de l'heure
		
			date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		
			# Variables :
			#src_dir="dossier/à/sauvegarder"
			#dst_dir="dossier/de/destination"
		
			src_dir=input("Dossier à sauvegarder : ")
			dst_dir=input("Dossier de destination : ")

			while 1 == 1:
			    
				custom=input("Donner un nom particulier à l'archive? (Y/N) : ")
			    
				if custom == "y" or custom == "Y":
			    
					# Nom d'archive personnalisé (optionnel)
					#name="NomPersonnalisé"
				
					name=input("Nom de l'archive : ")
				
					#Remplacer ".tar.gz" par ".tar.bz2" pour utiliser bzip2
				
					dst_archive = name + ".tar.gz"
					break
				
				elif custom == "n" or custom == "N":
			    
					# Nom d'archive automatique avec la date et l'heure
					#Remplacer ".tar.gz" par ".tar.bz2" pour utiliser bzip2
				
					dst_archive = "backup_"+ date +".tar.gz"
					break
				
				else:
					print("Veuillez répondre par Y ou N")
				
				# Création de l'archive tar et ajout de tous
				# les fichiers et sous-dossiers du dossier choisi
				#Remplacer "z" par "j" pour utiliser bzip2
			
			subprocess.run(["tar","-cvzf", dst_archive,"-C", src_dir ,"."])
			
            # Déplacement de l'archive tar vers le dossier de destination
		
			shutil.move(dst_archive,dst_dir)
		    
			quit()
	    
        # Choix de ne pas faire de backup
		    
		elif backup == "n" or backup == "N":
			
			while 1 == 1:
				    
				restore=input("Restaurer un backup? (Y/N) : ")
				    
				# Restauration de backup
				    
				if restore == "y" or restore == "Y":
					
					# Variables :
					#archive="chemin/de/l'archive.tar.gz"
					#dst_dir="dossier/de/destination"
					
					archive = input("Archive du backup : ")
					dst_dir = input("Dossier de destination : ")
						
					# Ouverture et extraction des fichiers et sous-dossiers
					# du backup vers le dossier de destination
					#Remplacer "-xvzf par "-xvjf" pour utiliser bzip2
						
					subprocess.run(["tar","-xvzf",archive,"-C" + dst_dir,"--strip-components=1", "--overwrite"])
						
					quit()
					
				elif restore == "n" or restore == "N":

					quit()
			    
		else:
			print("Veuillez répondre par Y ou N")
	else:
		print("Veuillez répondre par Y ou N")
