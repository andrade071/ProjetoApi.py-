# PROJETO API TESTE 4P

# Uma breve descrição sobre o propósito dos testes 

- test_countries_api_success: Verifica se a API de países retorna corretamente
 a lista de países, incluindo chaves essenciais como nome, população e bandeira.

- test_dog_breeds_api_success: Verifica se a API de raças de cães retorna informações
 essenciais, como o nome, expectativa de vida e, se presente, o temperamento das raças.

- test_pokemon_api_success: Verifica se a API de Pokémon retorna dados corretos sobre o 
Pokémon que usei foi o "Ditto", incluindo o nome e habilidades.

- test_cat_facts_api_success: Verifica se a API de fatos sobre gatos retorna um fato
 válido, com a chave "fact" contendo uma string não vazia.

- test_covid_brazil_api_success: Verifica se a API de dados de COVID-19 do Brasil 
retorna as informações sobre casos, mortes e recuperações.

- test_covid_argentina_api_success: Verifica se a API de dados de COVID-19 da 
Argentina retorna as informações sobre casos, mortes e recuperações.

# URLs das APIs
1. API_COUNTRIES = "https://restcountries.com/v3.1/all"
2. API_DOG_BREEDS = "https://api.thedogapi.com/v1/breeds"
3. API_POKEMON = "https://pokeapi.co/api/v2/pokemon/ditto"
4. API_CAT_FACTS = "https://catfact.ninja/fact"

# URLs da API para dados de COVID-19 no Brasil e Argentina
5.1 API_COVID_BRAZIL = "https://disease.sh/v3/covid-19/countries/Brazil"
5.2 API_COVID_ARGENTINA = "https://disease.sh/v3/covid-19/countries/Argentina"

 # Teste de Integração com APIs Públicas

Este projeto contém testes de integração para APIs públicas que oferecem 
dados diversos, como informações sobre países, raças de cães, Pokémon
e dados de COVID-19.

 # Instalei as dependências do projeto usando o "requirements.txt"

- pip install -r requirements.txt

# Para executar os Testes que coloquei; 
 Utilizei o comando:
- pytest 

# Arquivo "requirements.txt"

Para especificar as dependências do projeto.

- requests
- pytest

