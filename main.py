import requests
from bs4 import BeautifulSoup
import os


def scrape_images(url):
    # Create a session to send requests
    session = requests.Session()

    # Set up the proxy
    proxy = {'http': 'http://<PROXY_IP>:<PROXY_PORT>', 'https': 'http://<PROXY_IP>:<PROXY_PORT>'}
    session.proxies.update(proxy)

    # Send the request to the website
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all images on the page
    images = soup.find_all('img')

    # Create folders to save images
    person_folder = 'person_wearing_clothes'
    fabric_folder = 'fabrics'
    os.makedirs(person_folder, exist_ok=True)
    os.makedirs(fabric_folder, exist_ok=True)

    # Loop through all images
    for image in images:
        src = image.get('src')
        alt = image.get('alt')

        # Check if the image is of a person wearing clothes
        if 'person' in alt.lower():
            img_data = session.get(src).content
            with open(os.path.join(person_folder, os.path.basename(src)), 'wb') as f:
                f.write(img_data)

        # Check if the image is of a fabric
        elif 'fabric' in alt.lower():
            img_data = session.get(src).content
            with open(os.path.join(fabric_folder, os.path.basename(src)), 'wb') as f:
                f.write(img_data)


# Example URL
url = 'https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204?webcat=men%7Cclothing%7Cmen-clothing-hoodies-sweatshirts'
scrape_images(url)

