from team import Team
from playoffs import Playoffs
from constants import *


class Season:
    
    def __init__(self, year, teams, regular_season, playoffs, awards):
        self.year = year
        self.playoffs = playoffs
        self.regular_season = regular_season
        self.teams = teams
        self.awards = awards

    def get_year(self):
        return self.year 
    
    def add_regular_season_game(self, regular_season_game):
        self.regular_season.append(regular_season_game)
    
    def get_regular_season(self):
        return self.regular_season

    def set_playoffs(self, playoffs : Playoffs):
        self.playoffs = playoffs

    def get_playoffs(self):
        return self.playoffs
    
    def add_team(self, team: Team):
        self.teams.append(team)

    def get_teams(self):
        return self.teams
    
    def set_awards(self, awards):
        self.awards = awards

    def get_awards(self):
        return self.awards
    
    def to_model(self, playoffs_id, regular_season_games):
        season_model = {
            PYMONGO_YEAR: self.year,
            PYMONGO_PLAYOFFS: playoffs_id,
            PYMONGO_REGULAR_SEASON: regular_season_games,
        }
        return season_model
    
    def create_season_awards_model(self, season_id, awards_id):
        season_awards = {
            PYMONGO_SEASON: season_id,
            PYMONGO_AWARDS: awards_id
        }
        return season_awards