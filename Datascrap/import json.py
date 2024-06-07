import json
import os


def extract_influencers_from_har(har_file):
    with open(har_file, 'r', encoding='utf-8') as file:
        har_data = json.load(file)
    
    influencers = []
    for entry in har_data['log']['entries']:
        try:
            content = json.loads(entry['response']['content']['text'])
            reports = content.get('data', {}).get('reports', [])
            for report in reports:
                influencer_data = {
                    'social_id': report['basic'].get('social_id', ''),
                    'username': report['basic'].get('username', ''),
                    'fullname': report['basic'].get('fullname', ''),
                    'avatar_url': report['basic'].get('avatar_url', ''),
                    'is_verified': report['basic'].get('is_verified', False),
                    'audience_geo_country_1_code': report['features'].get('audience_geo_country_1_code', ''),
                    'audience_geo_country_1_prc': report['features'].get('audience_geo_country_1_prc', 0),
                    'blogger_thematics': report['features'].get('blogger_thematics', {}).get('data', []),
                    'subscribers_count': report['metrics'].get('subscribers_count', {}).get('value', 0),
                    'engagement_avg': report['metrics'].get('engagement_avg', {}).get('value', 0),
                    'authentic_engagement': report['metrics'].get('authentic_engagement', {}).get('value', 0)
                }
                influencers.append(influencer_data)
        except (KeyError, json.JSONDecodeError):
            continue
    
    return influencers


def save_influencers_to_json(influencers, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for influencer in influencers:
        username = influencer['username']
        if not username:
            continue
        filename = f"{username}.json"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(influencer, file, ensure_ascii=False, indent=4)


def process_har_files(input_dir, output_dir):
    for i in range(2, 21):
        har_file = os.path.join(input_dir, f'hypeauditor.com{i}.har')
        if os.path.exists(har_file):
            influencers = extract_influencers_from_har(har_file)
            save_influencers_to_json(influencers, output_dir)
        else:
            print(f"File {har_file} does not exist.")

if __name__ == '__main__':
    input_directory = '/home/virlustitiae/Área de trabalho/data scrap brazil influencers/instrgramtop1000brazil'  
    output_directory = '/home/virlustitiae/Área de trabalho/data scrap brazil influencers/instrgramtop1000brazil/filtrados'  
    process_har_files(input_directory, output_directory)
