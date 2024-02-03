

class Team:

    def __init__(self, id, name, team_record, is_user_team):
        self.id = id
        self.name = name
        self.is_user_team = is_user_team
        self.team_record = team_record
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

    def get_team_record(self):
        return self.team_record

    def set_team_record(self, value):
        self.team_record = value

    def get_players(self):
        return self.players

    def add_player(self, value):
        self.players.append(value)
