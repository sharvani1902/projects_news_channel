from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_live_news():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    results = []

    channels = {
        "Republic World": "https://www.youtube.com/@RepublicWorld/live",
        "India Today": "https://www.youtube.com/@indiatoday/live",
        "NDTV": "https://www.youtube.com/@ndtv/live",
        "Times Now": "https://www.youtube.com/@TimesNow/live",
        "WION": "https://www.youtube.com/@WION/live"
    }

    wait = WebDriverWait(driver, 10)

    for name, url in channels.items():
        driver.get(url)

        try:
            title_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h1//yt-formatted-string"))
            )
            title = title_element.text
        except:
            title = "Not Live / Title Not Found"

        results.append({
            "channel": name,
            "title": title
        })

    driver.quit()
    return results