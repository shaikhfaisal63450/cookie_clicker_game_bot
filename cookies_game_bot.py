from attr import attributes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

#keys attribute is used to clock on the web button/link as we do with the keyboard
#search_box.send_keys("Selenium web scraping tutorial" + Keys.ENTER)
#Keys.DELETE

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")

sleep(2)

#Find the big cookie to click
cookie = driver.find_element(By.ID, value="bigCookie")
item_ids = [f"product{i}" for i in range(18)]

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60*5

while True:
    cookie.click()

    #Every 5 second , try to buy the most expensive item we can afford
    if time() > timeout :
        try :
            cookies_element = driver.find_element(by = By.ID, value = "cookies")
            cookies_text = cookies_element.text
            #Extract number from text like "123 cookies"
            cookie_count = int(cookies_text.split()[0].replace(",", ""))

            #Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value = "div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except(NoSuchElementException, ValueError):
            print("couldn't find cookie count or items")
            
        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value = "cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("couldn't get final cookies count")
        break
driver.quit()