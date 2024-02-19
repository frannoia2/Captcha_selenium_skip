from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
import easyocr

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)   
driver = webdriver.Chrome(options)
driver.get("https://www.galileo.edu/wp-content/plugins/si-captcha-for-wordpress/captcha/test/captcha_test.php")
captchaBool = False
while captchaBool is not True:
    try:
        #scrapeamos la imagen del captcha 
        captchaImage = driver.find_element(By.XPATH, '//*[@id="si_image"]')
        captchaImageSave = driver.execute_async_script("""
                    var element = arguments[0], callback = arguments[1];
                    element.addEventListener('load', function fn(){
                        element.removeEventListener('load', fn, false);
                        var canva = document.createElement('canvas');
                        canva.width = this.width; canva.height = this.height;
                        canva.getContext('2d').drawImage(this, 0, 0);
                        var imagen = canva.toDataURL('image/jpeg').substring(22);
                        callback(imagen);
                    }, false);
                    element.dispatchEvent(new Event('load'));
                    """, captchaImage)

        with open(r"captcha.jpg", 'wb') as f:
            f.write(base64.b64decode(captchaImageSave))

        #utilizamos la libreria easyocr para leer el texto de la imagen de antes
        reader = easyocr.Reader(['en'])
        result = reader.readtext('captcha.jpg')
        for x in result:
            captchaResult = x[1]
        print(captchaResult)
        #escribimos el texto leido y pulsamos el ok 
        driver.find_element(By.XPATH, '//*[@id="code"]').send_keys(captchaResult)
        driver.find_element(By.XPATH, '//*[@id="captcha_test"]/p[2]/input[2]').click()
        print("Volviendo a intentar el captcha")
    except:
        print("Captcha completado con exito")
        captchaBool = True
        driver.quit()
            