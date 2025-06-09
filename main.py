from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import logging
from datetime import datetime

logging.basicConfig(
    filename='automation_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

logging.info("--- Starting new automation run ---")

options = Options()
options.add_argument("--mute-audio")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

try:
    logging.info("Initializing Chrome WebDriver.")
    driver = webdriver.Chrome(options=options)

    url = 'https://www.youtube.com/@RoamingBoi/shorts'
    logging.info(f"Navigating to URL: {url}")
    driver.get(url)

    time.sleep(5)

    actions = ActionChains(driver)

    i = 0
    while i < 15:
        log_message = f"Scrolling to next video... ({i + 1}/15)"
        print(log_message)
        logging.info(log_message)

        actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(15)
        i = i + 1

except Exception as e:
    error_message = f"An error occurred: {e}"
    print(error_message)
    logging.error(error_message)
    driver.save_screenshot('error_screenshot.png')

finally:
    logging.info("Automation finished. Closing driver.")
    logging.info("--- End of automation run ---\n")
    print("Automation finished. Closing driver.")
    if 'driver' in locals() and driver:
        driver.quit()