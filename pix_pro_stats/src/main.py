from os import listdir, remove
from os.path import isfile, join
from pathlib import Path
from constants import *    
from file_utils import FileUtils
from team import Team
from player import Player
from record import Record
from pitching_stats import PitchingStats
from batting_stats import BattingStats

import json
from date_time_encoder import DateTimeEncoder

teams = {}

def create_record(season_obj, team):
    games_won = season_obj.get(GAMES_WON, -1)
    games_played = season_obj.get(GAMES_PLAYED, -1)
    team_record = Record(games_won, games_played)
    team.set_team_record(team_record)

def create_pitching_stats(pitching_obj):
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

    player_pitching_stats = PitchingStats(strike_outs, at_bats, innings_outs, pitches, walks, home_runs, num_games, strikes, earned_runs, hits, balls, runs)
    return player_pitching_stats

def create_batting_stats(batting_obj):
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

    player_batting_stats = BattingStats(strike_outs, at_bats, singles, doubles, triples, home_runs, contact, sacrifice_flys, stolen_bases,
                                        walks, plate_apperances, num_games, hits, rbis, strikes, balls, hit_by_pitch, runs)

    return player_batting_stats

def get_pitcher_type(pitching_obj):
    pitcher_type = pitching_obj.get(PLAYER_PITCHING_TYPE, 0)
    return pitcher_type

def create_player(player_obj):
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
    team_pitching = create_pitching_stats(team_pitching_obj)
    team_batting = create_batting_stats(team_batting_obj)

    is_hof = False

    player = Player(player_id, name, handedness, position, pitcher_type, designated_hitter, season_pitching, season_batting, team_pitching, team_batting, is_hof)
    return player

def create_players(players_list, team):
    for player_obj in players_list:
        player = create_player(player_obj)
        team.add_player(player)

def fill_teams():
    for team_id, team in teams.items():
        team_file_path = PLAIN_TXT_FILES_PATH + TEAM_FILE.format(team_id=team_id)
        team_obj = FileUtils.read_json_file(team_file_path)
        players_list = team_obj.get(TEAM_PLAYERS, {})
        create_players(players_list, team)
        season_obj = team_obj.get(TEAM_SEASON, {})
        create_record(season_obj, team)
        is_user_team = team_obj.get(TEAM_IS_USER_TEAM, False)
        team.set_is_user_team(is_user_team)

def create_teams():
    team_names_path = PLAIN_TXT_FILES_PATH + TEAM_NAMES_FILE 
    team_names_map = FileUtils.read_json_file(team_names_path)
    team_id_name_map = team_names_map.get(TEAM_NAMES, {})
    for team_id, team_name in team_id_name_map.items():
        new_team = Team(team_id, team_name)
        teams[team_id] = new_team

def convert_files():
    FileUtils.convert_files_to_plist()
    FileUtils.convert_files_to_json()

def create_season():
    create_teams()
    fill_teams()
    regular_season_games = create_regular_season()
    post_season = create_post_season()

if __name__ == '__main__':
    create_season()
    
