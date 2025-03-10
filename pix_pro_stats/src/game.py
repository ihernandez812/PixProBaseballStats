from team import Team
from constants import *
import uuid
from uuid import UUID

class Game:
    ID='id'
    TEAM_ONE_ID='t0id'
    TEAM_ONE_SCORE='t0score'
    TEAM_TWO_ID='t1id'
    TEAM_TWO_SCORE='t1score'
    TEAM_ONE='team_one'
    TEAM_TWO='team_two'
    #TEAM_ONE_SCORE='team_one_score'
    #TEAM_TWO_SCORE='team_two_score'
    WINNER='winner'
    #For some reason the playoff have different keys
    PLAYOFFS_TEAM_ONE_ID='team0id'
    PLAYOFFS_TEAM_TWO_ID='team1id'
    PLAYOFFS_TEAM_ONE_SCORE='score0'
    PLAYOFFS_TEAM_TWO_SCORE='score1'

    def __init__(self, team_one: Team, team_one_score: int, team_two: Team, team_two_score: int) -> None:
        self.id = uuid.uuid4()
        self.team_one = team_one
        self.team_one_score = team_one_score
        self.team_two = team_two
        self.team_two_score = team_two_score
    
    def get_game_id(self) -> UUID:
        return self.id

    def get_team_one(self) -> Team:
        return self.team_one

    def get_team_two(self) -> Team:
        return self.team_two

    def get_team_one_score(self) -> int:
        return self.team_one_score

    def get_team_two_score(self) -> int:
        return self.team_two_score

    def get_winner(self) -> Team:
        if self.team_one_score > self.team_two_score:
            return self.team_one
        else:
            return self.team_two
        
    @DeprecationWarning
    def to_model(self) -> dict[str,]:
        team_one = self.team_one.get_id()
        team_two = self.team_two.get_id()
        team_one_score = self.team_one_score
        team_two_score = self.team_two_score
        winner = self.get_winner().get_id()

        game_model = {
            self.TEAM_ONE: team_one,
            self.TEAM_TWO: team_two,
            self.TEAM_ONE_SCORE: team_one_score,
            self.TEAM_TWO_SCORE: team_two_score,
            self.WINNER: winner,
        }

        return game_model
    
    def to_dict(self) -> dict[str,]:
        team_one = self.team_one.get_id()
        team_two = self.team_two.get_id()
        team_one_score = self.team_one_score
        team_two_score = self.team_two_score
        winner = self.get_winner().get_id()

        game_model = {
            self.ID: str(self.id),
            self.TEAM_ONE: team_one,
            self.TEAM_TWO: team_two,
            self.TEAM_ONE_SCORE: team_one_score,
            self.TEAM_TWO_SCORE: team_two_score,
            self.WINNER: winner,
        }

        return game_model