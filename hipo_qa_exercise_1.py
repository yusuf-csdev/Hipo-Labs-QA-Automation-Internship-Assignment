# imported time module for time.sleep() method which will help to keep track of the steps clearly
# also to make sure that we do not test a page which is not loaded yet
import time
from selenium import webdriver

"""
  Project done by Yusuf Tamince for Hipo Labs QA Automation Internship position. This is part 1 of the given assingment.
"""

# Step 0: create driver object using selenium and maximize the browser window
driver = webdriver.Firefox()
driver.maximize_window()

# Step 1: go to google.com.tr
driver.get("https://www.google.com.tr")

# Step 2: verify that it is Google TR
current_page = driver.current_url
assert "google.com.tr" in current_page, "The current page is not Google TR"

# Step 3: search for "Hipo Labs"
search = driver.find_element_by_name("q")
search.send_keys("Hipo Labs")
search.submit() 
time.sleep(3) 

# Step 4: verify hipolabs.com is listed
search_results = driver.find_elements_by_tag_name("cite")
for site in search_results:
  if "hipolabs.com" in site.text:   
    break
else:
  assert False, "hipolabs.com is not listed in google search results"

# Step 5: open hipolabs.com
driver.get("https://www.hipolabs.com")

# Step 6: find and open team menu
team_menu = driver.find_element_by_xpath("//li[@id='menuMaximizedButtonTeam']/a").get_attribute("href")
time.sleep(3)
driver.get(team_menu)

# Step 7: find and follow "APPLY FOR JOBS" link
# make sure that the whole page gets loaded
driver.execute_script("window.scrollTo(0, 10800);") 
time.sleep(3)
driver.find_element_by_id("pageTeamApplynowButton").click()

# Step 8: verify that the page has "APPLY NOW" text
# take the screenshot when APPLY NOW is visible
# make sure that we are applying on a subpage of hipolabs.com
current_page = driver.current_url
assert "hipolabs.com" in current_page, "The current page is not from hipolabs.com"
driver.execute_script("window.scrollTo(0, 10800);")
time.sleep(3)
assert "APPLY NOW" in driver.page_source, "APPLY NOW text does not exist on the webpage"

# Step 9: take a screenshot and save it
driver.save_screenshot("screenshot.png")

# Step 10: check the link of "APPLY NOW" button and verify that it leads to "mailto:jobs@hipolabs.com"
apply_now_button_link = driver.find_element_by_class_name("hipo-jobs-open-position-apply-button-link").get_attribute("href")
assert apply_now_button_link == "mailto:jobs@hipolabs.com", f"The address on the button leads to {apply_now_button_link}, which is not 'mailto:jobs@hipolabs.com'"

# Step 11: click on the "APPLY NOW" button 
driver.get(apply_now_button_link)

# Step 12: quit the driver
driver.quit()