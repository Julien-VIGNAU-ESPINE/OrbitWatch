# SPACEFLIGHTS PARSER
# Author: Julien VIGNAU-ESPINE
# Date: 14-01-2025 21:03

# ============================================================================
# IMPORTS
# ============================================================================

import requests
from bs4 import BeautifulSoup
import json

# ============================================================================ #
# CONSTANTS
# ============================================================================ #
DESTINATION_ORBITE_URL = "https://destination-orbite.net/astronautique/lancements/calendrier/?utm_source=chatgpt.com"

def fetchLaunches_destination_orbite(url=DESTINATION_ORBITE_URL):
    """Scrap all the needed information from the web site"""
    launch_names = []
    launch_dates_and_hours = []
    launch_dates = []
    launch_hours = []

    # Request the web site
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Request Error: {response.status_code}")
        return [], [], []

    # Parse the web site
    soup = BeautifulSoup(response.text, 'html.parser')

    # Search for the launch entries
    launchs = soup.find_all(class_='row g-0 bg-dark')
    if not launchs:
        print("No launches found. Please check the HTML structure.")
        return [], [], []

    # Extract launch names, dates, and hours
    for launch in launchs:
        date_and_hours = launch.find('ul', class_='list-unstyled mt-5')
        if date_and_hours:
            items = date_and_hours.find_all('li')
            for item in items:
                launch_dates_and_hours.append(item.text.strip().split(": ")[1])

        name = launch.find('p', class_='bg-white text-dark p-3 fw-bold')
        if name:
            launch_names.append(name.text.strip())

    # Format the data
    for index in range(len(launch_dates_and_hours)):
        if index % 2 == 0:
            launch_dates.append(launch_dates_and_hours[index])
        else:
            launch_hours.append(launch_dates_and_hours[index])

    return launch_names, launch_dates, launch_hours

def save_launches_to_json(launch_names, launch_dates, launch_hours):
    """Create a json file and store the data"""
    if not launch_names or not launch_dates or not launch_hours:
        print("No data to save.")
        return

    data = []
    # Write the data in a json file
    for i in range(len(launch_names)):
        data.append({
            'name': launch_names[i],
            'date': launch_dates[i],
            'hour': launch_hours[i]
        })

    with open('launch_data1.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("Data saved in 'launch_data1.json'")

# ============================================================================ #
# MAIN
# ============================================================================ #

def main():
    # Fetch launch data
    launch_names, launch_dates, launch_hours = fetchLaunches_destination_orbite(DESTINATION_ORBITE_URL)

    # Save the data to JSON file
    save_launches_to_json(launch_names, launch_dates, launch_hours)

if __name__ == '__main__':
    main()