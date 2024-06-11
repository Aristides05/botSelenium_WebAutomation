from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

DEFAULT_DIR = "C:\\Users\\allan\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"
PROFILES = ["mm9kcsy8.GOMES", "wmtulw9d.STORE"]

TARGET_BASE = 'https://advertising.amazon.com.br/bulksheet/HomePage?entityId='
TARGET_PROFILE_ENTITY = ["ENTITYZA5DLHLE8215", "ENTITY1CYX8CNAV1RAA"]

def main():
    for i in range(len(PROFILES)):
        PROFILE = f'{DEFAULT_DIR}\\{PROFILES[i]}'
        TARGET = f'{TARGET_BASE}{TARGET_PROFILE_ENTITY[i]}'
        
        options = Options()
        options.add_argument("-profile")
        options.add_argument(PROFILE)

        driver = webdriver.Firefox(options=options)

        driver.get(TARGET)
        
        time.sleep(4)
        driver.quit()
        
main()