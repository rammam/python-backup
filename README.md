# python-backup

> Sauvegardez des backups de dossiers et restaurez-les automatiquement.

## Fonctionnement

Création de backup : Sauvegarde un dossier en tant qu'archive gzip vers le chemin choisi.

Restauration de backup : Restaure l'archive et écrit par dessus les fichiers/dossiers identiques.

## Installation

```sh
git clone https://github.com/rammam/python-backup/
```

## Utilisation

### Script principal

#### Exécution :

```sh
sudo python3 backup.py
```
Tous les paramètres seront demandés pendant l'exécution, on spécifie les dossiers avec un path absolu ou relatif.

### Script automatique :

#### Exécution :

```sh
sudo python3 backup-auto.py <dossier/à/sauvegarder> <dossier/de/destination> [--name NomPersonnalisé]
```
Le paramètre --name est optionnel.

Le nom par défaut des archives est sous ce format :

```sh
backup_YYYY-MM-DD_HH-MM-SS.tar.gz
```

## Versions

* 0.1.0
    * Première release

## Modifications

Toutes les modifications détaillées sont en commentaires dans le code, et sont :

* Les chemins de dossier
* Le type de compression de l'archive
* Le nom des archives à créer

## Contribuer

Les contributions sont ce qui fait de la communauté open source un endroit extraordinaire pour apprendre, inspirer et créer. Toutes vos contributions sont grandement appréciées.

* Signalez les problèmes
* Ouvrez des pull request pour des améliorations
* Parlez-en autour de vous !

## Licence

Ce projet est sous licence GNU General Public License v3.0.
