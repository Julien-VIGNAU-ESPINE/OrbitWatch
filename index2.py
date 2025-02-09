import requests
from bs4 import BeautifulSoup
import json
import re

companies = []
names = []
date_and_hours = []
dates = []
times = []

response = requests.get("https://nextspaceflight.com/launches/")
if response.status_code == 200:
    print("Request successful !")
else:
    print(f"Request Error: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')
if soup:
    print("Parsing successful !")

companies_list = soup.find_all(class_='mdl-card__title-text')

for company in companies_list:
    span = company.find('span')
    if span:
        companies.append(span.text.strip())

companies = companies[::2]
print(companies)

names_list = soup.find_all(class_='header-style')

for name in names_list:
    # Récupérer le texte de chaque élément, supprimer les espaces inutiles
    names.append(name.text.strip())

# Afficher les résultats
print(names)

datenhours = soup.find_all(class_='mdl-card__supporting-text')

for date_and_hour in datenhours:
    span = date_and_hour.find('span')
    if span:
        date_and_hours.append(span.text.strip())
    else :
        txt = str(date_and_hour.text.strip())
        clean = txt.split("\n")[0].strip() 
        date_and_hours.append(clean)

print(date_and_hours)


for text in date_and_hours:
    # Cas 1 : Format complet avec date et heure
    if re.search(r"\d{2}:\d{2}", text):  # Vérifie s'il y a une heure (format HH:MM)
        parts = text.split(" ")
        date_part = " ".join(parts[:4])  # Prend les parties pour la date (ex. Thu Jan 16, 2025)
        time_part = parts[4]  # Prend la partie de l'heure (ex. 06:00)
        dates.append(date_part)
        times.append(time_part)
    # Cas 2 : Format avec seulement date
    else:
        date_part = text.replace("NET", "").strip()  # Enlève "NET" et nettoie
        dates.append(date_part)
        times.append(None)  # Pas d'heure pour ce cas


print (dates)
print(times)


print (len(companies))
print (len(names))
print (len(date_and_hours))
print (len(dates))
print (len(times))

# Create a json file and store the data
data = []
for i in range(len(names)):
    data.append({
        'company': companies[i],
        'name': names[i],
        'date': dates[i],
        'hour': times[i]
    })

with open('launch_data2.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)