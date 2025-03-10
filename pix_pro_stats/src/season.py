from team import Team
from playoffs import Playoffs
from game import Game
from awards import Awards
from player import Player
from constants import *
import json


class Season:
    TEAM_PLAYERS='teamSeasonPlayers'
    TEAM_RECORD='teamRecords'
    PLAYOFFS='playoffs'
    AWARDS='awards'
    HOF_CLASS='hofClass'
    REGULAR_SEASON='regularSeason'
    YEAR='year'

    def __init__(self, year: str, teams: list[Team], regular_season: list[Game], playoffs: Playoffs, awards: Awards) -> None:
        self.year = year
        self.playoffs = playoffs
        self.regular_season = regular_season
        self.teams = teams
        self.awards = awards
        self.hof_class: list[str] = []

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
    
    def set_hof_class(self, player_ids : list[str]) -> None:
        self.hof_class = player_ids
    
    def get_hof_class(self) -> list[str]:
        return self.hof_class
    
    @DeprecationWarning
    def to_model(self, playoffs_id: str, awards_id: str, regular_season_games: list[str]) -> dict[str,]:
        season_model = {
            League.YEAR: self.year,
            self.PLAYOFFS: playoffs_id,
            self.AWARDS: awards_id,
            self.REGULAR_SEASON: regular_season_games,
        }
        return season_model
    
    def to_dict(self) -> dict[str,]:
        return {
            self.YEAR: self.year,
            self.PLAYOFFS: self.playoffs.to_dict(),
            self.REGULAR_SEASON: [game.to_dict() for game in self.regular_season],
            #PYMONGO_TEAMS: [team.to_dict() for team in self.teams],
            self.AWARDS: self.awards.to_dict(),
            self.HOF_CLASS: self.hof_class
        }
        

    def to_json(self):
        return json.dumps(
            self.__dict__, 
            sort_keys=True,
            indent=4)

    @DeprecationWarning
    def create_season_awards_model(self, season_id: str, awards_id: str) -> dict[str, str]:
        season_awards = {
            League.SEASON: season_id,
            self.AWARDS: awards_id
        }
        return season_awards