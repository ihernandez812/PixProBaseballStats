from enum import Enum
from pitching_stats import PitchingStats
from batting_stats import BattingStats
from constants import *

class Player:
    STATS='stats'
    NAME='name'
    ID='id'
    HANDEDNESS='handed'
    SEASON_BATTING='seasonBatting'
    SEASON_PITCHING='seasonPitching'
    POSITION='fieldingPosition'
    DESIGNATED_HITTER='designatedHitter'
    PITCHING='pitching'
    PITCHING_TYPE='pitcherType'
    LEFT_HANDED=-1
    RIGHT_HANDED=1
    IS_HOF='is_hof'
    BATTING_STATS='battingStats'
    PITCHING_STATS='pitchingStats'
    AGE='age'
    def __init__(self, id: str, name: str, age: int, overall: float, handedness: int, position: int, pitcher_type: int, designated_hitter: bool, season_batting: BattingStats,
                season_pitching: PitchingStats,  is_hof: bool):
        self.id = id
        self.name = name
        self.handedness = handedness
        self.position = position
        self.pitcher_type = pitcher_type
        self.designated_hitter = designated_hitter
        self.season_batting = season_batting
        self.season_pitching = season_pitching
        self.is_hof = is_hof
        #Only need this if this is a brand new player
        self.age = age
        self.overall = overall

    def get_id(self) -> str:
        return self.id

    def set_id(self, value: str):
        self.id = value

    def get_name(self) -> str:
        return self.name

    def set_name(self, value: str):
        self.name = value

    def get_age(self, year: int) -> int:
        return self.age[year]
    
    def set_age(self, year: int, age: int):
        self.age[year] = age

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

    def get_season_pitching(self) -> PitchingStats:
        return self.season_pitching

    def set_season_pitching(self, value: PitchingStats):
        self.season_pitching = value
    
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
            Player.ID: player_id,
            Player.NAME: player_name,
            Player.HANDEDNESS: player_handedness,
            Player.POSISTION: player_position,
            Player.PITCHER_TYPE: player_pitcher_type,
            Player.DESIGNATED_HITTER: player_designated_hitter,
            Player.IS_HOF: player_is_hof
        }
        return player_model
    
    def to_dict(self, season_year: int, current_player_pitching: list=None, current_player_batting: list=None, current_player_age: int=0) -> dict[str,]:
        if current_player_batting is None:
            current_player_batting = []
        if current_player_pitching is None:
            current_player_pitching = []

        player_season_pitching = {}
        player_season_batting = {}
        if self.position == PlayerType.PITCHER.value:
            player_season_pitching = self.season_pitching.to_dict(season_year)
            current_player_pitching.append(player_season_pitching)
        else:
            player_season_batting = self.season_batting.to_dict(season_year)
            current_player_batting.append(player_season_batting)

        #There is a bug in the app so I need to update the age based off the last season
        #If it is zero it means it was a new player and we can just use the one from the json
        if current_player_age != 0:
            self.age = current_player_age+1
        
            

        player_model = {
            Player.ID: self.id,
            Player.NAME: self.name,
            Player.AGE: self.age,
            Player.HANDEDNESS: self.handedness,
            Player.POSITION: self.position,
            Player.PITCHING_TYPE: self.pitcher_type,
            Player.DESIGNATED_HITTER: self.designated_hitter,
            Player.PITCHING_STATS: current_player_pitching,
            Player.BATTING_STATS: current_player_batting,
            Player.IS_HOF: self.is_hof
        }
        return player_model

    @DeprecationWarning
    def create_hof_class_model(self) -> dict[str, str]:
        hof_class_model = {
            Player.ID: self.id,
            League.YEAR: League.YEAR 
        }
        return hof_class_model
    
class PlayerType(Enum):
    PITCHER=0
    CATCHER=1
    FIRST_BASE=2
    SECOND_BASE=3
    THIRD_BASE=4
    SHORT_STOP=5
    LEFT_FIELD=6
    CENTER_FIELD=7
    RIGHT_FIELD=8

class PitcherType(Enum):
    NOT_PITCHER=-1
    STATER=0
    RELIEVER=1
    CLOSER=2
