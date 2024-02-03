from team import Team

class Game:
    def __init__(self, team_one, team_one_score, team_two, team_two_score):
        self.team_one = team_one
        self.team_one_score = team_one_score
        self.team_two = team_two
        self.team_two_score = team_two_score
    
    def get_team_one(self):
        return self.team_one

    def get_team_two(self):
        return self.team_two

    def get_winner(self):
        if self.team_one_score > self.team_two_score:
            return self.team_one
        else:
            return self.team_two