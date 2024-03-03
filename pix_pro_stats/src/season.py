from team import Team
from playoffs import Playoffs
from game import Game
from awards import Awards
from constants import *


class Season:
    
    def __init__(self, year: str, teams: list[Team], regular_season: list[Game], playoffs: Playoffs, awards: Awards) -> None:
        self.year = year
        self.playoffs = playoffs
        self.regular_season = regular_season
        self.teams = teams
        self.awards = awards

    def get_year(self) -> str:
        return self.year 
    
    def add_regular_season_game(self, regular_season_game: Game) -> Game:
        self.regular_season.append(regular_season_game)
    
    def get_regular_season(self) -> list[Game]:
        return self.regular_season

    def set_playoffs(self, playoffs : Playoffs):
        self.playoffs = playoffs

    def get_playoffs(self) -> Playoffs:
        return self.playoffs
    
    def add_team(self, team: Team) -> None:
        self.teams.append(team)

    def get_teams(self) -> list[Team]:
        return self.teams
    
    def set_awards(self, awards: Awards):
        self.awards = awards

    def get_awards(self) -> Awards:
        return self.awards
    
    def to_model(self, playoffs_id: str, awards_id: str, regular_season_games: list[str]) -> dict[str,]:
        season_model = {
            PYMONGO_YEAR: self.year,
            PYMONGO_PLAYOFFS: playoffs_id,
            PYMONGO_AWARDS: awards_id,
            PYMONGO_REGULAR_SEASON: regular_season_games,
        }
        return season_model
    
    def create_season_awards_model(self, season_id: str, awards_id: str) -> dict[str, str]:
        season_awards = {
            PYMONGO_SEASON: season_id,
            PYMONGO_AWARDS: awards_id
        }
        return season_awards