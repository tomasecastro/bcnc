import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

@when('hacemos click en el boton "Home"')
def step_click_home(context):
    # Esperar hasta que el botón Home sea visible, clickeable y la página esté completamente cargada
    home_button = WebDriverWait(context.driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu sidebar__menu']//a[contains(.,'Home')]"))
    )
    home_button.click()
    time.sleep(10)

@when('buscamos las clases text dentro de los DIVS en Home')
def step_find_texts_home(context):
    # Esperar hasta que se encuentre el div con la clase 'text' en Home
    text_div = WebDriverWait(context.driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='page__wrapper page__wrapper--home-intro']//div[@class='text']"))
    )
    context.text = text_div.text
    print("Texto capturado:", context.text) 

@then('Imprimimos los textos encontrados en Home')
def step_print_texts_home(context):
    print("Textos de la sección HOME:")
    print(context.text)
