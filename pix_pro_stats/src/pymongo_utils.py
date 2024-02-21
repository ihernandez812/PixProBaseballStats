
from season import Season
from playoffs import Playoffs
from series import Series
from game import Game
from team import Team
from record import Record
from player import Player
from batting_stats import BattingStats
from pitching_stats import PitchingStats
from mongodb_utils import Database
from constants import *

class PymongoUtils:

    @staticmethod
    def insert_game(game: Game, database: Database):
        team_one = game.get_team_one().get_id()
        team_two = game.get_team_two().get_id()
        team_one_score = game.get_team_one_score()
        team_two_score = game.get_team_two_score()
        winner = game.get_winner().get_id()

        game_model = {
            PYMONGO_TEAM_ONE: team_one,
            PYMONGO_TEAM_TWO: team_two,
            PYMONGO_TEAM_ONE_SCORE: team_one_score,
            PYMONGO_TEAM_TWO_SCORE: team_two_score,
            PYMONGO_WINNER: winner,
        }

        game_collection = database.get_collection(PYMONGO_GAME_COLLECTION)
        game_id = game_collection.insert_one(game_model).inserted_id
        return str(game_id)

    @staticmethod
    def insert_games(games: list[Game], database: Database):
        game_ids = []
        for game in games:
            game_id = PymongoUtils.insert_game(game, database)
            game_ids.append(game_id)

        return game_ids

    @staticmethod
    def insert_series(series: Series, database: Database):
        team_one = series.get_team_one().get_id()
        team_two = series.get_team_two().get_id()
        winner = series.get_series_winner().get_id()
        games = PymongoUtils.insert_games(series.get_games(), database)
        series_length = series.get_series_length()

        series_model = {
            PYMONGO_TEAM_ONE: team_one,
            PYMONGO_TEAM_TWO: team_two,
            PYMONGO_WINNER: winner,
            PYMONGO_GAMES: games,
            PYMONGO_SERIES_LENGTH: series_length
        }

        series_collection = database.get_collection(PYMONGO_SERIES_COLLECTION)
        series_id = series_collection.insert_one(series_model).inserted_id
        return str(series_id)

    @staticmethod
    def insert_playoffs(playoffs: Playoffs, database: Database):
        nl_wildcard  = PymongoUtils.insert_series(playoffs.get_nl_wildcard(), database)
        al_wildcard = PymongoUtils.insert_series(playoffs.get_al_wildcard(), database)
        nl_divisional_one = PymongoUtils.insert_series(playoffs.get_nl_divisional_one(), database)
        al_divisional_one = PymongoUtils.insert_series(playoffs.get_al_divisional_one(), database)
        nl_divisional_two = PymongoUtils.insert_series(playoffs.get_nl_divisional_two(), database)
        al_divisional_two = PymongoUtils.insert_series(playoffs.get_al_divisional_two(), database)
        nl_championship = PymongoUtils.insert_series(playoffs.get_nl_championship(), database)
        al_championship = PymongoUtils.insert_series(playoffs.get_al_championship(), database)
        world_series = PymongoUtils.insert_series(playoffs.get_world_series(), database)

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

        playoffs_collection = database.get_collection(PYMONGO_PLAYOFFS_COLLECTION)
        playoffs_id = playoffs_collection.insert_one(playoff_model).inserted_id

        return str(playoffs_id)

    @staticmethod
    def insert_record(record: Record, database: Database):
        games_won = record.get_games_won()
        games_played = record.get_games_played()

        record_model = {
            PYMONGO_GAMES_WON: games_won,
            PYMONGO_GAMES_PLAYED: games_played
        }

        record_collection = database.get_collection(PYMONGO_RECORD_COLLECTION)
        record_id = record_collection.insert_one(record_model).inserted_id
        return str(record_id)

    @staticmethod
    def insert_teams_record(team: Team, season_id: str, database: Database):
        team_id = team.get_id()
        record_id = PymongoUtils.insert_record(team.get_record(), database)

        team_record_model = {
            PYMONGO_TEAM: team_id,
            PYMONGO_SEASON: season_id,
            PYMONGO_RECORD: record_id
        }

        teams_records_collection = database.get_collection(PYMONGO_TEAM_RECORD_COLLECTION)
        teams_records_collection.insert_one(team_record_model)

    @staticmethod
    def insert_team_player_season(player: Player, team_id: str, season_id: str, database: Database):
        team_player_season_model = {
            PYMONGO_PLAYER: player.get_id(),
            PYMONGO_TEAM: team_id,
            PYMONGO_SEASON: season_id
        }

        team_player_season_collection = database.get_collection(PYMONGO_TEAM_SEASON_PLAYERS_COLLECTION)
        team_player_season_collection.insert_one(team_player_season_model)

    @staticmethod
    def insert_team_players_season(team: Team, season_id: str, database: Database):
        for player in team.get_players():
            team_id = team.get_id()
            PymongoUtils.insert_team_player_season(player, team_id, season_id, database)

    @staticmethod   
    def insert_team(team: Team, database: Database):
        team_name = team.get_name()
        team_id = team.get_id() 
        is_user_team = team.get_is_user_team()

        team_model = {
            PYMONGO_TEAM_NAME: team_name,
            PYMONGO_TEAM_ID: team_id,
            PYMONGO_TEAM_IS_USER_TEAM: is_user_team
        }

        teams_collection = database.get_collection(PYMONGO_TEAM_COLLECTION)
        found_team = teams_collection.find_one({PYMONGO_TEAM_ID: team_id})
        #we only need to insert the team if it doesn't exist
        if not found_team:
            teams_collection.insert_one(team_model)

    @staticmethod
    def insert_player(player: Player, database: Database):
        player_id = player.get_id()
        player_name = player.get_name()
        player_handedness = player.get_handedness()
        player_position = player.get_position()
        player_pitcher_type = player.get_pitcher_type()
        player_designated_hitter = player.get_designated_hitter()
        player_is_hof = player.get_is_hof()

        player_model = {
            PYMONGO_PLAYER_ID: player_id,
            PYMONGO_PLAYER_NAME: player_name,
            PYMONGO_PLAYER_HANDEDNESS: player_handedness,
            PYMONGO_PLAYER_POSISTION: player_position,
            PYMONGO_PLAYER_PITCHER_TYPE: player_pitcher_type,
            PYMONGO_PLAYER_DESIGNATED_HITTER: player_designated_hitter,
            PYMONGO_PLAYER_IS_HOF: player_is_hof
        }

        player_collection = database.get_collection(PYMONGO_PLAYER_COLLECTION)
        found_player = player_collection.find_one({PYMONGO_PLAYER_ID: player_id})
        #we only need to insert the player if is not there
        if not found_player:
            player_collection.insert_one(player_model)

    @staticmethod
    def insert_players(players: list[Player], database: Database):
        for player in players:
            PymongoUtils.insert_player(player, database)

    @staticmethod
    def upsert_batting_stats(batting_stats_obj: BattingStats, player_id: str, season_id: str, database: Database):
        strike_outs = batting_stats_obj.get_strike_outs()
        at_bats = batting_stats_obj.get_at_bats()
        singles = batting_stats_obj.get_singles()
        doubles = batting_stats_obj.get_doubles()
        triples = batting_stats_obj.get_triples()
        home_runs = batting_stats_obj.get_home_runs()
        contact = batting_stats_obj.get_contact()
        sacrifice_flys = batting_stats_obj.get_sacrifice_flys()
        stolen_bases = batting_stats_obj.get_stolen_bases()
        walks = batting_stats_obj.get_walks()
        plate_apperances = batting_stats_obj.get_plate_apperances()
        num_games = batting_stats_obj.get_num_games()
        hits = batting_stats_obj.get_hits()
        rbis = batting_stats_obj.get_rbis()
        strikes = batting_stats_obj.get_strikes()
        balls = batting_stats_obj.get_balls()
        hit_by_pitch = batting_stats_obj.get_hit_by_pitch()
        runs = batting_stats_obj.get_runs()

        batting_stats_model = {
            PYMONGO_PLAYER: player_id,
            PYMONGO_SEASON: season_id,
            PYMONGO_STATS_STRIKE_OUTS: strike_outs,
            PYMONGO_STATS_AT_BATS: at_bats,
            PYMONGO_STATS_SINGLES: singles,
            PYMONGO_STATS_DOUBLES: doubles,
            PYMONGO_STATS_TRIPLES: triples,
            PYMONGO_STATS_HOME_RUNS: home_runs,
            PYMONGO_STATS_CONTACT: contact,
            PYMONGO_STATS_SACRIFICE_FLYS: sacrifice_flys,
            PYMONGO_STATS_STOLEN_BASES: stolen_bases,
            PYMONGO_STATS_WALKS: walks,
            PYMONGO_STATS_PLATE_APPERANCES: plate_apperances,
            PYMONGO_STATS_NUMBER_OF_GAMES: num_games,
            PYMONGO_STATS_HITS: hits,
            PYMONGO_STATS_RBIS: rbis,
            PYMONGO_STATS_STRIKES: strikes,
            PYMONGO_STATS_BALLS: balls,
            PYMONGO_STATS_HIT_BY_PITCH: hit_by_pitch,
            PYMONGO_STATS_RUNS: runs
        }

        batting_stats_collection = database.get_collection(PYMONGO_BATTING_STATS_COLLECTION)
        batting_stats_collection.update_one({PYMONGO_PLAYER: player_id, PYMONGO_SEASON: season_id}, {PYMONGO_SET: batting_stats_model}, upsert=True)

    @staticmethod
    def upsert_pitching_stats(pitching_stats_obj: PitchingStats, player_id: str, season_id: str, database: Database):
        strike_outs = pitching_stats_obj.get_strike_outs()
        at_bats = pitching_stats_obj.get_at_bats()
        innings_outs = pitching_stats_obj.get_innings_outs()
        pitches = pitching_stats_obj.get_pitches()
        walks = pitching_stats_obj.get_walks()
        home_runs = pitching_stats_obj.get_home_runs()
        num_games = pitching_stats_obj.get_num_games()
        strikes = pitching_stats_obj.get_strikes()
        earned_runs = pitching_stats_obj.get_earned_runs()
        hits = pitching_stats_obj.get_hits()
        balls = pitching_stats_obj.get_balls()
        runs = pitching_stats_obj.get_runs()

        pitching_stats_model = {
            PYMONGO_STATS_STRIKE_OUTS: strike_outs,
            PYMONGO_STATS_AT_BATS: at_bats,
            PYMONGO_STATS_INNINGS_OUTS: innings_outs,
            PYMONGO_STATS_PITCHES: pitches,
            PYMONGO_STATS_WALKS: walks,
            PYMONGO_STATS_HOME_RUNS: home_runs,
            PYMONGO_STATS_NUMBER_OF_GAMES: num_games,
            PYMONGO_STATS_STRIKES: strikes,
            PYMONGO_STATS_EARNED_RUNS: earned_runs,
            PYMONGO_STATS_HITS: hits,
            PYMONGO_STATS_BALLS: balls,
            PYMONGO_STATS_RUNS: runs
        }

        pitching_stats_collection = database.get_collection(PYMONGO_PITCHING_STATS_COLLECTION)
        pitching_stats_collection.update_one({PYMONGO_PLAYER: player_id, PYMONGO_SEASON: season_id}, {PYMONGO_SET: pitching_stats_model}, upsert=True)

    @staticmethod
    def upsert_player_stats(player: Player, season_id: str, database: Database):
        player_id = player.get_id()
        season_batting = player.get_season_batting()
        season_pitching = player.get_season_pitching()
        team_batting = player.get_team_batting()
        team_pitching = player.get_team_pitching()

        PymongoUtils.upsert_batting_stats(season_batting, player_id, season_id, database)
        PymongoUtils.upsert_pitching_stats(season_pitching, player_id, season_id, database)
        PymongoUtils.upsert_batting_stats(team_batting, player_id, None, database)
        PymongoUtils.upsert_pitching_stats(team_pitching, player_id, None, database)

    @staticmethod
    def upsert_players_stats(players: list[Player], season_id: str, database: Database):
        for player in players:
            PymongoUtils.upsert_player_stats(player, season_id, database)

    @staticmethod
    def insert_season(season: Season, database: Database):
        year = season.get_year()
        playoffs = PymongoUtils.insert_playoffs(season.get_playoffs(), database)
        regular_season = PymongoUtils.insert_games(season.get_regular_season(), database)
        PymongoUtils.insert_teams(season.get_teams(), database)

        season_model = {
            PYMONGO_YEAR: year,
            PYMONGO_PLAYOFFS: playoffs,
            PYMONGO_REGULAR_SEASON: regular_season,
        }

        season_collection = database.get_collection(PYMONGO_SEASON_COLLECTION)
        season_id = season_collection.insert_one(season_model).inserted_id
        return str(season_id)

    @staticmethod
    def insert_teams(teams: list[Team], database: Database):
        for team in teams:
            PymongoUtils.insert_team(team, database)

    @staticmethod
    def insert_teams_records(teams: list[Team], season_id: str, database: Database):
        for team in teams:
            PymongoUtils.insert_teams_record(team, season_id, database)

    @staticmethod
    def insert_teams_players_season(teams: list[Team], season_id: str, database: Database):
        for team in teams: 
            PymongoUtils.insert_team_players_season(team, season_id, database)

    @staticmethod
    def insert_teams_players(teams: list[Team], database: Database):
        for team in teams:
            PymongoUtils.insert_players(team.get_players(), database)

    @staticmethod
    def upsert_teams_players_stats(teams: list[Team], season_id: str, database: Database):
        for team in teams: 
            PymongoUtils.upsert_players_stats(team.get_players(), season_id, database)