from pitching_stats import PitchingStats
from batting_stats import BattingStats
from constants import *
class Player:

    def __init__(self, id: str, name: str, handedness: int, position: int, pitcher_type: int, designated_hitter: bool, season_batting: BattingStats,
                 team_batting: BattingStats, season_pitching: PitchingStats, team_pitching: PitchingStats, is_hof: bool):
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

    def get_id(self) -> str:
        return self.id

    def set_id(self, value: str):
        self.id = value

    def get_name(self) -> str:
        return self.name

    def set_name(self, value: str):
        self.name = value

    def get_handedness(self) -> int:
        return self.handedness

    def set_handedness(self, value: int):
        self.handedness = value

    def get_position(self) -> int:
        return self.position

    def set_position(self, value: int):
        self.position = value

    def get_pitcher_type(self) -> int:
        return self.pitcher_type

    def set_pitcher_type(self, value: int):
        self.pitcher_type = value

    def get_designated_hitter(self) -> bool:
        return self.designated_hitter

    def set_designated_hitter(self, value: bool):
        self.designated_hitter = value

    def get_season_batting(self) -> BattingStats:
        return self.season_batting

    def set_season_batting(self, value: BattingStats):
        self.season_batting = value

    def get_team_batting(self) -> BattingStats:
        return self.team_batting

    def set_team_batting(self, value: BattingStats):
        self.team_batting = value

    def get_season_pitching(self) -> PitchingStats:
        return self.season_pitching

    def set_season_pitching(self, value: PitchingStats):
        self.season_pitching = value

    def get_team_pitching(self) -> PitchingStats:
        return self.team_pitching

    def set_team_pitching(self, value: PitchingStats):
        self.team_pitching = value
    
    def get_is_hof(self) -> bool:
        return self.is_hof
    
    def set_is_hof(self, is_hof: bool):
        self.is_hof = is_hof
    
    def to_model(self) -> dict[str,]:
        player_id = self.get_id()
        player_name = self.get_name()
        player_handedness = self.get_handedness()
        player_position = self.get_position()
        player_pitcher_type = self.get_pitcher_type()
        player_designated_hitter = self.get_designated_hitter()
        player_is_hof = self.get_is_hof()

        player_model = {
            PYMONGO_PLAYER_ID: player_id,
            PYMONGO_PLAYER_NAME: player_name,
            PYMONGO_PLAYER_HANDEDNESS: player_handedness,
            PYMONGO_PLAYER_POSISTION: player_position,
            PYMONGO_PLAYER_PITCHER_TYPE: player_pitcher_type,
            PYMONGO_PLAYER_DESIGNATED_HITTER: player_designated_hitter,
            PYMONGO_PLAYER_IS_HOF: player_is_hof
        }
        return player_model
    
    def to_dict(self, season_year: int, current_player_pitching: list, current_player_batting: list) -> dict[str,]:
        player_id = self.get_id()
        player_name = self.get_name()
        player_handedness = self.get_handedness()
        player_position = self.get_position()
        player_pitcher_type = self.get_pitcher_type()
        player_designated_hitter = self.get_designated_hitter()
        player_is_hof = self.get_is_hof()
        player_season_pitching = {}
        # player_team_pitching = {}
        player_season_batting = {}
        # player_team_batting = {}
        if player_position == PITCHER:
            player_season_pitching = self.get_season_pitching().to_dict(season_year)
            current_player_pitching.append(player_season_pitching)
            # player_team_pitching = self.get_team_pitching().to_dict()
        else:
            player_season_batting = self.get_season_batting().to_dict(season_year)
            current_player_batting.append(player_season_batting)
            # player_team_batting = self.get_team_batting().to_dict()

        player_model = {
            PYMONGO_PLAYER_ID: player_id,
            PYMONGO_PLAYER_NAME: player_name,
            PYMONGO_PLAYER_HANDEDNESS: player_handedness,
            PYMONGO_PLAYER_POSISTION: player_position,
            PYMONGO_PLAYER_PITCHER_TYPE: player_pitcher_type,
            PYMONGO_PLAYER_DESIGNATED_HITTER: player_designated_hitter,
            PYMONGO_PITCHING_STATS_COLLECTION: current_player_pitching,
            # PYMONGO_TEAM_PITCHING_STATS_COLLECTION: player_team_pitching,
            PYMONGO_BATTING_STATS_COLLECTION: current_player_batting,
            # PYMONGO_TEAM_BATTING_STATS_COLLECTION: player_team_batting,
            PYMONGO_PLAYER_IS_HOF: player_is_hof
        }
        return player_model

    def create_hof_class_model(self) -> dict[str, str]:
        hof_class_model = {
            PYMONGO_PLAYER: self.id,
            PYMONGO_YEAR: YEAR 
        }
        return hof_class_model