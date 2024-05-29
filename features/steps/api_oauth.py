import requests
from requests.auth import HTTPBasicAuth
import os
from behave import given, when, then

# Configuración de Auth0
client_id = os.getenv('CLIENT_ID', 'TU_CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET', 'TU_CLIENT_SECRET')
token_url = 'https://dev-ywu61lihk0hn1li8.us.auth0.com/api/v2/'
api_url = 'https://jsonplaceholder.typicode.com/albums'

@given('que tengo un client ID y client secret válidos de Auth0')
@when ('solicito un token de acceso usando el grant type "client credentials"')
@then ('obtengo los datos de la API utilizando el token de acceso')
def get_access_token_client_credentials():
    auth = HTTPBasicAuth(client_id, client_secret)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'audience': 'TU_AUDIENCIA'  # Especifica la audiencia según tu configuración en Auth0
    }
    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    token = response.json()['access_token']
    return token

def make_authenticated_request(token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()

try:
    token = get_access_token_client_credentials()
    data = make_authenticated_request(token)
    print("Datos obtenidos con Client Credentials Grant:")
    print(data[:5])  # Mostrar los primeros 5 elementos
except Exception as e:
    print(f"Error: {e}")
