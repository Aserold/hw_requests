import requests
import json

id_dict = {
    "Thanos": 655,
    "Captain America": 149,
    "Hulk": 332
}


supes_dict = {} #Словарь с именнами и интеллектом супергероев
keys_list = list(id_dict.keys()) # Это список имен по словарю
values_list = list(id_dict.values()) # Это список id по словарю

for i in range(len(id_dict)):
    id = values_list[i]
    url = f'https://akabab.github.io/superhero-api/api//powerstats/{id}.json'
    resp = requests.get(url)
    json_response = resp.json()
    name = keys_list[i]
    intelligence = json_response['intelligence']
    if name in supes_dict:
        print('Ошибка! Возможно вы добавили одинаковых героев')
    else:
        supes_dict[name] = intelligence


intelligince_list = [name for name, intelligence in sorted(supes_dict.items(), key=lambda x: x[1], reverse=True)]
print(f'Самый умный из героев: {intelligince_list[0]}')

