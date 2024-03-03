from os import listdir, remove
from os.path import isfile, join
from pathlib import Path
from constants import *    
from file_utils import FileUtils
from stats_utils import StatsUtils
from team import Team
from player import Player
from record import Record
from pitching_stats import PitchingStats
from batting_stats import BattingStats
from game import Game
from series import Series
from season import Season
from playoffs import Playoffs
from awards import Awards
from mongodb_utils import Database
from pymongo_utils import PyMongoUtils

teams = {}

def create_game(game_obj: dict[str,]) -> Game:
    game = None
    league_type = game_obj.get(LEAGUE_TYPE,-1)
    if league_type == MAJOR_LEAGUE:
        team_one_id = game_obj.get(TEAM_ONE_ID)
        team_one = teams.get(team_one_id)
        team_two_id = game_obj.get(TEAM_TWO_ID)
        team_two = teams.get(team_two_id)
        team_one_score = game_obj.get(TEAM_ONE_SCORE, 0)
        team_two_score = game_obj.get(TEAM_TWO_SCORE, 0)
        game = Game(team_one, team_one_score, team_two, team_two_score)
    return game

#Post season json file has diffrent keys so we need a diffrent method
def create_post_season_game(post_season_game_obj: dict[str,]) -> Game:
    game = None
    team_one_id = post_season_game_obj.get(PLAYOFFS_TEAM_ONE_ID)
    team_one = teams.get(team_one_id)
    team_two_id = post_season_game_obj.get(PLAYOFFS_TEAM_TWO_ID)
    team_two = teams.get(team_two_id)
    team_one_score = post_season_game_obj.get(PLAYOFFS_TEAM_ONE_SCORE, 0)
    team_two_score = post_season_game_obj.get(PLAYOFFS_TEAM_TWO_SCORE, 0)
    game = Game(team_one, team_one_score, team_two, team_two_score)
    return game

def create_series(post_season_obj: dict, key: str, series_type: str=None) -> Series:
    if series_type is not None:
        key = key.format(series=series_type)
    series_obj = post_season_obj.get(key, {})
    series_length = series_obj.get(SERIES_LENGTH)
    winner_id = series_obj.get(WINNER_ID)
    team_one_id = series_obj.get(PLAYOFFS_TEAM_ONE_ID)
    team_two_id = series_obj.get(PLAYOFFS_TEAM_TWO_ID)
    team_one = teams.get(team_one_id)
    team_two = teams.get(team_two_id)
    games = series_obj.get(FIXTURES, [])
    series_games = []
    for game in games:
        new_game = create_post_season_game(game)
        series_games.append(new_game)
    
    series = Series(team_one, team_two, winner_id, series_games, series_length)
    return series

def check_is_mlb_post_season(post_season_obj: dict[str,]) -> bool:
    world_series = post_season_obj.get(WORLD_SERIES, {})
    team_one_id = world_series.get(PLAYOFFS_TEAM_ONE_ID, -1)
    return team_one_id in list(teams.keys())

def create_playoffs(post_season_obj: dict[str,]) -> Playoffs:
    is_major_leauge = check_is_mlb_post_season(post_season_obj)
    playoffs = None
    if is_major_leauge:
        al_wildcard = create_series(post_season_obj, AL_WILDCARD)
        nl_wildcard = create_series(post_season_obj, NL_WILDCARD)
        al_divisional_one = create_series(post_season_obj, AL_DIVISIONAL, 0)
        al_divisional_two = create_series(post_season_obj, AL_DIVISIONAL, 1)
        nl_divisonal_one = create_series(post_season_obj, NL_DIVISONAL, 0)
        nl_divisonal_two = create_series(post_season_obj, NL_DIVISONAL, 1)
        al_championship = create_series(post_season_obj, AL_CHAMPIONSHIP)
        nl_championship = create_series(post_season_obj, NL_CHAMPIONSHIP)
        world_series = create_series(post_season_obj, WORLD_SERIES)
        playoffs = Playoffs(al_wildcard, nl_wildcard, al_divisional_one, al_divisional_two, nl_divisonal_one, nl_divisonal_two,
                            al_championship, nl_championship, world_series)
    return playoffs


def create_post_season() -> Playoffs:
    post_season_path = PLAIN_TXT_FILES_PATH + POST_SEASON_DATA_FILE
    post_season_data = FileUtils.read_json_file(post_season_path)
    post_season_leagues = post_season_data.get(POST_SEASON_LEAGUES, [])
    post_season = None
    for post_season_league in post_season_leagues:
        post_season = create_playoffs(post_season_league)
        if post_season:
            break
    return post_season

