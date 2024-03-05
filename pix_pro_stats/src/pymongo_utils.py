
from season import Season
from playoffs import Playoffs
from series import Series
from game import Game
from team import Team
from record import Record
from player import Player
from awards import Awards
from batting_stats import BattingStats
from pitching_stats import PitchingStats
from mongodb_utils import Database
from pymongo.cursor import Cursor
from constants import *

class PyMongoUtils:

    @staticmethod
    def update_player_hof(player: Player, database: Database) -> None:
        player_id = player.get_id()
        player_model = player.to_model()
        player_collection = database.get_collection(PYMONGO_PLAYER_COLLECTION)
        player_collection.update_one({PYMONGO_PLAYER_ID: player_id}, {PYMONGO_SET: player_model})

    @staticmethod
    def insert_hof_class(player: Player, database: Database) -> None:
        hof_class_model = player.create_hof_class_model()
        hof_class_collection = database.get_collection(PYMONGO_HOF_CLASS_COLLECTION)
        hof_class_collection.insert_one(hof_class_model)

    @staticmethod
    def insert_awards(awards: Awards, database: Database) -> str:
        awards_model = awards.to_model()
        awards_collection = database.get_collection(PYMONGO_AWARDS_COLLECTION)
        awards_id = awards_collection.insert_one(awards_model).inserted_id
        return str(awards_id)
    
    #probably don't need this but I'll leave it in just in case
    @staticmethod
    def insert_season_to_awards(season: Season, awards_id: str, season_id: str, database: Database) -> None:
        season_awards = season.create_season_awards_model(season_id, awards_id)

        season_to_awards_collection = database.get_collection(PYMONGO_SEASON_AWARDS_COLLECTION)
        season_to_awards_collection.insert_one(season_awards)


    @staticmethod
    def insert_game(game: Game, database: Database) -> str:
        game_model = game.to_model()

        game_collection = database.get_collection(PYMONGO_GAME_COLLECTION)
        game_id = game_collection.insert_one(game_model).inserted_id
        return str(game_id)

    @staticmethod
    def insert_games(games: list[Game], database: Database) -> list[str]:
        game_ids = []
        for game in games:
            game_id = PyMongoUtils.insert_game(game, database)
            game_ids.append(game_id)

        return game_ids

    @staticmethod
    def insert_series(series: Series, database: Database) -> str:
        games = PyMongoUtils.insert_games(series.get_games(), database)
        series_model = series.to_model(games)
        series_collection = database.get_collection(PYMONGO_SERIES_COLLECTION)
        series_id = series_collection.insert_one(series_model).inserted_id
        return str(series_id)

    @staticmethod
    def insert_playoffs(playoffs: Playoffs, database: Database) -> str:
        nl_wildcard  = PyMongoUtils.insert_series(playoffs.get_nl_wildcard(), database)
        al_wildcard = PyMongoUtils.insert_series(playoffs.get_al_wildcard(), database)
        nl_divisional_one = PyMongoUtils.insert_series(playoffs.get_nl_divisional_one(), database)
        al_divisional_one = PyMongoUtils.insert_series(playoffs.get_al_divisional_one(), database)
        nl_divisional_two = PyMongoUtils.insert_series(playoffs.get_nl_divisional_two(), database)
        al_divisional_two = PyMongoUtils.insert_series(playoffs.get_al_divisional_two(), database)
        nl_championship = PyMongoUtils.insert_series(playoffs.get_nl_championship(), database)
        al_championship = PyMongoUtils.insert_series(playoffs.get_al_championship(), database)
        world_series = PyMongoUtils.insert_series(playoffs.get_world_series(), database)

        playoff_model = playoffs.to_model(al_wildcard, nl_wildcard, al_divisional_one, nl_divisional_one,
                                          al_divisional_two, nl_divisional_two, al_championship, nl_championship,
                                          world_series)

        playoffs_collection = database.get_collection(PYMONGO_PLAYOFFS_COLLECTION)
        playoffs_id = playoffs_collection.insert_one(playoff_model).inserted_id

        return str(playoffs_id)

    @staticmethod
    def insert_record(record: Record, database: Database) -> str:
        record_model = record.to_model()

        record_collection = database.get_collection(PYMONGO_RECORD_COLLECTION)
        record_id = record_collection.insert_one(record_model).inserted_id
        return str(record_id)

    @staticmethod
    def insert_teams_record(team: Team, season_id: str, database: Database) -> None:
        record_id = PyMongoUtils.insert_record(team.get_record(), database)
        team_record_model = team.create_team_record_model(record_id, season_id)

        teams_records_collection = database.get_collection(PYMONGO_TEAM_RECORD_COLLECTION)
        teams_records_collection.insert_one(team_record_model)

    @staticmethod
    def insert_team_player_season(team: Team, player_id: str, season_id: str, database: Database) -> None:
        team_player_season_model = team.create_team_player_season_model(player_id, season_id)

        team_player_season_collection = database.get_collection(PYMONGO_TEAM_SEASON_PLAYERS_COLLECTION)
        team_player_season_collection.insert_one(team_player_season_model)

    @staticmethod
    def insert_team_players_season(team: Team, season_id: str, database: Database) -> None:
        for player in team.get_players():
            player_id = player.get_id()
            PyMongoUtils.insert_team_player_season(team, player_id, season_id, database)

    @staticmethod   
    def insert_team(team: Team, database: Database) -> None:
        team_id = team.get_id()
        team_model = team.to_model()

        teams_collection = database.get_collection(PYMONGO_TEAM_COLLECTION)
        found_team = teams_collection.find_one({PYMONGO_TEAM_ID: team_id})
        #we only need to insert the team if it doesn't exist
        if not found_team:
            teams_collection.insert_one(team_model)

    @staticmethod
    def insert_player(player: Player, database: Database) -> None:
        player_id = player.get_id()
        player_model = player.to_model()

        player_collection = database.get_collection(PYMONGO_PLAYER_COLLECTION)
        found_player = player_collection.find_one({PYMONGO_PLAYER_ID: player_id})
        #we only need to insert the player if is not there
        if not found_player:
            player_collection.insert_one(player_model)

    @staticmethod
    def insert_players(players: list[Player], database: Database) -> None:
        for player in players:
            PyMongoUtils.insert_player(player, database)

    @staticmethod
    def upsert_batting_stats(batting_stats_obj: BattingStats, player_id: str, season_id: str, database: Database) -> None:
        team_id = batting_stats_obj.get_team_id()
        batting_stats_model = batting_stats_obj.to_model(player_id, season_id)

        batting_stats_collection = database.get_collection(PYMONGO_BATTING_STATS_COLLECTION)
        batting_stats_collection.update_one({PYMONGO_PLAYER: player_id, PYMONGO_TEAM: team_id, PYMONGO_SEASON: season_id}, {PYMONGO_SET: batting_stats_model}, upsert=True)

    @staticmethod
    def upsert_pitching_stats(pitching_stats_obj: PitchingStats, player_id: str, season_id: str, database: Database) -> None:
        team_id = pitching_stats_obj.get_team_id()
        pitching_stats_model = pitching_stats_obj.to_model(player_id, season_id)

        pitching_stats_collection = database.get_collection(PYMONGO_PITCHING_STATS_COLLECTION)
        pitching_stats_collection.update_one({PYMONGO_PLAYER: player_id, PYMONGO_SEASON: season_id, PYMONGO_TEAM: team_id}, {PYMONGO_SET: pitching_stats_model}, upsert=True)

    @staticmethod
    def upsert_player_stats(player: Player, season_id: str, database: Database) -> None:
        player_id = player.get_id()
        season_batting = player.get_season_batting()
        season_pitching = player.get_season_pitching()
        team_batting = player.get_team_batting()
        team_pitching = player.get_team_pitching()

        PyMongoUtils.upsert_batting_stats(season_batting, player_id, season_id, database)
        PyMongoUtils.upsert_pitching_stats(season_pitching, player_id, season_id, database)
        PyMongoUtils.upsert_batting_stats(team_batting, player_id, None, database)
        PyMongoUtils.upsert_pitching_stats(team_pitching, player_id, None, database)

    @staticmethod
    def upsert_players_stats(players: list[Player], season_id: str, database: Database) -> None:
        for player in players:
            PyMongoUtils.upsert_player_stats(player, season_id, database)

    @staticmethod
    def insert_season(season: Season, database: Database) -> str:
        playoffs = PyMongoUtils.insert_playoffs(season.get_playoffs(), database)
        regular_season = PyMongoUtils.insert_games(season.get_regular_season(), database)
        PyMongoUtils.insert_teams(season.get_teams(), database)
        awards = PyMongoUtils.insert_awards(season.get_awards(), database)
        season_model = season.to_model(playoffs, awards, regular_season)
    
        season_collection = database.get_collection(PYMONGO_SEASON_COLLECTION)
        season_id = season_collection.insert_one(season_model).inserted_id
        return str(season_id)

    @staticmethod
    def insert_teams(teams: list[Team], database: Database) -> None:
        for team in teams:
            PyMongoUtils.insert_team(team, database)

    @staticmethod
    def insert_teams_records(teams: list[Team], season_id: str, database: Database) -> None:
        for team in teams:
            PyMongoUtils.insert_teams_record(team, season_id, database)

    @staticmethod
    def insert_teams_players_season(teams: list[Team], season_id: str, database: Database) -> None:
        for team in teams: 
            PyMongoUtils.insert_team_players_season(team, season_id, database)

    @staticmethod
    def insert_teams_players(teams: list[Team], database: Database) -> None:
        for team in teams:
            PyMongoUtils.insert_players(team.get_players(), database)

    @staticmethod
    def upsert_teams_players_stats(teams: list[Team], season_id: str, database: Database) -> None:
        for team in teams: 
            PyMongoUtils.upsert_players_stats(team.get_players(), season_id, database)

    @staticmethod
    def get_all_player_pitching(player_id, database: Database) -> Cursor:
        pitching_collection = database.get_collection(PYMONGO_PITCHING_STATS_COLLECTION)
        all_stats = pitching_collection.find({PYMONGO_PLAYER : player_id, PYMONGO_TEAM : TEAM_NO_ID})
        return list(all_stats)

    @staticmethod
    def get_all_player_batting(player_id, database: Database) -> Cursor:
        batting_collection = database.get_collection(PYMONGO_BATTING_STATS_COLLECTION)
        all_stats = batting_collection.find({PYMONGO_PLAYER : player_id, PYMONGO_TEAM : TEAM_NO_ID})
        return list(all_stats)
    
    @staticmethod
    def insert_seasons_awards(awards: Awards, season_id, database: Database) -> None:
        awards_id = PyMongoUtils.insert_awards(awards, database)
        PyMongoUtils.insert_season_award(awards_id, season_id, database)
    
    @staticmethod
    def update_players_hof(players: list[Player], database) -> None:
        for player in players:
            PyMongoUtils.update_player_hof(player, database)
            PyMongoUtils.insert_hof_class(player, database)