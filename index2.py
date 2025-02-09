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
if response.status_code != 200:
    print(f"Request Error: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Extraction des entreprises
companies_list = soup.find_all(class_='mdl-card__title-text')

for company in companies_list:
    span = company.find('span')
    if span:
        companies.append(span.text.strip())

companies = companies[::2]  # Garder une entreprise sur deux

# Extraction des noms de lancements
names_list = soup.find_all(class_='header-style')

for name in names_list:
    names.append(name.text.strip())

# Extraction des dates et heures
datenhours = soup.find_all(class_='mdl-card__supporting-text')

for date_and_hour in datenhours:
    span = date_and_hour.find('span')
    if span:
        date_and_hours.append(span.text.strip())
    else:
        txt = str(date_and_hour.text.strip())
        clean = txt.split("\n")[0].strip() 
        date_and_hours.append(clean)

# Traitement des dates et heures
for text in date_and_hours:
    if re.search(r"\d{2}:\d{2}", text):  # Cas avec heure
        parts = text.split(" ")
        date_part = " ".join(parts[:4])
        time_part = parts[4]
        dates.append(date_part)
        times.append(time_part)
    else:  # Cas sans heure
        date_part = text.replace("NET", "").strip()
        dates.append(date_part)
        times.append(None)

# Créer le fichier JSON avec les données extraites
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
