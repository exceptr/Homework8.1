import requests as requests


def get_max_intelligence_hero():
    hero_intelligence = {}
    request_url = f"https://superheroapi.com/api/2619421814940190/332/powerstats"
    response = requests.get(request_url)
    hero_intelligence['Hulk'] = int(response.json()['intelligence'])
    request_url = f"https://superheroapi.com/api/2619421814940190/149/powerstats"
    response = requests.get(request_url)
    hero_intelligence['CaptainAmerica'] = int(response.json()['intelligence'])
    request_url = f"https://superheroapi.com/api/2619421814940190/655/powerstats"
    response = requests.get(request_url)
    hero_intelligence['Thanos'] = int(response.json()['intelligence'])
    max_intelligence = max(hero_intelligence, key=hero_intelligence.get)
    return max_intelligence


print(get_max_intelligence_hero())