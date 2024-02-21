

class Team:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.is_user_team = False
        self.record = None
        self.players = []



    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_is_user_team(self):
        return self.is_user_team

    def set_is_user_team(self, value):
        self.is_user_team = value

    def get_record(self):
        return self.record

    def set_record(self, value):
        self.record = value

    def get_players(self):
        return self.players

    def add_player(self, value):
        self.players.append(value)
