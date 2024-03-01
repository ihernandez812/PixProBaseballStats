from constants import *

class Team:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.is_user_team = False
        self.record = None
        self.players = []



    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_is_user_team(self):
        return self.is_user_team

    def set_is_user_team(self, value):
        self.is_user_team = value

    def get_record(self):
        return self.record

    def set_record(self, value):
        self.record = value

    def get_players(self):
        return self.players

    def add_player(self, value):
        self.players.append(value)
    
    def to_model(self):
        team_name = self.name
        team_id = self.id 
        is_user_team = self.is_user_team

        team_model = {
            PYMONGO_TEAM_NAME: team_name,
            PYMONGO_TEAM_ID: team_id,
            PYMONGO_TEAM_IS_USER_TEAM: is_user_team
        }

        return team_model

    def create_team_record_model(self, record_id, season_id):
        team_record_model = {
            PYMONGO_TEAM: self.id,
            PYMONGO_SEASON: season_id,
            PYMONGO_RECORD: record_id
        }
        return team_record_model
    
    def create_team_player_season_model(self, player_id, season_id):
        team_player_season_model = {
            PYMONGO_PLAYER: player_id,
            PYMONGO_TEAM: self.id,
            PYMONGO_SEASON: season_id
        }
        return team_player_season_model