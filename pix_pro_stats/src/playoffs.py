from series import Series
from constants import *

class Playoffs:
    def __init__(self, al_wildcard, nl_wildcard, al_divisional_one, nl_divisional_one, al_divisional_two, nl_divisional_two,
                al_championship, nl_championship, world_series):
        self.al_wildcard = al_wildcard
        self.nl_wildcard = nl_wildcard
        self.al_divisional_one = al_divisional_one
        self.nl_divisional_one = nl_divisional_one
        self.al_divisional_two = al_divisional_two
        self.nl_divisional_two = nl_divisional_two
        self.al_championship = al_championship
        self.nl_championship = nl_championship
        self.world_series = world_series

    def get_al_wildcard(self):
        return self.al_wildcard

    def set_al_wildcard(self, value):
        self.al_wildcard = value

    def get_nl_wildcard(self):
        return self.nl_wildcard

    def set_nl_wildcard(self, value):
        self.nl_wildcard = value

    def get_al_divisional_one(self):
        return self.al_divisional_one

    def set_al_divisional_one(self, value):
        self.al_divisional_one = value

    def get_al_divisional_two(self):
        return self.al_divisional_two

    def set_al_divisional_two(self, value):
        self.al_divisional_two = value

    def get_nl_divisional_one(self):
        return self.nl_divisional_one

    def set_nl_divisional_one(self, value):
        self.nl_divisional_one = value

    def get_nl_divisional_two(self):
        return self.nl_divisional_two

    def set_nl_divisional_two(self, value):
        self.nl_divisional_two = value

    def get_al_championship(self):
        return self.al_championship

    def set_al_championship(self, value):
        self.al_championship = value

    def get_nl_championship(self):
        return self.nl_championship

    def set_nl_championship(self, value):
        self.nl_championship = value

    def get_world_series(self):
        return self.world_series

    def set_world_series(self, value):
        self.world_series = value

    def to_model(self,al_wildcard, nl_wildcard, al_divisional_one, nl_divisional_one, al_divisional_two,
                nl_divisional_two, al_championship, nl_championship, world_series):
        playoff_model = {
            PYMONGO_NL_WILDCARD: nl_wildcard,
            PYMONGO_AL_WILDCARD: al_wildcard,
            PYMONGO_NL_DIVISIONAL_ONE: nl_divisional_one,
            PYMONGO_AL_DIVISIONAL_ONE: al_divisional_one,
            PYMONGO_NL_DIVISIONAL_TWO: nl_divisional_two,
            PYMONGO_AL_DIVISIONAL_TWO: al_divisional_two,
            PYMONGO_NL_CHAMPIONSHIP: nl_championship,
            PYMONGO_AL_CHAMPIONSHIP: al_championship,
            PYMONGO_WORLD_SERIES: world_series
        }