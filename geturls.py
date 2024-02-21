import requests
from bs4 import BeautifulSoup
import re
import time


def extract_magnet_links(url, keyword):
    try:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        magnet_links_set = set()

        # Extract magnet links from the page content
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('magnet:'):
                parts = href.split('&')  # Split the magnet link into parts
                for part in parts:
                    if keyword in part:
                        magnet_links_set.add(href)
                        

        return list(magnet_links_set)
    
    except Exception as e:
        print("An error occurred:", str(e))
        return []

def main():
    main_url = 'https://en.torlock-official.site/series/archer-2009'
    reqs_main = requests.get(main_url, timeout=10)
    reqs_main.raise_for_status()
    soup_main = BeautifulSoup(reqs_main.text, 'html.parser')

    mag_file = 'ArcherMagnetLinks.txt'
    keyword = '1080p'
    

    # Extract all the URLs from the main webpage
    urls = []
    for link in soup_main.find_all('a', href=True):
        href = link.get('href') or link['href']
        if href and '/episodes/' in href:
            urls.append(href)

    with open(mag_file, 'w') as f:  # Open file in write mode
        # Visit each URL and extract magnet links
        for url in urls:
            try:
                print(f"Processing URL:{url}")
                magnet_links = extract_magnet_links(url, keyword)
                if magnet_links:
                    f.write(f"Magnet links containing '{keyword}' from {url}:\n")
                    for magnet_link in magnet_links:
                        f.write(magnet_link + '\n')
                    f.write('\n')  # Add a newline after each URL's magnet links
                time.sleep (1)
            except Exception as e:
                print(f"An error occurred while processing {url}: {str(e)}")

    print(f"Magnet links saved to {mag_file}")

if __name__ == "__main__":
    main()