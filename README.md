# python-backup
> Créez des backups et restaurez-les.

Création de backup : Sauvegarde un dossier en tant qu'archive gzip datée vers le chemin choisi.

Restauration de backup : Restaure l'archive et écrit par dessus les fichiers/dossiers identiques.

## Installation

```sh
git clone https://github.com/rammam/python-backup/
```

## Utilisation

Lancer le script :
```sh
sudo python3 backup.py
```
Tous les paramètres sont sous forme d'input, on spécifie les dossiers de sauvegarde avec un path absolu ou relatif.

## Versions

* 0.1.0
    * Première release
