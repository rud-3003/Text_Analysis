import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Define paths
base_folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(base_folder, '../Input.xlsx')
output_folder = os.path.join(base_folder, '../ExtractedTexts')

os.makedirs(output_folder, exist_ok=True)

def extract_text_from_url(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "No Title"
        paragraphs = soup.find_all('p')
        content = ' '.join(p.get_text(strip=True) for p in paragraphs)

        
        return title + "\n\n" + content
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return ""

input_df = pd.read_excel(input_file)

# Loop through each URL and save the extracted text
for _, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    article_text = extract_text_from_url(url)

    with open(os.path.join(output_folder, f"{url_id}.txt"), 'w', encoding='utf-8') as file:
        file.write(article_text)

    print(f"Article {url_id} saved.")
