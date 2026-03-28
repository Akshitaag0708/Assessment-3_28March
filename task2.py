from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# launching browser
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
# opening the webpage
driver.get("https://www.myntra.com/")
# Maximize browser window
driver.maximize_window()
# Apply implicit wait (wait up to 10 seconds for elements to appear)
driver.implicitly_wait(10)
# Create ActionChains object for advanced user interactions
actions = ActionChains(driver)
# Locate a product element using XPath
ele=driver.find_element(By.XPATH,"(//div[@class='desktop-navContent'])[6]")
# Perform the hover action
actions.move_to_element(ele).perform()
# Locate a product element using LINK_TEXT
ele2=driver.find_element(By.LINK_TEXT , "Jackets Under ₹899")
# Click the 'Jackets Under ₹899' link
actions.click(ele2).perform()
# Locate a product element using XPath
check1=driver.find_element(By.XPATH,"(//div[@class='common-checkboxIndicator'])[10]")
# click on checkbox
actions.click(check1).perform()
# Locate a product element using XPath
check2=driver.find_element(By.XPATH,"//span[@class='colour-label colour-colorDisplay']/..//div")
# click on checkbox
actions.click(check2).perform()
# Locate a product element using XPath
ele2=driver.find_element(By.XPATH , "//div[@class='sort-sortBy']")
# Hover over the 'Sort By' dropdown
actions.move_to_element(ele2).perform()
# locate and click on popularity
driver.find_element(By.XPATH , "//ul[@class='sort-list']//li[3]").click()
# Locate a product element using XPath
pdt=driver.find_element(By.XPATH,"//ul[@class='results-base']//li")
# perform click on first product
actions.click(pdt).perform()
# switches to new tab
driver.switch_to.window(driver.window_handles[1])
# Locate a product element using XPath
size=driver.find_element(By.XPATH,"//div[@class='size-buttons-size-buttons']//div")
# click on size
actions.click(size).perform()
#locate and click on add to bag
driver.find_element(By.XPATH,"//span[@class='myntraweb-sprite pdp-whiteBag sprites-whiteBag pdp-flex pdp-center']").click()
# Wait to see the result before closing
sleep(2)
# Close the browser
driver.quit()


