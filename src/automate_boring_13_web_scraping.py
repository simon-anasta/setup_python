# Notes made during chapter 13 of Automate the Boring Stuff With Python
# 2025-12-02

# %% Download web pages -------------------------------------------------------

import requests

# fetch
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

type(response)
# success
response.status_code == requests.codes.ok

# contents
len(response.text)
print(response.text[:100])

# error if not conected
response.raise_for_status()

# write to disk
# binary format (wb) to preserve unicode
with open('temp_file.txt', 'wb') as output_file:
    # iterate through bites
    for chunk in response.iter_content(100000):
        output_file.write(chunk)

# %% Fetch from API -----------------------------------------------------------

# APIs are URLs with specific format that return specific results
# URLs are called 'endpoints'
# Read API documentation first
# may need to register for an API key

# example API fetch 1 - longitude and latitude from city name
response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')

response.text # is a text string

import json
response_data = json.loads(response.text) # Python data structure

# example API fetch 2 - weather from long and lat
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')

response_data = json.loads(response.text)
response_data['main']['temp'] # temperature
response_data['weather'][0]['main']

# %% Parsing HTML with Beautiful Soup -----------------------------------------

# do not use regex to parse HTML >> nightmares
# use specialist package

# uv pip beautifulsoup4
import bs4

res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()
example_soup = bs4.BeautifulSoup(res.text, 'html.parser')
type(example_soup)

# can then retrieve using CSS selector
example_soup.select('p') # elements named p (paragraph)
example_soup.select('#author') # has id attribute author
example_soup.select('.notice') # class attribute notice
example_soup.select('div span') # span within div
example_soup.select('div > span') # span immediately within div
# and others

# best way to figure out what you want is to inspect the webpage


# %% Control your browser - Selenium ------------------------------------------

# Helps hide this access is a script not a user

from selenium import webdriver

brower = webdriver.Firefox()
type(browser)
browser.get(URL)

# similar CSS options for finding elements
# or clicking buttons

# %% Control your browser - Playwright ----------------------------------------

# newer than Selenium
# can run in headless mode (no browser window open)

from playwright.sync_api import sync_playwright

# launches headless by default
with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()
    page.goto('https://autbor.com/example3.html')
    print(page.title())
    browser.close()

# launch interactively
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
# slowmo adds a delay to operations
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
browser.close()
playwright.stop()

# range of options for
# finding elements on page
# clicking elements on page
# filling out or submitting forms
# sending special keys

