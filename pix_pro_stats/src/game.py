from team import Team
from constants import *

class Game:
    def __init__(self, team_one: Team, team_one_score: int, team_two: Team, team_two_score: int):
        self.team_one = team_one
        self.team_one_score = team_one_score
        self.team_two = team_two
        self.team_two_score = team_two_score
    
    def get_team_one(self):
        return self.team_one

    def get_team_two(self):
        return self.team_two

    def get_team_one_score(self):
        return self.team_one_score

    def get_team_two_score(self):
        return self.team_two_score

    def get_winner(self):
        if self.team_one_score > self.team_two_score:
            return self.team_one
        else:
            return self.team_two
    def to_model(self):
        team_one = self.team_one.get_id()
        team_two = self.team_two.get_id()
        team_one_score = self.team_one_score
        team_two_score = self.team_two_score
        winner = self.get_winner().get_id()

        game_model = {
            PYMONGO_TEAM_ONE: team_one,
            PYMONGO_TEAM_TWO: team_two,
            PYMONGO_TEAM_ONE_SCORE: team_one_score,
            PYMONGO_TEAM_TWO_SCORE: team_two_score,
            PYMONGO_WINNER: winner,
        }

        return game_model