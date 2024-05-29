from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Configurar las opciones del navegador (en este caso, Chrome)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Maximizar la ventana

    # Crear una instancia del controlador
    context.driver = webdriver.Chrome(options=chrome_options)

    # Abrir la página web
    context.driver.get("https://bcncgroup.com/")

def after_all(context):
    # Cerrar el navegador al finalizar las pruebas
    context.driver.quit()
