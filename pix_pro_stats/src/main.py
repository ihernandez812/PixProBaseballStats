from os import listdir, remove
from os.path import isfile, join
from pathlib import Path
from constants import *    
from file_utils import FileUtils

import json
from date_time_encoder import DateTimeEncoder

teams = {}

def create_pitching_stats(pitching_obj):
    #TODO create pitching stats object
    pass


def create_batting_obj(batting_obj):
    #TODO create batting stats obj
    pass 


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
    season_pitching_obj = stats_obj.get(PLAYER_SEASON_PITCHING)
    season_batting_obj = stats_obj.get(PLAYER_SEASON_BATTING)
    team_pitching_obj = stats_obj.get(PLAYER_TEAM_PTICHING)
    team_batting_obj = stats_obj.get(PLAYER_TEAM_BATTING)
    
    season_pitching = create_pitching_stats(season_pitching_obj)
    season_batting = create_batting_stats(season_batting_obj)
    team_pitching = create_pitching_stats(team_pitching_obj)
    team_batting = create_batting_stats(team_batting_obj)

    is_hof = False


def create_players(players_list, team):
    for player_obj in players_list:
        player = create_player(player)
        team.add_player(player)

def fill_teams():
    for team_id, team in teams.values():
        team_file_path = PLAIN_TXT_FILES_PATH + TEAM_FILE.format(team_id)
        team_obj = FileUtils.read_json_file(team_file_path)
        players_list = team_obj.get(PLAYERS, {})
        create_players(players_list, team)
        season_obj = team_obj.get(TEAM_SEASON, {})
        create_record(season_obj, team)
        is_user_team = team_obj.get(TEAM_IS_USER_TEAM, False)
        team.set_is_user_team(is_user_team)

def create_teams():
    team_names_path = PLAIN_TXT_FILES_PATH + TEAM_NAMES_FILE 
    team_names = FileUtils.read_json_file(team_names_path)
    for team_id, team_name in team_names.values():
        team = Team(team_id, team_name)
        teams[team_id] = team

def convert_files():
    FileUtils.convert_files_to_plist()
    FileUtils.convert_files_to_json()

if __name__ == '__main__':
    convert_files()
    
