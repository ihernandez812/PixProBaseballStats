from constants import *

class GeneralStats:

    def __init__(self, strike_outs, at_bats, walks, home_runs, num_games, strikes, hits, balls, runs, team_id):
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

    def get_strike_outs(self):
        return self.strike_outs

    def set_strike_outs(self, value):
        self.strike_outs = value

    def get_at_bats(self):
        return self.at_bats

    def set_at_bats(self, value):
        self.at_bats = value

    def get_walks(self):
        return self.walks

    def set_walks(self, value):
        self.walks = value

    def get_home_runs(self):
        return self.home_runs

    def set_home_runs(self, value):
        self.home_runs = value

    def get_num_games(self):
        return self.num_games

    def set_num_games(self, value):
        self.num_games = value

    def get_strikes(self):
        return self.strikes

    def set_strikes(self, value):
        self.strikes = value


    def get_hits(self):
        return self.hits

    def set_hits(self, value):
        self.hits = value

    def get_balls(self):
        return self.balls

    def set_balls(self, value):
        self.balls = value

    def get_runs(self):
        return self.runs

    def set_runs(self, value):
        self.runs = value
    
    def get_team_id(self):
        return self.team_id

    def set_team_id(self, value):
        self.team_id = value
    
    def to_model(self):
        return {
            PYMONGO_STATS_STRIKE_OUTS: self.strike_outs,
            PYMONGO_STATS_AT_BATS: self.at_bats,
            PYMONGO_TEAM: self.team_id,
            PYMONGO_STATS_HOME_RUNS: self.home_runs,
            PYMONGO_STATS_WALKS: self.walks,
            PYMONGO_STATS_NUMBER_OF_GAMES: self.num_games,
            PYMONGO_STATS_STRIKES: self.strikes,
            PYMONGO_STATS_HITS: self.hits,
            PYMONGO_STATS_BALLS: self.balls,
            PYMONGO_STATS_RUNS: self.runs,
        }