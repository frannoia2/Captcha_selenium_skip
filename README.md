# Captcha_selenium_skip

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

**Herramientas para evitar posibles captchas utilizando selenium**
## Tipos de captchas:

- CloudFlare captcha: Con este tipo usamos Selenium para localizar el cuadro flotante y pulsarlo, además de establecer una serie de opciones para simular que lo realiza un humano.
* Text type captcha: En este caso scrapeamos la imagen, analizamos el texto que contiene, lo escribimos y repetimos este proceso hasta que resolvemos el texto de la imagen.