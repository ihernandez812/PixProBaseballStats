from general_stats import GeneralStats
from constants import *

class PitchingStats(GeneralStats):
    INNINGS_OUTS='inningsOuts'
    PITCHES='pitches'
    EARNED_RUNS='earnedRuns'
    
    def __init__(self, strike_outs: int=None, at_bats: int=None, innings_outs: int=None, pitches: int=None, walks: int=None, home_runs: int=None, num_games: int=None,
                 strikes: int=None, earned_runs: int=None, hits: int=None, balls: int=None, runs: int=None, team_id: int=None) -> None:
        GeneralStats.__init__(self, strike_outs, at_bats, walks, home_runs, num_games,strikes, hits, balls, runs, team_id)
        self.innings_outs = innings_outs
        self.pitches = pitches
        self.earned_runs = earned_runs

    def get_innings_outs(self) -> int:
        return self.innings_outs

    def set_innings_outs(self, value: int):
        self.innings_outs = value

    def get_pitches(self) -> int:
        return self.pitches

    def set_pitches(self, value: int):
        self.pitches = value

    def get_earned_runs(self) -> int:
        return self.earned_runs

    def set_earned_runs(self, value: int):
        self.earned_runs = value

    @DeprecationWarning
    def to_model(self, player_id: str, season_id: str) -> dict[str,]:
        general_stats = super().to_model()
        pitching_stats =  {
            self.INNINGS_OUTS: self.innings_outs,
            self.PITCHES: self.pitches,
            self.EARNED_RUNS: self.earned_runs,
            League.PLAYER: player_id,
            League.SEASON: season_id
        }
        pitching_stats.update(general_stats)
        return pitching_stats
    
    def to_dict(self, season_year: int) -> dict[str,]:
        general_stats = super().to_dict(season_year)
        pitching_stats =  {
            self.INNINGS_OUTS: self.innings_outs,
            self.PITCHES: self.pitches,
            self.EARNED_RUNS: self.earned_runs,
        }
        pitching_stats.update(general_stats)
        return pitching_stats