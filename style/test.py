import re
import glob

# Définir le motif de recherche
pattern = r'#343a40'  # Le motif que vous recherchez dans les fichiers CSS

# Le texte de remplacement
replacement = '#004aad'  # Le texte par lequel vous souhaitez remplacer le motif trouvé

# Spécifiez le répertoire où vous souhaitez rechercher les fichiers CSS
directory = r'C:\wamp64\www\portfolio\style'

# Utilisez la bibliothèque glob pour obtenir la liste de tous les fichiers .css
css_files = glob.glob(f"{directory}/*.css")

for file in css_files:
    with open(file, 'r') as f:
        css_content = f.read()

    # Effectuer la recherche et la substitution
    modified_css = re.sub(pattern, replacement, css_content)

    # Écrire le CSS modifié dans le fichier
    with open(file, 'w') as f:
        f.write(modified_css)

print('Remplacement terminé avec succès.')


