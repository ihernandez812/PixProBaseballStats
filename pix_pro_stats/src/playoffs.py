from series import Series
from constants import *

class Playoffs:
    POST_SEASON_LEAGUES='postSeasonLeagues'
    WORLD_SERIES='final'
    AL_CHAMPIONSHIP='confOneFinal'
    NL_CHAMPIONSHIP='confTwoFinal'
    AL_DIVISIONAL='confOneSemi{series}'
    NL_DIVISIONAL='confTwoSemi{series}'
    AL_WILDCARD='confOneWildcard'
    NL_WILDCARD='confTwoWildcard'
    
    def __init__(self, al_wildcard: Series, nl_wildcard: Series, al_divisional_one: Series, nl_divisional_one: Series, al_divisional_two: Series, nl_divisional_two: Series,
                al_championship: Series, nl_championship: Series, world_series: Series) -> None:
        self.al_wildcard = al_wildcard
        self.nl_wildcard = nl_wildcard
        self.al_divisional_one = al_divisional_one
        self.nl_divisional_one = nl_divisional_one
        self.al_divisional_two = al_divisional_two
        self.nl_divisional_two = nl_divisional_two
        self.al_championship = al_championship
        self.nl_championship = nl_championship
        self.world_series = world_series

    def get_al_wildcard(self) -> Series:
        return self.al_wildcard

    def set_al_wildcard(self, value: Series):
        self.al_wildcard = value

    def get_nl_wildcard(self) -> Series:
        return self.nl_wildcard

    def set_nl_wildcard(self, value: Series):
        self.nl_wildcard = value

    def get_al_divisional_one(self) -> Series:
        return self.al_divisional_one

    def set_al_divisional_one(self, value: Series):
        self.al_divisional_one = value

    def get_al_divisional_two(self) -> Series:
        return self.al_divisional_two

    def set_al_divisional_two(self, value: Series):
        self.al_divisional_two = value

    def get_nl_divisional_one(self) -> Series:
        return self.nl_divisional_one

    def set_nl_divisional_one(self, value: Series):
        self.nl_divisional_one = value

    def get_nl_divisional_two(self) -> Series:
        return self.nl_divisional_two

    def set_nl_divisional_two(self, value: Series):
        self.nl_divisional_two = value

    def get_al_championship(self) -> Series:
        return self.al_championship

    def set_al_championship(self, value: Series):
        self.al_championship = value

    def get_nl_championship(self) -> Series:
        return self.nl_championship

    def set_nl_championship(self, value: Series):
        self.nl_championship = value

    def get_world_series(self) -> Series:
        return self.world_series

    def set_world_series(self, value: Series):
        self.world_series = value

    def to_model(self,al_wildcard: str, nl_wildcard: str, al_divisional_one: str, nl_divisional_one: str, al_divisional_two: str,
                nl_divisional_two: str, al_championship: str, nl_championship: str, world_series: str) -> dict[str,]:
        playoff_model = {
            self.NL_WILDCARD: nl_wildcard,
            self.AL_WILDCARD: al_wildcard,
            self.NL_DIVISIONAL_ONE: nl_divisional_one,
            self.AL_DIVISIONAL_ONE: al_divisional_one,
            self.NL_DIVISIONAL_TWO: nl_divisional_two,
            self.AL_DIVISIONAL_TWO: al_divisional_two,
            self.NL_CHAMPIONSHIP: nl_championship,
            self.AL_CHAMPIONSHIP: al_championship,
            self.WORLD_SERIES: world_series
        }
        return playoff_model
    
    def to_dict(self) -> dict[str,]:
        nl_divisional_one = self.NL_DIVISIONAL.format(series='0')
        nl_divisional_two = self.NL_DIVISIONAL.format(series='1')
        al_divisional_one = self.AL_DIVISIONAL.format(series='0')
        al_divisional_two = self.AL_DIVISIONAL.format(series='1')
        playoff_model = {
            self.NL_WILDCARD: self.nl_wildcard.to_dict(),
            self.AL_WILDCARD: self.al_wildcard.to_dict(),
            nl_divisional_one: self.nl_divisional_one.to_dict(),
            al_divisional_one: self.al_divisional_one.to_dict(),
            nl_divisional_two: self.nl_divisional_two.to_dict(),
            al_divisional_two: self.al_divisional_two.to_dict(),
            self.NL_CHAMPIONSHIP: self.nl_championship.to_dict(),
            self.AL_CHAMPIONSHIP: self.al_championship.to_dict(),
            self.WORLD_SERIES: self.world_series.to_dict()
        }
        return playoff_model