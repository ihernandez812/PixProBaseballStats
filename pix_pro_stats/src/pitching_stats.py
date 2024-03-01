from general_stats import GeneralStats
from constants import *

class PitchingStats(GeneralStats):

    def __init__(self, strike_outs, at_bats, innings_outs, pitches, walks, home_runs, num_games, strikes, earned_runs, hits, balls, runs, team_id):
        GeneralStats.__init__(self, strike_outs, at_bats, walks, home_runs, num_games,strikes, hits, balls, runs, team_id)
        self.innings_outs = innings_outs
        self.pitches = pitches
        self.earned_runs = earned_runs

    def get_innings_outs(self):
        return self.innings_outs

    def set_innings_outs(self, value):
        self.innings_outs = value

    def get_pitches(self):
        return self.pitches

    def set_pitches(self, value):
        self.pitches = value

    def get_earned_runs(self):
        return self.earned_runs

    def set_earned_runs(self, value):
        self.earned_runs = value

    def to_model(self, player_id: str, season_id: str):
        general_stats = super().to_model()
        pitching_stats =  {
            PYMONGO_STATS_INNINGS_OUTS: self.innings_outs,
            PYMONGO_STATS_PITCHES: self.pitches,
            PYMONGO_STATS_EARNED_RUNS: self.earned_runs,
            PYMONGO_PLAYER: player_id,
            PYMONGO_SEASON: season_id
        }
        pitching_stats.update(general_stats)
        return pitching_stats