def create_regular_season() -> list[Game]:
    regular_season_path = PLAIN_TXT_FILES_PATH + REGULAR_SEASON_DATA_FILE
    regular_season_data = FileUtils.read_json_file(regular_season_path)
    regular_season_games = regular_season_data.get(FIXTURES, [])
    games = []
    for regular_season_game in regular_season_games:
        new_game = create_game(regular_season_game)
        if new_game:
            games.append(new_game)
    return games

def create_record(season_obj: dict[str,], team: Team) -> None:
    games_won = season_obj.get(GAMES_WON, -1)
    games_played = season_obj.get(GAMES_PLAYED, -1)
    team_record = Record(games_won, games_played)
    team.set_record(team_record)

def create_pitching_stats(pitching_obj: dict[str,], curr_team: Team=None) -> PitchingStats:
    strike_outs = pitching_obj.get(STRIKE_OUTS, -1)
    at_bats = pitching_obj.get(AT_BATS, -1)
    innings_outs = pitching_obj.get(INNINGS_OUTS, -1)
    pitches = pitching_obj.get(PITCHES, -1)
    walks = pitching_obj.get(WALKS, -1)
    home_runs = pitching_obj.get(HOME_RUNS, -1)
    num_games = pitching_obj.get(NUMBER_OF_GAMES, -1)
    strikes = pitching_obj.get(STRIKES, -1)
    earned_runs = pitching_obj.get(EARNED_RUNS, -1)
    hits = pitching_obj.get(HITS, -1)
    balls = pitching_obj.get(BALLS, -1)
    runs = pitching_obj.get(RUNS, -1)
    team_id = -1
    if curr_team:
        team_id = curr_team.get_id()
    player_pitching_stats = PitchingStats(strike_outs, at_bats, innings_outs, pitches, walks, home_runs, num_games, strikes, earned_runs, hits, balls, runs, team_id)
    return player_pitching_stats

def create_batting_stats(batting_obj: dict[str,], curr_team: Team=None) -> BattingStats:
    strike_outs = batting_obj.get(STRIKE_OUTS, -1)
    at_bats = batting_obj.get(AT_BATS, -1)
    singles = batting_obj.get(SINGLES, -1)
    doubles = batting_obj.get(DOUBLES, -1)
    triples = batting_obj.get(TRIPLES, -1)
    home_runs = batting_obj.get(HOME_RUNS, -1)
    contact = batting_obj.get(CONTACT, -1)
    sacrifice_flys = batting_obj.get(SACRIFICE_FLYS, -1)
    stolen_bases = batting_obj.get(STOLEN_BASES, -1)
    walks = batting_obj.get(WALKS, -1)
    plate_apperances = batting_obj.get(PLATE_APPERANCES, -1)
    num_games = batting_obj.get(NUMBER_OF_GAMES, -1)
    hits = batting_obj.get(HITS, -1)
    rbis = batting_obj.get(RBIS, -1)
    strikes = batting_obj.get(STRIKES, -1)
    balls = batting_obj.get(BALLS, -1)
    hit_by_pitch = batting_obj.get(HIT_BY_PITCH, -1)
    runs = batting_obj.get(RUNS, -1) 
    team_id = -1
    if curr_team:
        team_id = curr_team.get_id()
    player_batting_stats = BattingStats(strike_outs, at_bats, singles, doubles, triples, home_runs, contact, sacrifice_flys, stolen_bases,
                                        walks, plate_apperances, num_games, hits, rbis, strikes, balls, hit_by_pitch, runs, team_id)

    return player_batting_stats

def get_pitcher_type(pitching_obj: dict[str,]) -> int:
    pitcher_type = pitching_obj.get(PLAYER_PITCHING_TYPE, 0)
    return pitcher_type

def create_player(player_obj: dict[str,], curr_team: Team) -> Player:
    player_id = player_obj.get(PLAYER_ID, -1)
    name = player_obj.get(PLAYER_NAME, 'J. Doe')
    handedness = player_obj.get(PLAYER_HANDEDNESS, 1)
    position = player_obj.get(PLAYER_POSITION, 0)
    pitching_obj = player_obj.get(PLAYER_PITCHING, {})
    pitcher_type = get_pitcher_type(pitching_obj)
    designated_hitter = player_obj.get(PLAYER_DESIGNATED_HITTER)
    stats_obj = player_obj.get(PLAYER_STATS, {})
    season_pitching_obj = stats_obj.get(PLAYER_SEASON_PITCHING, {})
    season_batting_obj = stats_obj.get(PLAYER_SEASON_BATTING, {})
    team_pitching_obj = stats_obj.get(PLAYER_TEAM_PITCHING, {})
    team_batting_obj = stats_obj.get(PLAYER_TEAM_BATTING, {})
    
    season_pitching = create_pitching_stats(season_pitching_obj)
    season_batting = create_batting_stats(season_batting_obj)
    team_pitching = create_pitching_stats(team_pitching_obj, curr_team)
    team_batting = create_batting_stats(team_batting_obj, curr_team)

    is_hof = False

    player = Player(player_id, name, handedness, position, pitcher_type, designated_hitter, season_batting, team_batting, season_pitching, team_pitching, is_hof)
    return player

