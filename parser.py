import json

# Charge ton fichier JSON
with open('launch_data1.json', 'r') as file:
    data = json.load(file)

# Liste des mots à détecter
spacex_words = ['falcon']
mhi_words = ['Michibiki']
rocketlab_words = ['Electron', 'Curie']
casc_words = ['casc', 'chang', 'march march', 'zheng']
ariane_words = ['ariane', 'vega']
isro_words = ['isro', 'lvm', 'PSLV', 'SSLV']
roscosmos_words = ['soyuz']
ula_words = ['atlas']
blueorigin_words = ['new glenn', 'new-glenn', 'glenn']
orbitalscience_words = ['minotaur']

# Fonction pour détecter les mots dans la clé 'name' et attribuer la valeur à 'company'
def detecter_mots_et_attribuer_company(data, spacex_words):
    for item in data:
        if 'name' in item:
            nom = item['name'].lower()  # Mettre en minuscules pour éviter la casse
            company_value = "???"  # Valeur par défaut
            for mot in spacex_words:
                if mot.lower() in nom:  # Vérifier si le mot est dans le nom
                    company_value = "SpaceX"
                    break
            for mot in mhi_words:
                if mot.lower() in nom: 
                    company_value = "MHI"
                    break 
            for mot in rocketlab_words:
                if mot.lower() in nom: 
                    company_value = "Rocket Lab"
                    break 
            for mot in casc_words:
                if mot.lower() in nom: 
                    company_value = "CASC"
                    break 
            for mot in ariane_words:
                if mot.lower() in nom:
                    company_value = "Arianespace"
                    break
            for mot in isro_words:
                if mot.lower() in nom:
                    company_value = "ISRO"
                    break
            for mot in roscosmos_words:
                if mot.lower() in nom:
                    company_value = "Roscosmos"
                    break
            for mot in ula_words:
                if mot.lower() in nom:
                    company_value = "ULA"
                    break
            for mot in blueorigin_words:
                if mot.lower() in nom:
                    company_value = "Blue Origin"
                    break
            for mot in orbitalscience_words:
                if mot.lower() in nom:
                    company_value = "Orbital Science"
                    break
            item['company'] = company_value  # Ajouter ou mettre à jour la clé 'company'

    return data

# Appel de la fonction
data_mise_a_jour = detecter_mots_et_attribuer_company(data, spacex_words)

# Enregistrer les résultats mis à jour dans un nouveau fichier JSON
with open('launch_data1_updated.json', 'w') as file:
    json.dump(data_mise_a_jour, file, indent=4)  # Utilisation de indent=4 pour une lecture plus facile

# Affichage des résultats mis à jour
for item in data_mise_a_jour:
    print(item)
