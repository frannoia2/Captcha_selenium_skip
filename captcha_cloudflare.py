import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)   #no cierra la pantalla al acabar para ver resultado funciona
#todas estas opciones ayudan a que no sea tan automatico el navegador para parecer humano y evitar los captcha
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument("--no-sandbox")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options)
driver.execute_script("window.open('https://nowsecure.nl/', '_blank')")     #abre paginas manualmente en vez de get para simular humano (primero en blanco luego pag)
time.sleep(15)
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.frame(0)       #cambia de pag al pop up del captcha
driver.find_element(By.XPATH, '//*[@id="challenge-stage"]/div/label/input').click()    #pulsa en la caja del captcha
print("Captcha completado con exito")
driver.quit()