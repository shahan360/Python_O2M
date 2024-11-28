# Documentation for the selenium package: https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Specify the path to the ChromeDriver executable
chromedriver_path = './chromedriver'

# Create a Service object with the path to the ChromeDriver
service = Service(executable_path=chromedriver_path)

# Initialize the Chrome WebDriver
chrome_browser = webdriver.Chrome(service=service)

# Maximize the browser window
chrome_browser.maximize_window()

# Open Reddit's r/cscareerquestions subreddit
chrome_browser.get('https://www.reddit.com/r/cscareerquestions/')

# Wait for the page to load and display trending posts
try:
    # Wait until the posts are loaded (you might need to adjust the selector based on Reddit's structure)
    WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.Post"))
    )

    # Find and print the titles of the top 25 posts
    posts = chrome_browser.find_elements(By.CSS_SELECTOR, "div.Post")[:25]
    for index, post in enumerate(posts, start=1):
        title_element = post.find_element(By.CSS_SELECTOR, "h3")
        print(f"Post {index}: {title_element.text}")

finally:
    # Close the browser after printing the post titles
    chrome_browser.quit()