from selenium import webdriver

# Set the path to the Firefox GeckoDriver executable
GECKO_DRIVER_PATH = r'C:\Users\Chris\Documents\geckodriver.exe'

# Set Firefox options to bypass geckodriver path check
options = webdriver.FirefoxOptions()
options.set_preference("webdriver.gecko.driver", GECKO_DRIVER_PATH)

# Initialize Firefox WebDriver
driver = webdriver.Firefox(options=options)

try:
    # Open the webpage
    driver.get('https://eztvx.to/shows/576958/solo-leveling/')

    # Wait for user interaction
    input("Press Enter to close the browser...")

finally:
    # Close the WebDriver session
    driver.quit()
