import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform

def setup_driver():
    chrome_options = Options()
    chrome_options.debugger_address = "127.0.0.1:9222"
    system = platform.system()
    if system == "Darwin":  # macOS
        chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    elif system == "Windows":  # Windows
        chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    elif system == "Linux":  # Linux
        chrome_options.binary_location = "/usr/bin/google-chrome"
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_video_element(driver, video_selector):
    try:
        video_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, video_selector))
        )
        print("Video found")
        return video_element
    except Exception as e:
        print(f"Error locating video: {e}")
        return None

def click_video(driver, video_element, duration=5):
    if not video_element:
        print("No video found")
        return
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            driver.execute_script("arguments[0].click();", video_element)
        except Exception as e:
            print(f"Error clicking video: {e}")
            break

def click_upgrades(driver, upgrade_selector, clicks=20, limit=5):
    try:
        upgrade_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, upgrade_selector))
        )
        upgrade_buttons = upgrade_elements[:limit]
        for button in upgrade_buttons:
            for _ in range(clicks):
                try:
                    driver.execute_script("arguments[0].click();", button)
                except Exception as e:
                    print(f"Error clicking upgrade button: {e}")
                    break
    except Exception as e:
        print(f"Error finding upgrade buttons: {e}")

def main():
    url = input("Enter URL: ") 
    driver = setup_driver()
    driver.get(url)
    time.sleep(5)

    video_selector = "video"
    upgrade_selector = ".buttonBuy"

    video_element = get_video_element(driver, video_selector)
    if not video_element:
        print("No video found")
        driver.quit()
        return
    try:
        while True:
            click_video(driver, video_element, duration=5)
            click_upgrades(driver, upgrade_selector, clicks=20, limit=5)
    except KeyboardInterrupt:
        print("Stopped")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
