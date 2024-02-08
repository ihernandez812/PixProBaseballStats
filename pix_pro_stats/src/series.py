
class Series:

    def __init__(self, team_one, team_two, winner_id, games, series_length):
        self.team_one = team_one
        self.team_two = team_two
        self.winner_id = winner_id
        self.games = games
        self.series_length = series_length

    def get_team_one(self):
        return self.team_one

    def get_team_two(self):
        return self.team_two

    def add_game(self, game):
        self.games.append(game)

    def get_games(self):
        return self.games
    
    def get_series_length(self):
        return self.series_length

    def get_series_winner(self):
        series_winner = None
        team_one_id = self.team_one.get_id()
        team_two_id = self.team_two.get_id()
        if team_one_id == self.winner_id:
            series_winner = self.team_one
        else:
            series_winner = self.team_two

        return series_winner