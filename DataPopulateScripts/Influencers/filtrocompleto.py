import os
import json


niche_mapping = {
    "0": "moda",
    "1": "culinaria",
    "2": "outros",
    "4": "educacao",
    "5": "negocios",
    "6": "negocios",
    "7": "moda",
    "9": "outros",
    "10": "tecnologia",
    "11": "esporte",
    "12": "esporte",
    "13": "esporte",
    "14": "esporte",
    "15": "esporte",
    "16": "outros",
    "17": "outros",
    "18": "automoveis",
    "19": "culinaria",
    "20": "moda",
    "21": "moda",
    "22": "saude-bem-estar",
    "23": "saude-bem-estar",
    "26": "pets",
    "27": "outros",
    "28": "outros",
    "29": "tecnologia",
    "30": "tecnologia",
    "31": "educacao",
    "34": "tecnologia",
    "35": "culinaria",
    "38": "fotografia",
    "39": "outros",
    "41": "vida",
    "42": "vida",
    "43": "outros",
    "44": "negocios",
    "47": "outros",
    "48": "outros",
    "49": "outros",
    "50": "tecnologia",
    "51": "tecnologia",
    "52": "politica-ativismo"
}

def map_niche_ids(niche_ids, platform):
    if niche_ids is None:
        return ["outros"]
    if platform == "instagram":
        # remove o prefixo dos ids pra nao bugar
        niche_ids = [str(niche_id - 1000) for niche_id in niche_ids]
    return [niche_mapping.get(str(niche_id), "outros") for niche_id in niche_ids]

def filter_info(json_data, platform):
    if not json_data:
        return None
    
    
    username = json_data.get("basic", {}).get("username")
    avatar_url = json_data.get("basic", {}).get("avatar_url")
    geo_country = json_data.get("features", {}).get("audience_geo_country_1_code")
    niche_ids = json_data.get("features", {}).get("blogger_thematics", {}).get("data", [])
    
    
    niches = map_niche_ids(niche_ids, platform)
    
    return {
        "username": username,
        "avatar_url": avatar_url,
        "geo_country": geo_country,
        "niches": niches
    }

def process_files(input_directory, output_directory):
    
    os.makedirs(output_directory, exist_ok=True)
    
    for filename in os.listdir(input_directory):
        if filename.startswith(("instagram-", "youtube-")) and filename.endswith(".json"):
            file_path = os.path.join(input_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    json_data = json.load(file)
                    platform = "instagram" if "instagram-" in filename else "youtube"
                    filtered_info = filter_info(json_data, platform)
                    if filtered_info:
                        #criacao dos json para da influencer
                        username = filtered_info.get("username")
                        if username:
                            output_filename = f"{platform}-{username}.json"
                            output_path = os.path.join(output_directory, output_filename)
                            with open(output_path, 'w', encoding='utf-8') as outfile:
                                json.dump(filtered_info, outfile, ensure_ascii=False, indent=4)
                            print(f"Filtered information saved to {output_path}")
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {filename}: {e}")

if __name__ == "__main__":
    input_directory = "C:\\Users\\zuvan\\Desktop\\filtrando dados\\processados"
    output_directory = "C:\\Users\\zuvan\\Desktop\\filtrando dados\\youtubeeinstanome"
    process_files(input_directory, output_directory)
