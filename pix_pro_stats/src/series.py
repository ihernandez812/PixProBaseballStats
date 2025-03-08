from team import Team
from game import Game
from constants import *
import uuid
from uuid import UUID

class Series:

    def __init__(self, team_one: Team, team_two: Team, winner_id: int, games: list[Game], series_length: int, name: str) -> None:
        self.id = uuid.uuid4()
        self.team_one = team_one
        self.team_two = team_two
        self.winner_id = winner_id
        self.games = games
        self.series_length = series_length
        self.name = name

    def get_team_one(self) -> Team:
        return self.team_one

    def get_team_two(self) -> Team:
        return self.team_two

    def add_game(self, game: Game) -> None:
        self.games.append(game)

    def get_games(self) -> list[Game]:
        return self.games
    
    def get_series_length(self) -> int:
        return self.series_length
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name

    def get_series_winner(self) -> Team:
        series_winner = None
        team_one_id = self.team_one.get_id()
        if team_one_id == self.winner_id:
            series_winner = self.team_one
        else:
            series_winner = self.team_two

        return series_winner
    
    def to_model(self, games: list[str]) -> dict[str, ]:
        team_one = self.team_one.get_id()
        team_two = self.team_two.get_id()
        winner = self.get_series_winner().get_id()
        
        series_length = self.get_series_length()

        series_model = {
            PYMONGO_TEAM_ONE: team_one,
            PYMONGO_TEAM_TWO: team_two,
            PYMONGO_WINNER: winner,
            PYMONGO_GAMES: games,
            PYMONGO_SERIES_LENGTH: series_length
        }
        return series_model
    

    def to_dict(self) -> dict[str, ]:
        team_one = self.team_one.get_id()
        team_two = self.team_two.get_id()
        winner = self.get_series_winner().get_id()
        
        series_length = self.get_series_length()

        series_model = {
            PYMONGO_SERIES_ID: str(self.id),
            PYMONGO_TEAM_ONE: team_one,
            PYMONGO_TEAM_TWO: team_two,
            PYMONGO_WINNER: winner,
            PYMONGO_GAMES: [game.to_dict() for game in self.games],
            PYMONGO_SERIES_LENGTH: series_length,
            PYMONGO_SERIES_NAME: self.name
        }
        return series_model