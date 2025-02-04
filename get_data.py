import os
import requests
import zipfile
import gzip
import shutil

# URL de base
base_url = "https://commondatastorage.googleapis.com/clusterdata-2011-2"

# Créer le répertoire 'data' si nécessaire
if not os.path.exists('data'):
    os.makedirs('data')

# Ouvrir le fichier texte et lire chaque ligne
with open('extracted_links.txt', 'r') as file:
    for line in file:
        # Supprimer les espaces blancs et les nouvelles lignes
        line = line.strip()
        
        # Utiliser os.path.join pour construire l'URL complète
        file_url = os.path.join(base_url, line)
        
        # Nom du fichier de destination (dans le répertoire 'data')
        if '/' in line:
            base_directory = os.path.join('data',line.split('/')[0])
            if not os.path.exists(base_directory):
                os.makedirs(base_directory)
        dest_file = os.path.join('data', line)
        
        try:
            # Télécharger le fichier
            response = requests.get(file_url, stream=True)
            response.raise_for_status()  # Vérifier si la requête a réussi
            
            # Enregistrer le fichier dans le répertoire 'data'
            with open(dest_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Fichier téléchargé avec succès : {dest_file}")

            # Vérifier si le fichier est un fichier .gz ou .zip et le décompresser
            if dest_file.endswith('.gz') or dest_file.endswith('.zip'):
                # Ouvrir et décompresser le fichier
                with open(dest_file, 'rb') as f_in:
                    if dest_file.endswith('.zip'):
                        # Pour les fichiers ZIP, on extrait leur contenu
                        with zipfile.ZipFile(f_in) as zip_ref:
                            zip_ref.extractall('data')  # Extraire dans le dossier 'data'
                            print(f"Fichier ZIP décompressé : {dest_file}")
                    elif dest_file.endswith('.gz'):
                        # Si c'est un fichier .gz, utiliser gzip pour l'extraction
                        with gzip.open(f_in, 'rb') as f_gz:
                            with open(dest_file[:-3], 'wb') as f_out:  # Supprime .gz du nom
                                shutil.copyfileobj(f_gz, f_out)
                            print(f"Fichier GZ décompressé : {dest_file}")
                
                # Supprimer le fichier .gz ou .zip original après extraction
                os.remove(dest_file)
                print(f"Fichier original supprimé : {dest_file}")

        except requests.exceptions.RequestException as e:
            print(f"Erreur lors du téléchargement du fichier {file_url}: {e}")
