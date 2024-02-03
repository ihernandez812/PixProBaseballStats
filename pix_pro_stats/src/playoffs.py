from series import Series

class Playoffs:
    def __init__(self, al_wildcard, nl_wildcard, al_divisional, nl_divisional, al_championship, nl_championship, world_series):
        self.al_wildcard = al_wildcard
        self.nl_wildcard = nl_wildcard
        self.al_divisional = al_divisional
        self.nl_divisional = nl_divisional
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

    def get_al_divisional(self):
        return self.al_divisional

    def set_al_divisional(self, value):
        self.al_divisional = value

    def get_nl_divisional(self):
        return self.nl_divisional

    def set_nl_divisional(self, value):
        self.nl_divisional = value

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

