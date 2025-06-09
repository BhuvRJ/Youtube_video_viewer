from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# OPTIONAL: Set path to chromedriver if not in PATH
# service = Service("/usr/local/bin/chromedriver")  # adjust if needed

options = Options()
options.add_argument("--mute-audio")
options.add_argument("--headless")  # comment out if you want to see browser
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

# Use this if chromedriver path is needed
# driver = webdriver.Chrome(service=service, options=options)

# Use this if chromedriver is already accessible via PATH
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)
time.sleep(5)

driver.get('https://www.youtube.com/@RoamingBoi')

try:
    actions = ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR,
                                  "#content > ytm-shorts-lockup-view-model-v2 > ytm-shorts-lockup-view-model > a > div > img")
    element.click()
    i = 0
    while i < 15:
        print("Moving to next video")
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        i = i + 1

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
