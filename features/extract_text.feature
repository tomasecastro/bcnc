Feature: Pruebas de BCNC

  @test
  Scenario: Extraer los valores de las clases text dentro de los DIVS en el apartado "Home"
    Given abrimos la pagina web de bcngroup
    When hacemos click en el boton "Home"
    And buscamos las clases text dentro de los DIVS en Home
    Then Imprimimos los textos encontrados en Home

  @test
  Scenario: Extraer los valores de las clases text dentro de los DIVS en el apartado "Who We Are"
    Given abrimos la pagina web de bcngroup
    When hacemos click en el boton "Who We Are"
    And buscamos las clases text dentro de los DIVS en Who We Are
    Then Imprimimos los textos encontrados en Who We Are

  @test
  Scenario: Validar la respuesta de la API
    Given que la solicitud se hace a la URL proporcionada
    When se recibe la respuesta del servidor
    Then se verifica que los primeros 5 elementos coincidan con los datos esperados

  @test
  Scenario: Obtener datos usando Client Credentials Grant
    Given que tengo un client ID y client secret válidos de Auth0
    When solicito un token de acceso usando el grant type "client credentials"
    Then obtengo los datos de la API utilizando el token de acceso