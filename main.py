from selenium import webdriver
from selenium.webdriver.common.by import By


#keep chrome open
chrome_option  = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
price_rupee  = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
price_paisa = driver.find_element(By.CLASS_NAME, value = "a-price-fraction")
print(f"The price is {price_rupee.text}.{price_paisa.text}")

search_bar  = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID , value= "submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, value  = ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget time")
for times in event_times:
    print(times.text)
#
event_names = driver.find_elements(By.CSS_SELECTOR, value = ".event-widget li a ")
for names in event_names:
    print(names.text)
dict = {i :{event_times[i].text:event_names[i].text} for i in range(len(event_times))}
print(dict, "\n")

#driver.close()
driver.quit()
