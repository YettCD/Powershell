import requests
from bs4 import BeautifulSoup
import concurrent.futures
import csv

def extract_magnet_links(url, primary_keywords, secondary_keywords):
    try:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        magnet_links_set = set()  # Using a set to store unique magnet links

        # Extract magnet links from the page content
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('magnet:'):
                parts = href.split('&')  # Split the magnet link into parts
                combined_parts = ''.join(parts)  # Combine parts into a single string
                # Check if any primary keyword is present in the combined parts
                if all(keyword in combined_parts for keyword in primary_keywords):
                    magnet_links_set.add(href)  # Add the magnet link to the set

        # If no magnet links are found using primary keywords, try secondary keywords
        if not magnet_links_set:
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('magnet:'):
                    parts = href.split('&')  # Split the magnet link into parts
                    combined_parts = ''.join(parts)  # Combine parts into a single string
                    # Check if any secondary keyword is present in the combined parts
                    if all(keyword in combined_parts for keyword in secondary_keywords):
                        magnet_links_set.add(href)  # Add the magnet link to the set

        return list(magnet_links_set)  # Convert set back to list before returning

    except Exception as e:
        print("An error occurred:", str(e))
        return []

def process_url(url, primary_keywords, secondary_keywords, output_file):
    try:
        print(f"Processing URL: {url}")
        magnet_links = extract_magnet_links(url, primary_keywords, secondary_keywords)
        with open(output_file, 'a', newline='') as f:
            csv_writer = csv.writer(f)
            for magnet_link in magnet_links:
                csv_writer.writerow([url, magnet_link])
    except Exception as e:
        print(f"An error occurred while processing {url}: {str(e)}")

def main():
    main_url = 'https://en.torlock-official.site/series/the-rookie-2018'
    reqs_main = requests.get(main_url, timeout=10)
    reqs_main.raise_for_status()
    soup_main = BeautifulSoup(reqs_main.text, 'html.parser')

    # Extract all the URLs from the main webpage
    urls = []
    for link in soup_main.find_all('a', href=True):
        href = link['href']
        # Add an additional condition to filter URLs
        if '/episodes/' in href:
            urls.append(href)

    primary_keywords = ['1080p', 'WEB']  # Primary keywords to filter magnet links
    secondary_keywords = ['720p', 'WEB']  # Secondary keywords to filter magnet links
    output_file = 'therookiemagnetlinks.csv'  # Output file name

    with open(output_file, 'w', newline='') as f:  # Open file in write mode
        csv_writer = csv.writer(f)
        csv_writer.writerow(['URL', 'Magnet Link'])  # Write header row

    # Limit the number of threads to 5
    max_threads = 1

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        for url in urls:
            future = executor.submit(process_url, url, primary_keywords, secondary_keywords, output_file)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    print(f"Magnet links saved to {output_file}")

if __name__ == "__main__":
    main()
