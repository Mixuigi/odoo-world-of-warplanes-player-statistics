import requests

URL_GET_PLAYERS = 'https://api.worldofwarplanes.ru/wowp/ratings/top/?application_id=20efd0da52184a9fbcdfb44664432f5a&rank_field=damage_dealt_ground&type=28&limit=100'

URL_GET_INFO_ABOUT_PLAYERS = 'https://api.worldofwarplanes.ru/wowp/account/info2/?application_id=20efd0da52184a9fbcdfb44664432f5a&account_id='


def get_player_info(info_players, id) -> tuple:
    all_info = info_players['data'][id]
    info = all_info['nickname'], \
           all_info['client_language'], \
           all_info['account_id'], \
           all_info['statistics']['all']['air_targets']['max_damage_dealt'], \
           all_info['statistics']['all']['ground_objects']['max_damage_dealt'], \
           all_info['global_rating'], \
           all_info['statistics']['all']['losses'], \
           all_info['statistics']['all']['wins']
    return info


def get_players() -> list:
    players = []
    get_players_json = requests.get(URL_GET_PLAYERS).json()
    for words in get_players_json['data']:
        id = words['account_id']
        info_players = requests.get(f'{URL_GET_INFO_ABOUT_PLAYERS}+{id}').json()
        players.append(get_player_info(info_players, str(id)))
    return players
