from constants import *
import uuid

class GeneralStats:
    ID='id'
    STRIKE_OUTS='strikeOuts'
    AT_BATS='atBats'
    WALKS='walks'
    HOME_RUNS='homeRuns'
    NUMBER_OF_GAMES='numGames'
    STRIKES='strikes'
    HITS='hits'
    BALLS='balls'
    RUNS='runs'
    def __init__(self, strike_outs: int, at_bats: int, walks: int, home_runs: int, num_games: int, strikes: int, hits: int, balls: int, runs: int, team_id: int):
        self.id = uuid.uuid4()
        self.strike_outs = strike_outs
        self.at_bats = at_bats
        self.walks = walks
        self.home_runs = home_runs
        self.num_games = num_games
        self.strikes = strikes
        self.hits = hits
        self.balls = balls
        self.runs = runs
        self.team_id = team_id

    def get_strike_outs(self) -> int:
        return self.strike_outs

    def set_strike_outs(self, value: int):
        self.strike_outs = value

    def get_at_bats(self) -> int:
        return self.at_bats

    def set_at_bats(self, value: int):
        self.at_bats = value

    def get_walks(self) -> int:
        return self.walks

    def set_walks(self, value: int):
        self.walks = value

    def get_home_runs(self) -> int:
        return self.home_runs

    def set_home_runs(self, value: int):
        self.home_runs = value

    def get_num_games(self) -> int:
        return self.num_games

    def set_num_games(self, value: int):
        self.num_games = value

    def get_strikes(self) -> int:
        return self.strikes

    def set_strikes(self, value: int):
        self.strikes = value

    def get_hits(self) -> int:
        return self.hits

    def set_hits(self, value: int):
        self.hits = value

    def get_balls(self) -> int:
        return self.balls

    def set_balls(self, value: int):
        self.balls = value

    def get_runs(self) -> int:
        return self.runs

    def set_runs(self, value: int):
        self.runs = value
    
    def get_team_id(self) -> int:
        return self.team_id

    def set_team_id(self, value: int):
        self.team_id = value
    
    @DeprecationWarning
    def to_model(self) -> dict[int, int]:
        return {
            self.STRIKE_OUTS: self.strike_outs,
            self.AT_BATS: self.at_bats,
            League.TEAM: self.team_id,
            self.HOME_RUNS: self.home_runs,
            self.WALKS: self.walks,
            self.NUMBER_OF_GAMES: self.num_games,
            self.STRIKES: self.strikes,
            self.HITS: self.hits,
            self.BALLS: self.balls,
            self.RUNS: self.runs,
        }
    
    def to_dict(self, season_year: int) -> dict[int, int]:
        return {
            self.ID: str(self.id),
            League.SEASON: season_year,
            self.STRIKE_OUTS: self.strike_outs,
            self.AT_BATS: self.at_bats,
            League.TEAM: self.team_id,
            self.HOME_RUNS: self.home_runs,
            self.WALKS: self.walks,
            self.NUMBER_OF_GAMES: self.num_games,
            self.STRIKES: self.strikes,
            self.HITS: self.hits,
            self.BALLS: self.balls,
            self.RUNS: self.runs,
        }