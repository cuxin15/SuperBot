# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
# from io import BytesIO
# import time

# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# driver.get('https://openweathermap.org/widgets-constructor')

# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(
#         (By.ID, 'container-openweathermap-widget-11'))
# )
# ele = driver.find_elements_by_xpath('/html/body/main')
# total_height = ele[0].size["height"]+1000

# driver.set_window_size(1920, total_height)  # the trick
# time.sleep(2)

# element = driver.find_element_by_id('container-openweathermap-widget-11')
# location = element.location
# size = element.size


# png = driver.get_screenshot_as_png()
# driver.quit()

# im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']


# im = im.crop((left, top, right, bottom))  # defines crop points
# im.save('screenshot.png')  # saves new cropped image


#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_fullpage_screenshot():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://openweathermap.org/widgets-constructor")
    time.sleep(2)

    #the element with longest height on page
    ele = driver.find_element(
        "xpath", '/html/body/main')
    total_height = ele.size["height"]+1000

    driver.set_window_size(1920, total_height)  # the trick
    time.sleep(2)


    element = driver.find_element_by_id('container-openweathermap-widget-11')
    location = element.location
    size = element.size


    x = location['x']
    y = location['y']
    
    driver.save_screenshot("screenshot1.png")
    driver.quit()

    width = location['x']+size['width']
    height = location['y']+size['height']
    im = Image.open('screenshot1.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save('screenshot1.png')

if __name__ == "__main__":
    test_fullpage_screenshot()
