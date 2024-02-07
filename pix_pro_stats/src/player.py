from pitching_stats import PitchingStats
from batting_stats import BattingStats

class Player:

    def __init__(self, id, name, handedness, position, pitcher_type, designated_hitter, season_batting, team_batting, season_pitching, team_pitching, is_hof):
        self.id = id
        self.name = name
        self.handedness = handedness
        self.position = position
        self.pitcher_type = pitcher_type
        self.designated_hitter = designated_hitter
        self.season_batting = season_batting
        self.team_batting = team_batting
        self.season_pitching = season_pitching
        self.team_pitching = team_pitching
        self.is_hof = is_hof

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_handedness(self):
        return self.handedness

    def set_handedness(self, value):
        self.handedness = value

    def get_position(self):
        return self.position

    def set_position(self, value):
        self.position = value

    def get_pitcher_type(self):
        return self.pitcher_type

    def set_pitcher_type(self, value):
        self.pitcher_type = value

    def get_designated_hitter(self):
        return self.designated_hitter

    def set_designated_hitter(self, value):
        self.designated_hitter = value

    def get_season_batting(self):
        return self.season_batting

    def set_season_batting(self, value):
        self.season_batting = value

    def get_team_batting(self):
        return self.team_batting

    def set_team_batting(self, value):
        self.team_batting = value

    def get_season_pitching(self):
        return self.season_pitching

    def set_season_pitching(self, value):
        self.season_pitching = value

    def get_team_pitching(self):
        return self.team_pitching

    def set_team_pitching(self, value):
        self.team_pitching = value
    
    def get_is_hof(self):
        return self.is_hof
    
    def set_is_hof(self, is_hof):
        self.is_hof = is_hof