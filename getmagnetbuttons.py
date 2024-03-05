from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the Firefox GeckoDriver executable
GECKO_DRIVER_PATH = r'C:\Users\Chris\Documents\geckodriver.exe'

# URL of the webpage to scrape
url = 'https://eztvx.to/shows/576958/solo-leveling/'

# Set Firefox options to bypass geckodriver path check
options = webdriver.FirefoxOptions()
options.set_preference("webdriver.gecko.driver", GECKO_DRIVER_PATH)

# Initialize Firefox WebDriver
driver = webdriver.Firefox(options=options)

try:
    # Open the webpage
    driver.get(url)

    # Find and click the "Show Links" button using the HTML <button> tag
    show_links_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))
    )
    show_links_button.click()

    # Wait for the magnet links to load
    magnet_links = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[starts-with(@href, 'magnet:')]"))
    )

    # Save magnet links to a text file
    with open('magnet_links.txt', 'w') as f:
        for link in magnet_links:
            f.write(link.get_attribute('href') + '\n')

finally:
    # Close the WebDriver session
    driver.quit()
