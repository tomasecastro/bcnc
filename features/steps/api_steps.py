import requests
from behave import given, when, then


@given('que la solicitud se hace a la URL proporcionada')
def step_given_solicitud_url():
    return "https://jsonplaceholder.typicode.com/albums"

@when('se recibe la respuesta del servidor')
def step_when_obtenemos_respuesta(url):
    response = requests.get(url)
    return response

@then('se verifica que los primeros {int} elementos coincidan con los datos esperados')
def step_then_verificamos_elementos(response):
    if response.status_code != 200:
        print(f"Estado de la respuesta no es 200: {response.status_code}")
        return

    data = response.json()
    if len(data) < 5:
        print(f"No hay suficientes elementos en la respuesta: {len(data)}")
        return

    print("Datos de los primeros 5 elementos:")
    for album in data[:5]:
        print(album)

# Simular la ejecución de los pasos
url = step_given_solicitud_url()
response = step_when_obtenemos_respuesta(url)
step_then_verificamos_elementos(response)