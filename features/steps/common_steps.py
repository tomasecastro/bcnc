import time
from behave import given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('abrimos la pagina web de bcngroup')
def step_open_webpage(context):
    context.driver.get("https://bcncgroup.com/")
    accept_cookies(context.driver)


def accept_cookies(driver):
    try:
        # Esperar hasta 60 segundos para que aparezca el banner de cookies
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cc-window"))
        )
        cookie_banner = driver.find_element(By.CLASS_NAME, "cc-window")
        accept_button = cookie_banner.find_element(By.CLASS_NAME, "cc-allow"
        )
        accept_button.click()
        time.sleep(10)

    except:
        pass  # Si el banner de cookies no aparece, no hacer nada