import GeneralStats


class PitchingStats(GeneralStats):

    def __init__(self, strike_outs, at_bats, innings_outs, pitches, walks, home_runs, num_games, strikes, earned_runs, hits, balls, runs):
        GeneralStats.__init__(self, strike_outs, at_bats, walks, home_runs, strikes, hits, balls, runs)
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
