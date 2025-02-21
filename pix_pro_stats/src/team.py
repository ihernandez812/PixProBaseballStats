from record import Record
from player import Player
from constants import *

class Team:

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.is_user_team = False
        self.record = None
        self.players:  list[Player] = []



    def get_id(self) -> int:
        return self.id

    def set_id(self, value: int):
        self.id = value

    def get_name(self) -> str:
        return self.name

    def set_name(self, value: str):
        self.name = value

    def get_is_user_team(self) -> bool:
        return self.is_user_team

    def set_is_user_team(self, value: bool):
        self.is_user_team = value

    def get_record(self) -> Record:
        return self.record

    def set_record(self, value: Record):
        self.record = value

    def get_players(self) -> list[Player]:
        return self.players

    def add_player(self, value: Player):
        self.players.append(value)
    
    def to_model(self) -> dict[str,]:
        team_name = self.name
        team_id = self.id 
        is_user_team = self.is_user_team

        team_model = {
            PYMONGO_TEAM_NAME: team_name,
            PYMONGO_TEAM_ID: team_id,
            PYMONGO_TEAM_IS_USER_TEAM: is_user_team
        }

        return team_model

    def create_team_record_model(self, record_id: str, season_id: str) -> dict[str,]:
        team_record_model = {
            PYMONGO_TEAM: self.id,
            PYMONGO_SEASON: season_id,
            PYMONGO_RECORD: record_id
        }
        return team_record_model
    
    def create_team_player_season_model(self, player_id: str, season_id: str) -> dict[str,]:
        team_player_season_model = {
            PYMONGO_PLAYER: player_id,
            PYMONGO_TEAM: self.id,
            PYMONGO_SEASON: season_id
        }
        return team_player_season_model
    
    def to_dict(self) -> dict[str,]:
        team_name = self.name
        team_id = self.id 
        is_user_team = self.is_user_team
        team_model = {
            PYMONGO_TEAM_NAME: team_name,
            PYMONGO_TEAM_ID: team_id,
            PYMONGO_TEAM_IS_USER_TEAM: is_user_team,
            PYMONGO_RECORD: self.record.to_dict(),
            PYMONGO_PLAYER_COLLECTION: [player.to_dict() for player in self.players]
        }

        return team_model