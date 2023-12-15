import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.ntu.edu.sg/life-at-ntu/student-life/clubs-groups-societies/hall-councils'

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

halls_data = []

# Assuming each hall section is uniquely identified by a container having 'full container bg-blue'
halls_sections = soup.find_all('section', {'class': 'full container bg-blue'})

for section in halls_sections:
    hall_name = section.find('h5').text.strip()  # Assuming hall name is within an <h5> tag
    social_links = section.find('strong').find_all('a')
    
    data = {'Hall Name': hall_name}
    for link in social_links:
        if 'facebook' in link['href']:
            data['Facebook'] = link['href']
        elif 'instagram' in link['href']:
            data['Instagram'] = link['href']

    halls_data.append(data)

    
# Convert to DataFrame and save as CSV
df = pd.DataFrame(halls_data)
df.to_csv('ntu_halls_data.csv', index=False)

print("Data saved to ntu_halls_data.csv")
