from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create service object
service = Service(ChromeDriverManager().install())

# Start driver
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")