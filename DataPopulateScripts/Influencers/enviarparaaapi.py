import os
import json
import requests
import random
from datetime import datetime, timedelta

# Configurações do Spring Boot
server_port = 8001
servlet_context_path = "/influenceconnect"
api_base_url = f"http://localhost:8001/influenceconnect/influencers"

# Dicionário de mapeamento de estado
state_mapping = {
    "br": list(range(1, 28)),  # Estados do Brasil de 1 a 27
    "outro": [28]  #gringos
}

# Lista de domínios de e-mail para escolha aleatória
email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

# Dicionário de mapeamento de nichos
niche_mapping = {
    "esporte": 1,
    "musica": 2,
    "moda": 3,
    "saude-bem-estar": 4,
    "negocios": 5,
    "design-interior": 6,
    "tecnologia": 7,
    "fotografia": 8,
    "culinaria": 9,
    "educacao": 10,
    "games": 11,
    "sustentabilidade": 12,
    "automoveis": 13,
    "viagens": 14,
    "pets": 15,
    "vida": 16,
    "politica-ativismo": 17,
    "outros": 18
}

# Função para gerar data de nascimento aleatória a partir de 1930
def generate_birthdate():
    start_date = datetime(1930, 1, 1)
    end_date = datetime.now() - timedelta(days=365 * 18)  # Menos de 18 anos
    birth_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return birth_date.strftime("%Y-%m-%d")

# Função para gerar e-mail aleatório
def generate_email(username):
    domain = random.choice(email_domains)
    return f"{username}@{domain}"

# Função para enviar dados para a API
def send_to_api(username, avatar_url, geo_country, niches, platform):
    # chamando a funcao para gerar dados aleatorios
    birthdate = generate_birthdate()
    email = generate_email(username)

    # escolha do estado com base na geolocalizacao , escolha do estado é aleatoria
    #se for gringo coloca ele fora do brasil. 
    state_id = random.choice(state_mapping.get(geo_country.lower(), [28]))

    # Mapear os nomes dos nichos para IDs usando o dicionário de mapeamento 
    niche_ids = [niche_mapping.get(niche.lower(), 18) for niche in niches]

    # arrumando os dados na formatacao esperada para a api 
    if platform == "instagram":
        social_media_id = 2
        link = f"https://www.instagram.com/{username}"
    elif platform == "youtube":
        social_media_id = 3
        link = f"https://www.youtube.com/{username}"
    else:
        return  

    data = {
        "email": email,
        "name": username,
        "password": "12345678Aa!",  
        "cpf": "111.111.111-11",  
        "profilePhoto": avatar_url,
        "stateId": state_id,
        "birthdate": birthdate,
        "nicheIds": niche_ids,
        "influencerSocialMedia": [{
            "socialMediaId": social_media_id,
            "link": link
        }]
    }

    # Cabeçalhos da requisição
    headers = {
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:5173'  # gambiarra para simular que sou o site de origem 
    }

    # requisicao post pra api louca
    try:
        response = requests.post(api_base_url, json=data, headers=headers)
        if response.status_code == 201:
            print(f"Influencer {username} enviado com sucesso para a API")
        else:
            print(f"Falha ao enviar influencer {username} para a API: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

# processamento dos arquivos
def process_files(input_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith(".json"):
            platform = None
            if filename.startswith("instagram-"):
                platform = "instagram"
                username = filename.replace("instagram-", "").replace(".json", "")
            elif filename.startswith("youtube-"):
                platform = "youtube"
                username = filename.replace("youtube-", "").replace(".json", "")

            if platform:
                file_path = os.path.join(input_directory, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    try:
                        json_data = json.load(file)
                        avatar_url = json_data.get("avatar_url") or "https://example.com/default_avatar.jpg"
                        geo_country = json_data.get("geo_country") or "br"
                        niche_names = json_data.get("niches", [])

                        # Chamar função para enviar para a API
                        send_to_api(username, avatar_url, geo_country, niche_names, platform)

                    except json.JSONDecodeError as e:
                        print(f"Erro ao decodificar JSON do arquivo {filename}: {e}")

if __name__ == "__main__":
    input_directory = "C:\\Users\\zuvan\\Desktop\\filtrando dados\\jsonparapopularapi"
    process_files(input_directory)
