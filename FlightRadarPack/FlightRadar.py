from selenium import webdriver
import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='C:\\Users\\mahib\\chromedriver_win32\\chromedriver.exe', options=options)
driver.get('https://www.flightradar24.com/')
driver.maximize_window()

# consent
consent = driver.find_element(By.XPATH, '//*[@id="map"]/div[15]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
consent.click()

# cookie handling
cookie = driver.find_element(By.XPATH, "//button[text()='Accept Cookies']")
cookie.click()

action = ActionChains(driver)

# go to Airport Data tab
data = driver.find_element(By.XPATH, "//a[@id = 'navTopDataHistory']")
data.click()
airport = driver.find_element(By.XPATH, "//span[text() = 'Airports']")
airport.click()

# search Airport of choice
search = driver.find_element(By.XPATH, "//input[@id = 'searchAirport']")
search.send_keys("BHX")
action.move_to_element(driver.find_element(By.XPATH, "//span[@class = 'tt-dropdown-menu']")).click().perform()

# take screenshot after scroll down to Departures
departures = driver.find_element(By.XPATH, "//a[contains(@class, 'btn ') and text() = ' Departures ']")
departures.click()

wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[text() = 'Load later flights']")))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.save_screenshot("bhx_departure.png")

# web scrapping
dep_table = driver.find_element(By.XPATH, '//table[@class = "table table-condensed table-hover data-table m-n-t-15"]')
rows = len(dep_table.find_elements(By.XPATH, ".//tbody/tr[@class = 'hidden-xs hidden-sm ng-scope']"))
cols = len(dep_table.find_elements(By.XPATH, './/thead/tr/th'))

print("Time" + "       " + "Flight" + "      " + "To" + "      " + "Airline" + "      " + "Aircraft" + "       " + "Est. Dep")

# writing scraped table data into excel file
path = "C:\\Users\\mahib\\PycharmProjects\\FlightRadarDemo\\Book1.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        x = dep_table.find_element(By.XPATH,
                                   "//tbody/tr[@class = 'hidden-xs hidden-sm ng-scope'][" + str(r) + "]/td[" + str(
                                       c) + "]").text
        sheet.cell(row=r, column=c).value = x
        print(x, end='     ')
    print()

workbook.save(path)
