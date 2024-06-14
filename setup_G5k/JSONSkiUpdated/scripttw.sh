#!/bin/bash

# Vérifier s'il y a un argument passé au script
if [ $# -ne 1 ]; then
    echo "Usage: $0 fichier.json"
    exit 1
fi

# Vérifier si le fichier JSON existe
if [ ! -f "$1" ]; then
    echo "Le fichier $1 n'existe pas."
    exit 1
fi

jsonski -f "$1" -k "Created_at" | while read -r path; do
    echo "Champ 'author' trouvé au chemin : $path"
done
