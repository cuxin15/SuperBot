from Screenshot import Screenshot_Clipping
from selenium import webdriver


ob = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://openweathermap.org/widgets-constructor"
driver.get(url)
# Use full class name
Hide_elements = [
    'class=container-widget container-widget--11']
img_url = ob.get_element(
    driver, save_path=r'.', elements=Hide_elements, image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()
