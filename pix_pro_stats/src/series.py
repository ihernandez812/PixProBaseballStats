

class Series:

    def __init__(self, games):
        self.games = games:
    
    def add_game(self, game):
        self.games.append(game)

    def get_games(self):
        return game

    def get_series_winner(self):
        series_winner = None
        game = self.games[0]
        team_one = game.get_team_one()
        team_two = game.get_team_two()
        team_one_win_count = 0
        for game in games:
            winning_team = game.get_winner()
            if team_one.get_id() == winning_team.get_id():
                team_one_win_count += 1
        
        series_length = len(self.games)

        if team_one_win_count > (series_length // 2):
            series_winner = team_one
        else:
            series_winner = team_two
        
        return series_winner