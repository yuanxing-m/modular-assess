from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from config import path_chromedriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

# Provide the path of chromedriver present on your system.
driver = webdriver.Chrome(executable_path=path_chromedriver,
                          chrome_options=options)

url = "https://www.ccilindia.com/FPI_ARCV.aspx"

wait = WebDriverWait(driver, 30)
driver.get(url)
driver.maximize_window()

select = Select(driver.find_element('name','drpArchival'))
options = select.options
dates = []
for opt in options:
    if "Select" not in opt.text:
        dates.append(opt.text)
for d in dates:
    select = Select(driver.find_element('name', 'drpArchival'))
    select.select_by_visible_text(d)
    driver.find_element('name', "btnFPISWH").click()


driver.close()
