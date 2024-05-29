import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then


@when('hacemos click en el boton "Who We Are"')
def step_click_who_we_are(context):
    time.sleep(10)
    # Esperar hasta que el elemento de carga desaparezca
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "preloader"))
    )

    # Hacer clic en el botón "Who We Are"
    who_we_are_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='menu sidebar__menu']//a[contains(.,'Who we are')]"))
    )
    who_we_are_button.click()
    time.sleep(10)


@when('buscamos las clases text dentro de los DIVS en Who We Are')
def step_find_texts_who_we_are(context):
   # Esperar hasta que se encuentre el div con la clase 'text' en Who we are
    text_div = WebDriverWait(context.driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//section[@class='page__intro page__intro--who-we-are']"))
    )
    context.text = text_div.text
    print("Texto capturado de la seccion", context.text) 

@then('Imprimimos los textos encontrados en Who We Are')
def step_print_texts_who_we_are(context):
    print('Textos de la sección "WHO WE ARE":')
    #for text in context.text:
    #print(context.text)
