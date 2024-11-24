import requests
import pytest

# URLs das APIs
API_COUNTRIES = "https://restcountries.com/v3.1/all"
API_DOG_BREEDS = "https://api.thedogapi.com/v1/breeds"
API_POKEMON = "https://pokeapi.co/api/v2/pokemon/ditto"
API_CAT_FACTS = "https://catfact.ninja/fact"

# URLs da API para dados de COVID-19 no Brasil e Argentina
API_COVID_BRAZIL = "https://disease.sh/v3/covid-19/countries/Brazil"
API_COVID_ARGENTINA = "https://disease.sh/v3/covid-19/countries/Argentina"

# Teste para API de informações sobre países
def test_countries_api_success():
    # Realiza a requisição para a API de países
    response = requests.get(API_COUNTRIES)
    
    # Verifica se o status da resposta é 200 (sucesso)
    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"
    
    # Extrai os dados em formato JSON
    data = response.json()
    
    # Itera sobre cada país retornado para verificar chaves essenciais
    for country in data:
        # Verifica se a chave 'name.common' existe para identificar o nome do país
        assert "name" in country and "common" in country["name"], "Chave 'name.common' não encontrada"
        
        # Verifica se a chave 'population' existe para obter a população do país
        assert "population" in country, "Chave 'population' não encontrada"
        
        # Verifica se a chave 'flags.png' existe para obter a bandeira do país
        assert "flags" in country and "png" in country["flags"], "Chave 'flags.png' não encontrada"


# Teste para API de raças de cães
def test_dog_breeds_api_success():
    # Realiza a requisição para a API de raças de cães
    response = requests.get(API_DOG_BREEDS)
    
    # Verifica se o status da resposta é 200 (sucesso)
    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"

    # Extrai os dados em formato JSON
    data = response.json()
    
    # Itera sobre cada raça de cão para verificar chaves essenciais
    for breed in data:
        # Verifica se a chave 'name' existe para identificar o nome da raça
        assert "name" in breed, "Chave 'name' não encontrada"
        
        # Verifica se a chave 'life_span' existe para obter a expectativa de vida da raça
        assert "life_span" in breed, "Chave 'life_span' não encontrada"
        
        # Verifica se a chave 'temperament' existe e, caso exista, se é uma string
        if "temperament" in breed:
            assert isinstance(breed["temperament"], str), "Temperamento deve ser uma string"


# Teste para API de informações sobre um Pokémon específico
def test_pokemon_api_success():
    # Realiza a requisição para a API de Pokémon (usei o Pokémon "Ditto" como exemplo)
    response = requests.get(API_POKEMON)
    
    # Verifica se o status da resposta é 200 (sucesso)
    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"
    
    # Extrai os dados em formato JSON
    data = response.json()
    
    # Verifica se a chave 'name' existe para identificar o nome do Pokémon
    assert "name" in data, "Chave 'name' não encontrada no Pokémon"
    
    # Verifica se a chave 'abilities' existe para obter a lista de habilidades do Pokémon
    assert "abilities" in data, "Chave 'abilities' não encontrada no Pokémon"
    
    # Verifica se a lista de habilidades não está vazia
    assert isinstance(data["abilities"], list) and len(data["abilities"]) > 0, "Nenhuma habilidade encontrada"
    
    
# Teste para API de fatos sobre gatos
def test_cat_facts_api_success():
    # Envia a requisição para a API
    response = requests.get(API_CAT_FACTS)
    
    # Verifica se o status da resposta é 200 (sucesso)
    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"
    
    # Verifica se a resposta contém o fato sobre gatos
    data = response.json()
    assert "fact" in data, "Chave 'fact' não encontrada na resposta"
    assert isinstance(data["fact"], str) and len(data["fact"]) > 0, "Fato sobre gatos está vazio ou não é uma string"


# Teste para dados de COVID-19 no Brasil
def test_covid_brazil_api_success():
    # Realiza a requisição para a API de dados de COVID-19 no Brasil
    response = requests.get(API_COVID_BRAZIL)
    
    # Verifica se o status da resposta é 200 (sucesso)
    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"
    
    # Extrai os dados em formato JSON
    data = response.json()
    
    # Verifica se a chave 'cases' existe para obter o número de casos de COVID-19
    assert "cases" in data, "Chave 'cases' não encontrada nos dados do Brasil"
    
    # Verifica se a chave 'deaths' existe para obter o número de mortes por COVID-19
    assert "deaths" in data, "Chave 'deaths' não encontrada nos dados do Brasil"
    
    # Verifica se a chave 'recovered' existe para obter o número de recuperados da COVID-19
    assert "recovered" in data, "Chave 'recovered' não encontrada nos dados do Brasil"
    
    # Imprime os dados de COVID-19 no Brasil (opcional para fins de depuração)
    print("Dados de COVID-19 no Brasil:", data)


# Teste para dados de COVID-19 na Argentina
def test_covid_argentina_api_success():
    # Realiza a requisição para a API de dados de COVID-19 na Argentina
    response = requests.get(API_COVID_ARGENTINA)
    
    # Verifica se o status da resposta é 200 (sucesso)
    assert response.status_code == 200, f"Esperado status 200, mas recebeu {response.status_code}"
    
    # Extrai os dados em formato JSON
    data = response.json()
    
    # Verifica se a chave 'cases' existe para obter o número de casos de COVID-19
    assert "cases" in data, "Chave 'cases' não encontrada nos dados da Argentina"
    
    # Verifica se a chave 'deaths' existe para obter o número de mortes por COVID-19
    assert "deaths" in data, "Chave 'deaths' não encontrada nos dados da Argentina"
    
    # Verifica se a chave 'recovered' existe para obter o número de recuperados da COVID-19
    assert "recovered" in data, "Chave 'recovered' não encontrada nos dados da Argentina"
    
    # Imprime os dados de COVID-19 na Argentina (opcional para fins de depuração)
    print("Dados de COVID-19 na Argentina:", data)
