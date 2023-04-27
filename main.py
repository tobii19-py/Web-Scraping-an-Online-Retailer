from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
  # Configure browser options
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver

def main():
  driver = get_driver()
  
  driver.find_element(by="id", value="CustomerEmail").send_keys("t.apps.python@gmail.com")
  time.sleep(1)
  driver.find_element(by="id", value="CustomerPassword").send_keys("authenthicpy" + Keys.RETURN)
  time.sleep(1)

  # Select contact us
  driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
  print(driver.current_url)

print(main())