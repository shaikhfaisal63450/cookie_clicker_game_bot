# from selenium import webdriver
#
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
#
# chrome_option  = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_option)
# #navigate to wikipedia
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # article_count = driver.find_element(By.CSS_SELECTOR, value = "#articlecount a")
# # article_count.click()
#
# #Find element by link Text
# all_portal = driver.find_element(By.LINK_TEXT, value="Reference desk")
# #all_portal.click()
#
# search = driver.find_element(By.NAME, value="search")
#
# #Sending Keyboard input to selenium
# search.send_keys("Python")
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchInput"))
)
search.send_keys("Python", Keys.RETURN)

# Wait only for presence (NOT clickable)

# Now interact manually
# search.click()
# search.clear()
search.send_keys("Python", Keys.RETURN)
