from team import Team
from playoffs import Playoffs


class Season:
    
    def __init__(self, year, teams, regular_season, playoffs):
        self.year = year
        self.playoffs = playoffs
        self.regular_season = regular_season
        self.teams = teams

    def get_year(self):
        return self.year 
    
    def add_regular_season_game(self, regular_season_game):
        self.regular_season.append(game)
    
    def get_regular_season(self):
        return regular_season

    def set_playoffs(self, playoffs : Playoffs):
        self.playoffs = playoffs

    def get_playoffs(self):
        return self.playoffs
    
    def add_team(self, team: Team):
        self.teams.append(team)

    def get_teams(self):
        return self.teams