

class Record:

    def __init__(self, games_won, games_played):
        self.games_won = games_won
        self.games_played = games_played

    def get_games_won(self):
        return self.games_won

    def set_games_won(self, value):
        self.games_won = value

    def get_games_played(self):
        return self.games_played

    def set_games_played(self, value):
        self.games_played = value