def create_players(players_list: list[dict[str,]], team: Team) -> None:
    for player_obj in players_list:
        player = create_player(player_obj, team)
        team.add_player(player)

def fill_teams() -> None:
    for team_id, team in teams.items():
        team_file_path = PLAIN_TXT_FILES_PATH + TEAM_FILE.format(team_id=team_id)
        team_obj = FileUtils.read_json_file(team_file_path)
        players_list = team_obj.get(TEAM_PLAYERS, {})
        create_players(players_list, team)
        season_obj = team_obj.get(TEAM_SEASON, {})
        create_record(season_obj, team)
        is_user_team = team_obj.get(TEAM_IS_USER_TEAM, False)
        team.set_is_user_team(is_user_team)

def create_teams() -> None:
    team_names_path = PLAIN_TXT_FILES_PATH + TEAM_NAMES_FILE 
    team_names_map = FileUtils.read_json_file(team_names_path)
    team_id_name_map = team_names_map.get(TEAM_NAMES, {})
    for team_id_str, team_name in team_id_name_map.items():
        team_id = int(team_id_str)
        new_team = Team(team_id, team_name)
        teams[team_id] = new_team

def get_user_team(teams: list[Team]) -> Team:
    user_team = None
    for team in teams:
        if team.get_is_user_team():
            user_team = team
    return user_team

def create_awards(teams: list[Team]) -> Awards:
    cy_young_winner = None
    mvp_winner = None
    avg_cy_young_winner = StatsUtils.calculate_average_cy_young_stats(CY_YOUNG_STATS)
    avg_mvp_winner = StatsUtils.calculate_average_mvp_stats(MVP_STATS)
    user_team = get_user_team(teams)
    for player in user_team.get_players():
        if StatsUtils.is_cy_young_canidate(player, avg_cy_young_winner):
            cy_young_winner = StatsUtils.get_cy_young_winner(player, cy_young_winner)
        if StatsUtils.is_mvp_canidate(player, avg_mvp_winner):
            mvp_winner = StatsUtils.get_mvp_winner(player, mvp_winner)
    awards = Awards(cy_young_winner, mvp_winner)
    return awards

def create_hofs(teams: list[Team], database: Database) -> list[Player]:
    avg_batting_hof = StatsUtils.get_average_batting_hof_stats(BATTING_HOF_STATS)
    avg_pitching_hof = StatsUtils.get_average_pitching_hof_stats(PITCHING_HOF_STATS)
    hof_class = []
    user_team = get_user_team(teams)
    for player in user_team.get_players():
        is_hofer = False
        if player.get_position() == PITCHER:
            all_time_pitching_stats = PyMongoUtils.get_all_player_pitching(player.get_id(),  database)
            is_hofer = StatsUtils.is_pitching_hofer(all_time_pitching_stats, avg_pitching_hof)
        else:
            all_time_batting_stats = PyMongoUtils.get_all_player_batting(player.get_id(), database)
            is_hofer = StatsUtils.is_batting_hofer(all_time_batting_stats, avg_batting_hof)

        if is_hofer:
            hof_class.append(player)
    return hof_class

def convert_files() -> None:
    FileUtils.convert_files_to_plist()
    FileUtils.convert_files_to_json()

def create_season() -> Season:
    create_teams()
    fill_teams()
    regular_season_games = create_regular_season()
    post_season = create_post_season()
    awards = create_awards(teams.values())
    team_list = teams.values()
    season = Season(YEAR, team_list, regular_season_games, post_season, awards)
    return season

if __name__ == '__main__':
    season = create_season()
    database = Database(ip=PYMONGO_IP, port= PYMONGO_PORT)
    database.create_connection()
    database.ping_connection()
    database.set_database(PYMONGO_DATABASE_NAME)
    season_id = PyMongoUtils.insert_season(season, database)
    season_teams = season.get_teams()
    PyMongoUtils.insert_teams_records(season_teams, season_id, database)
    PyMongoUtils.insert_teams_players_season(season_teams, season_id, database)
    PyMongoUtils.insert_teams_players(season_teams, database)
    PyMongoUtils.upsert_teams_players_stats(season_teams, season_id, database)
    hofers = create_hofs(season_teams, database)
    PyMongoUtils.update_players_hof(hofers, database)
    database.close_connection()
    
