from team import Team
from playoffs import Playoffs


class Season:
    
    def __init__(self, year):
        self.year = year
        self.playoffs = None
        self.teams = []

    def get_year(self):
        return self.year 
    
    def set_playoffs(self, playoffs : Playoffs):
        self.playoffs = playoffs

    def get_playoffs(self):
        return self.playoffs
    
    def add_team(self, team: Team):
        self.teams.append(team)

    def get_teams(self):
        return self.teams