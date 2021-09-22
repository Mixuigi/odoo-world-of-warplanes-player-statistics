from odoo import models, fields
from .get_info import *


class Player(models.Model):
    _name = 'wow.player'
    _description = 'Player Statistics'

    nickname = fields.Char(string='ник игрока')  # nickname
    region = fields.Char(string='страна игрока')  # client_language
    account_id = fields.Integer(string='ID')  # account_id
    max_aircraft_damage = fields.Integer(
        string='Максимальный урон по самолётам')  # statistics.all.air_targets.max_damage_dealt
    max_ground_objects_damage = fields.Integer(
        string='Максимальный урон по наземным целям')  # statistics.all.ground_objects.max_damage_dealt
    score = fields.Integer(string='Личный рейтинг')  # statistics.all.battle_score !!!!!!!!!!!!
    wins = fields.Integer(string='Количество побед')  # statistics.all.wins
    losses = fields.Integer(string='Количество поражений')  # statistics.all.losses

    def create_data(self):
        self.search([]).unlink()
        players_info = get_players()  # [info(0), info(1), info(2)........]
        for player_info in players_info:
            vals = [{
                'nickname': player_info[0],
                'region': player_info[1],
                'account_id': player_info[2],
                'max_aircraft_damage': player_info[3],
                'max_ground_objects_damage': player_info[4],
                'score': player_info[5],
                'wins': player_info[6],
                'losses': player_info[7],
            }]
            self.create(vals)
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
