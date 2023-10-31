from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


# Initialize the WebDriver (replace 'chromedriver.exe' with your browser's WebDriver)

chrome_options = webdriver.ChromeOptions()
"""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "c:/Users/salih/StudioProjects/salihnuman_test"
})
"""
chrome_options.add_argument("--user-data-dir=C:/Users/salih/AppData/Local/Google/Chrome/User Data")     # To change for each PC
chrome_options.add_argument("--profile-directory=Default")


driver = webdriver.Chrome(executable_path="chromedriver-win64\chromedriver.exe", options=chrome_options)
actions = ActionChains(driver)

# Open the website with the form
driver.get('https://sonuc.ysk.gov.tr/')



# Find and select an option from the first dropdown
types = driver.find_elements(By.CLASS_NAME, 'col-md-6')
types[-1].click()

time.sleep(5)

# Get the dropdown list for the election name
driver.find_element(By.CLASS_NAME, 'ng-arrow-wrapper').click()
time.sleep(1)
dropdown1List = driver.find_elements(By.CLASS_NAME, 'ng-option')

dropdown1List[5].click()                                        # Change List element according to the election

time.sleep(3)

# Choose the type of result (Genel sonuçlar / Yurt İçi / Yurt Dışı), click to "devam et"
## Yurt içi seçiyorum sadece ilçelere bakacağımızı varsayarak
options = driver.find_elements(By.CLASS_NAME, 'form-check')
options[1].click()
driver.find_element(By.CLASS_NAME, 'btn-success').click()

time.sleep(5)

# Choose the city
scroll_pixels = -700  # A negative value indicates scrolling upwards
driver.execute_script(f'window.scrollBy(0, {scroll_pixels});')               # scroll to the place of the dropdown lists
time.sleep(1)

dropdowns = driver.find_elements(By.CLASS_NAME, 'ng-arrow-wrapper')

dropdowns[1].click()                        # Cities listed
time.sleep(1)
cityList = driver.find_elements(By.CLASS_NAME, 'ng-option')

file = open("output.txt", "w")

# Loop through the cities
for index in range(79, 81):             # :: CHANGE HERE ::
    cityList = driver.find_elements(By.CLASS_NAME, 'ng-option')
    print("Retrieving the results for the city " + str(index+1) + ": " + cityList[index].text)
    file.write("Retrieving the results for the city " + str(index+1) + ": " + cityList[index].text + "\n")

    actions.move_to_element(cityList[index])                   # Move to the city in order to click it
    cityList[index].click()
    # Choose the district
    time.sleep(4)
    dropdowns[2].click()
    time.sleep(1)
    districtList = driver.find_elements(By.CLASS_NAME, 'ng-option')

    # Loop through the districts of the city
    for index2, district in enumerate(districtList):
        districtList = driver.find_elements(By.CLASS_NAME, 'ng-option')
        print("Retrieving the results for the  district " + str(index2+1) + ": " + districtList[index2].text)
        file.write("Retrieving the results for the  district " + str(index2+1) + ": " + districtList[index2].text + "\n")
        
        actions.move_to_element(districtList[index2])
        districtList[index2].click()
        time.sleep(4)
        # Click on "Sorgula"
        searchIconElements = driver.find_elements(By.CLASS_NAME, 'icon-flaticon1541572461-svg')
        try:
            searchIconElements[-1].click()
        except Exception as e:
            print("-------------------- FAILED TO CLICK ON SORGULA FOR THIS DISTRICT --------------------")
            print(e)
            file.write("-------------------- FAILED TO CLICK ON SORGULA FOR THIS DISTRICT --------------------\n")
            file.write(e + "\n")
        
        time.sleep(6)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


        # Click on "Tabloyu Kaydet"
        try:
            element = driver.find_element(By.CLASS_NAME, 'icon-excel')
            element.click()
            time.sleep(1)
            buttons = driver.find_elements(By.TAG_NAME, 'button')
            buttons[-2].click()
            time.sleep(3)
        except Exception as e:
            print("-------------------- FAILED TO PRESS THE BUTTON TO DOWNLOAD THE TABLE FOR THIS DISTRICT. --------------------")
            print(e)
            file.write("-------------------- FAILED TO PRESS THE BUTTON TO DOWNLOAD THE TABLE FOR THIS DISTRICT. --------------------\n")
            file.write(e + "\n")
        
        # Scroll up and click on the district dropdown again      
        scroll_pixels = -900  # A negative value indicates scrolling upwards
        driver.execute_script(f'window.scrollBy(0, {scroll_pixels});')               # scroll to the place of the dropdown lists
        time.sleep(1)
        dropdowns[2].click()
        time.sleep(1)

    dropdowns[2].click()
    dropdowns[1].click()
    print("")
    print("")
    file.write("\n")
    file.write("\n")
time.sleep(5)

# Close the webdriver
driver.quit()
file.close()