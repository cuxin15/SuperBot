from PIL import Image
from io import BytesIO

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def element_screenshot(location='', apikey='', eleLongestHeight='', by1='', eleScreenshot='', by2='', img_name='screenshot.png'):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://openweathermap.org/widgets-constructor")
    time.sleep(2)

    # the element with longest height on page
    ele = driver.find_element(by1, eleLongestHeight)
    total_height = ele.size["height"]+1000

    driver.set_window_size(1920, total_height)  # the trick
    time.sleep(2)

    inputElementApiKey = driver.find_element_by_id('api-key')
    inputElementApiKey.clear()
    inputElementApiKey.send_keys(apikey)

    inputEleLocation = driver.find_element_by_id('city-name')
    inputEleLocation.clear()
    inputEleLocation.send_keys(location+', VN')

    buttonEleSearch = driver.find_element_by_id('search-city').click()
    time.sleep(5)

    element = driver.find_element(by2, eleScreenshot)  # important
    location = element.location
    size = element.size

    x = location['x']
    y = location['y']

    png = driver.get_screenshot_as_png()
    driver.quit()

    im = Image.open(BytesIO(png))  # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save(img_name)


if __name__ == "__main__":
    im = element_screenshot(location='thanh pho Ho Chi Minh',
                       apikey='0092e33dc81d0caadd56e552dacd5717',
                       eleLongestHeight='/html/body/main',
                       by1='xpath',
                       eleScreenshot='container-openweathermap-widget-11',
                       by2='id',
                       img_name='xin.png')


