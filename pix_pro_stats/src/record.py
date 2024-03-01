from constants import *

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

    def to_model(self):
        games_won = self.get_games_won()
        games_played = self.get_games_played()

        record_model = {
            PYMONGO_GAMES_WON: games_won,
            PYMONGO_GAMES_PLAYED: games_played
        }
        return record_model