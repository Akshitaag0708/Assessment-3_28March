from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Launch the browser
o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
# opening the webpage
driver.get("https://www.shoppersstack.com/")
# Maximize browser window
driver.maximize_window()
# Apply implicit wait (wait up to 10 seconds for elements to appear)
driver.implicitly_wait(10)
# Static wait to allow page to fully load
sleep(5)
# Create ActionChains object for advanced user interactions
actions = ActionChains(driver)
# Locate a product element using XPath
ele=driver.find_element(By.XPATH,"//div[@class='featuredProducts_cardContainer__r2Ou6']//div//div")
# Move mouse to the element, pause for 2 seconds, and click on it
actions.move_to_element(ele).pause(2).click(ele).perform()
# Create explicit wait object (max wait time: 20 seconds)
wait=WebDriverWait(driver,20)
# Wait until the delivery input field is visible, then locate it
ele2=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='Check Delivery']")))
# Enter pincode into delivery field
ele2.send_keys("303702")
# Pause to observe the action
sleep(3)
# Wait until the "Check" button is visible
ele3=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='Check']")))
# Click on the "Check" button
ele3.click()
# Wait to see the result before closing
sleep(5)
# Close the browser
driver.quit()










