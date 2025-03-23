from os.path import exists
from constants import League, PitchingAttributes, BattingAttributes, BaseRunningAttributes, FieldingAttributes  
from file_utils import FileUtils
from stats_utils import StatsUtils
from team import Team
from player import Player, PlayerType
from record import Record
from pitching_stats import PitchingStats
from batting_stats import BattingStats
from game import Game
from series import Series
from season import Season
from playoffs import Playoffs
from awards import Awards
from division import Division
import json

teams = {}


def create_game(game_obj: dict[str,]) -> Game:
    game = None
    league_type = game_obj.get(League.LEAGUE_TYPE,-1)
    if league_type == League.MAJOR_LEAGUE:
        team_one_id = game_obj.get(Game.TEAM_ONE_ID)
        team_one = teams.get(team_one_id)
        team_two_id = game_obj.get(Game.TEAM_TWO_ID)
        team_two = teams.get(team_two_id)
        team_one_score = game_obj.get(Game.TEAM_ONE_SCORE, -1)
        team_two_score = game_obj.get(Game.TEAM_TWO_SCORE, -1)
        game = Game(team_one, team_one_score, team_two, team_two_score)
    return game

#Post season json file has diffrent keys so we need a diffrent method
def create_post_season_game(post_season_game_obj: dict[str,]) -> Game:
    game = None
    team_one_id = post_season_game_obj.get(Game.PLAYOFFS_TEAM_ONE_ID)
    team_one = teams.get(team_one_id)
    team_two_id = post_season_game_obj.get(Game.PLAYOFFS_TEAM_TWO_ID)
    team_two = teams.get(team_two_id)
    team_one_score = post_season_game_obj.get(Game.PLAYOFFS_TEAM_ONE_SCORE, 0)
    team_two_score = post_season_game_obj.get(Game.PLAYOFFS_TEAM_TWO_SCORE, 0)
    game = Game(team_one, team_one_score, team_two, team_two_score)
    return game

def create_series(post_season_obj: dict, key: str, series_type: str=None) -> Series:
    series_name = key
    if series_type is not None:
        key = key.format(series=series_type)
    series_obj = post_season_obj.get(key, {})
    series_length = series_obj.get(Series.LENGTH)
    winner_id = series_obj.get(Series.WINNER_ID)
    team_one_id = series_obj.get(Series.TEAM_ONE_ID)
    team_two_id = series_obj.get(Series.TEAM_TWO_ID)
    team_one = teams.get(team_one_id)
    team_two = teams.get(team_two_id)
    games = series_obj.get(League.FIXTURES, [])
    series_games = []
    for game in games:
        new_game = create_post_season_game(game)
        series_games.append(new_game)
    
    series = Series(team_one, team_two, winner_id, series_games, series_length, series_name)
    return series

def check_is_mlb_post_season(post_season_obj: dict[str,]) -> bool:
    world_series = post_season_obj.get(Playoffs.WORLD_SERIES, {})
    team_one_id = world_series.get(Series.TEAM_ONE_ID, -1)
    return team_one_id in list(teams.keys())

def create_playoffs(post_season_obj: dict[str,]) -> Playoffs:
    is_major_leauge = check_is_mlb_post_season(post_season_obj)
    playoffs = None
    if is_major_leauge:
        al_wildcard = create_series(post_season_obj, Playoffs.AL_WILDCARD)
        nl_wildcard = create_series(post_season_obj, Playoffs.NL_WILDCARD)
        al_divisional_one = create_series(post_season_obj, Playoffs.AL_DIVISIONAL, 0)
        al_divisional_two = create_series(post_season_obj, Playoffs.AL_DIVISIONAL, 1)
        nl_divisional_one = create_series(post_season_obj, Playoffs.NL_DIVISIONAL, 0)
        nl_divisional_two = create_series(post_season_obj, Playoffs.NL_DIVISIONAL, 1)
        al_championship = create_series(post_season_obj, Playoffs.AL_CHAMPIONSHIP)
        nl_championship = create_series(post_season_obj, Playoffs.NL_CHAMPIONSHIP)
        world_series = create_series(post_season_obj, Playoffs.WORLD_SERIES)
        playoffs = Playoffs(al_wildcard, nl_wildcard, al_divisional_one, nl_divisional_one, al_divisional_two, nl_divisional_two,
                            al_championship, nl_championship, world_series)
    return playoffs


def create_post_season() -> Playoffs:
    post_season_path = FileUtils.PLAIN_TXT_FILES_PATH + FileUtils.POST_SEASON_DATA_FILE
    post_season_data = FileUtils.read_json_file(post_season_path)
    post_season_leagues = post_season_data.get(Playoffs.POST_SEASON_LEAGUES, [])
    post_season = None
    for post_season_league in post_season_leagues:
        post_season = create_playoffs(post_season_league)
        if post_season:
            break
    return post_season

def create_regular_season() -> list[Game]:
    regular_season_path = FileUtils.PLAIN_TXT_FILES_PATH + FileUtils.REGULAR_SEASON_DATA_FILE
    regular_season_data = FileUtils.read_json_file(regular_season_path)
    regular_season_games = regular_season_data.get(League.FIXTURES, [])
    games = []
    for regular_season_game in regular_season_games:
        new_game = create_game(regular_season_game)
        if new_game:
            games.append(new_game)
    return games

def create_record(season_obj: dict[str,], team: Team) -> None:
    games_won = season_obj.get(Record.GAMES_WON, -1)
    games_played = season_obj.get(Record.GAMES_PLAYED, -1)
    team_record = Record(games_won, games_played)
    team.set_record(team_record)

def create_pitching_stats(pitching_obj: dict[str,], curr_team: Team=None) -> PitchingStats:
    strike_outs = pitching_obj.get(PitchingStats.STRIKE_OUTS, -1)
    at_bats = pitching_obj.get(PitchingStats.AT_BATS, -1)
    innings_outs = pitching_obj.get(PitchingStats.INNINGS_OUTS, -1)
    pitches = pitching_obj.get(PitchingStats.PITCHES, -1)
    walks = pitching_obj.get(PitchingStats.WALKS, -1)
    home_runs = pitching_obj.get(PitchingStats.HOME_RUNS, -1)
    num_games = pitching_obj.get(PitchingStats.NUMBER_OF_GAMES, -1)
    strikes = pitching_obj.get(PitchingStats.STRIKES, -1)
    earned_runs = pitching_obj.get(PitchingStats.EARNED_RUNS, -1)
    hits = pitching_obj.get(PitchingStats.HITS, -1)
    balls = pitching_obj.get(PitchingStats.BALLS, -1)
    runs = pitching_obj.get(PitchingStats.RUNS, -1)
    team_id = -1
    if curr_team:
        team_id = curr_team.get_id()
    player_pitching_stats = PitchingStats(strike_outs, at_bats, innings_outs, pitches, walks, home_runs, num_games, strikes, earned_runs, hits, balls, runs, team_id)
    return player_pitching_stats

def create_batting_stats(batting_obj: dict[str,], curr_team: Team=None) -> BattingStats:
    strike_outs = batting_obj.get(BattingStats.STRIKE_OUTS, -1)
    at_bats = batting_obj.get(BattingStats.AT_BATS, -1)
    singles = batting_obj.get(BattingStats.SINGLES, -1)
    doubles = batting_obj.get(BattingStats.DOUBLES, -1)
    triples = batting_obj.get(BattingStats.TRIPLES, -1)
    home_runs = batting_obj.get(BattingStats.HOME_RUNS, -1)
    contact = batting_obj.get(BattingStats.CONTACT, -1)
    sacrifice_flys = batting_obj.get(BattingStats.SACRIFICE_FLYS, -1)
    stolen_bases = batting_obj.get(BattingStats.STOLEN_BASES, -1)
    walks = batting_obj.get(BattingStats.WALKS, -1)
    plate_apperances = batting_obj.get(BattingStats.PLATE_APPERANCES, -1)
    num_games = batting_obj.get(BattingStats.NUMBER_OF_GAMES, -1)
    hits = batting_obj.get(BattingStats.HITS, -1)
    rbis = batting_obj.get(BattingStats.RBIS, -1)
    strikes = batting_obj.get(BattingStats.STRIKES, -1)
    balls = batting_obj.get(BattingStats.BALLS, -1)
    hit_by_pitch = batting_obj.get(BattingStats.HIT_BY_PITCH, -1)
    runs = batting_obj.get(BattingStats.RUNS, -1) 
    team_id = -1
    if curr_team:
        team_id = curr_team.get_id()
    player_batting_stats = BattingStats(strike_outs, at_bats, singles, doubles, triples, home_runs, contact, sacrifice_flys, stolen_bases,
                                        walks, plate_apperances, num_games, hits, rbis, strikes, balls, hit_by_pitch, runs, team_id)

    return player_batting_stats

def add_player_attributes(attributes: dict, keys: list[str]) -> float:
    total = 0
    for key in keys:
        attribute = attributes.get(key, 0)
        #From what I've seen the app takes the long decimal 
        #rounds it to the nearest thousandths and gets the average
        #from there
        total += round(attribute, 3)
    return total

def create_player_overall(player_obj: dict[str,], position: int) -> float:
    battingAttrs = player_obj.get(BattingAttributes.KEY, {})
    pitchingAttrs = player_obj.get(PitchingAttributes.KEY, {})
    baseRunningAttrs = player_obj.get(BaseRunningAttributes.KEY, {})
    fieldingAttrs = player_obj.get(FieldingAttributes.KEY)
    total = 0
    total += add_player_attributes(battingAttrs, BattingAttributes.ALL)
    total += add_player_attributes(baseRunningAttrs, BaseRunningAttributes.ALL)
    total += add_player_attributes(fieldingAttrs, FieldingAttributes.ALL)
    num_attributes = FieldingAttributes.NUM_ATTRIBUTES + BattingAttributes.NUM_ATTRIBUTES + BaseRunningAttributes.NUM_ATTRIBUTES
    #Not entirely sure how the app does pitcher overall
    #From what I can see it is everything including energy and base energy
    #divided by one less than the total number of attributes. Odd but that
    #is the only math that makes sense to me
    #so instead of doing the overall of them at that time add base energy twice
    #as if they were at full strength
    if position == PlayerType.PITCHER.value:
        total += add_player_attributes(pitchingAttrs, PitchingAttributes.ALL)
        num_attributes += PitchingAttributes.NUM_ATTRIBUTES
    
    overall = total / num_attributes
    overall = overall * 100
    overall = round(overall, 1)
    return overall
    


def create_player(player_obj: dict[str,], curr_team: Team) -> Player:
    player_id = player_obj.get(Player.ID, -1)
    name = player_obj.get(Player.NAME, 'N. Name')
    age = player_obj.get(Player.AGE, 0)
    handedness = player_obj.get(Player.HANDEDNESS, 1)
    position = player_obj.get(Player.POSITION, 0)
    pitching_obj = player_obj.get(Player.PITCHING, {})
    pitcher_type = pitching_obj.get(Player.PITCHING_TYPE, -1)
    pitch_types = pitching_obj.get(Player.PITCH_TYPES, [])
    designated_hitter = player_obj.get(Player.DESIGNATED_HITTER)
    stats_obj = player_obj.get(Player.STATS, {})
    season_pitching_obj = stats_obj.get(Player.SEASON_PITCHING, {})
    season_batting_obj = stats_obj.get(Player.SEASON_BATTING, {})
    
    
    season_pitching = create_pitching_stats(season_pitching_obj, curr_team)
    season_batting = create_batting_stats(season_batting_obj, curr_team)
    
    overall = create_player_overall(player_obj, position)
    is_hof = False


    player = Player(player_id, name, age, overall, handedness, position, pitcher_type, pitch_types, designated_hitter, season_batting, season_pitching, is_hof)
    return player

def create_players(players_list: list[dict[str,]], team: Team) -> None:
    for player_obj in players_list:
        player = create_player(player_obj, team)
        team.add_player(player)

def fill_teams() -> None:
    for team_id, team in teams.items():
        team_file_path = FileUtils.PLAIN_TXT_FILES_PATH + FileUtils.TEAM_FILE.format(team_id=team_id)
        team_obj = FileUtils.read_json_file(team_file_path)
        players_list = team_obj.get(Team.PLAYERS, {})
        create_players(players_list, team)
        season_obj = team_obj.get(Team.SEASON, {})
        create_record(season_obj, team)
        is_user_team = team_obj.get(Team.IS_USER_TEAM, False)
        team.set_is_user_team(is_user_team)

def create_teams() -> None:
    team_names_path = FileUtils.PLAIN_TXT_FILES_PATH + FileUtils.TEAM_NAMES_FILE 
    team_names_map = FileUtils.read_json_file(team_names_path)
    team_id_name_map = team_names_map.get(Team.NAMES, {})
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
    batting_title = None
    home_run_leader = None
    avg_cy_young_winner = StatsUtils.calculate_average_cy_young_stats(FileUtils.CY_YOUNG_STATS)
    avg_mvp_winner = StatsUtils.calculate_average_mvp_stats(FileUtils.MVP_STATS)
    user_team = get_user_team(teams)
    for player in user_team.get_players():
        if StatsUtils.is_cy_young_canidate(player, avg_cy_young_winner):
            cy_young_winner = StatsUtils.get_cy_young_winner(player, cy_young_winner)
        if StatsUtils.is_mvp_canidate(player, avg_mvp_winner):
            mvp_winner = StatsUtils.get_mvp_winner(player, mvp_winner)
        if player.get_position() != PlayerType.PITCHER.value:
            if StatsUtils.is_min_batting_stats(player.get_season_batting()):
                batting_title = StatsUtils.get_batting_title_winner(player, batting_title)
            home_run_leader = StatsUtils.get_home_run_leader_winner(player, home_run_leader)
    awards = Awards(cy_young_winner, mvp_winner, batting_title, home_run_leader)
    return awards

def create_hofers(user_team_players: list[dict]) -> list[str]:
    avg_batting_hof = StatsUtils.get_average_batting_hof_stats(FileUtils.BATTING_HOF_STATS)
    avg_pitching_hof = StatsUtils.get_average_pitching_hof_stats(FileUtils.PITCHING_HOF_STATS)
    hof_class = []
    for player in user_team_players:
        is_hofer = False
        #if they are already a hofer don't add them again
        if not player[Player.IS_HOF]:
            if player[Player.POSITION] == PlayerType.PITCHER.value:
                all_time_pitching_stats = player[Player.PITCHING_STATS]
                is_hofer = StatsUtils.is_pitching_hofer(all_time_pitching_stats, avg_pitching_hof)
            else:
                all_time_batting_stats = player[Player.BATTING_STATS] 
                is_hofer = StatsUtils.is_batting_hofer(all_time_batting_stats, avg_batting_hof)

        if is_hofer:
            hof_class.append(player[Player.ID])
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
    season = Season(League.YEAR, team_list, regular_season_games, post_season, awards)
    return season

def get_index_by_id(object_list, id, key) -> int:
    #if we don't find the index then the next slot is the idx
    idx = -1
    for i in range(len(object_list)):
        obj = object_list[i]
        if obj[key] == id:
            idx = i
    return idx

def get_team_index(team_list: list, team_id: int) -> int:
    return get_index_by_id(team_list, team_id, Team.ID)
    
def get_player_index(player_list: list, player_id: str) -> int:
    return get_index_by_id(player_list, player_id, Player.ID)


def check_for_new_year(current_league_data: dict):
    is_new_year = True
    seasons = current_league_data.get(League.SEASONS, [])
    for season in seasons:
        if season[Season.YEAR] == League.YEAR:
            is_new_year = False

    return is_new_year

def create_divisions() -> list[Division]:
    divisions_file_path = FileUtils.PLAIN_TXT_FILES_PATH + FileUtils.DIVISIONS_DATA_FILE
    divisions_data = FileUtils.read_json_file(divisions_file_path)
    leagues_data = divisions_data[League.LEAGUES]
    division_list = []
    for league_data in leagues_data:
        if league_data[League.NAME] == League.MAJOR_LEAGUE_NAME:
            conferences = league_data[League.CONFERENCES]
            for conference in conferences:
                conference_name = conference[League.NAME]
                divisions = conference[League.DIVISIONS]
                for division_data in divisions:
                    division_name = division_data[League.DIVISIONS_NAME]
                    teams = division_data[League.DIVISIONS_TEAMS]
                    division = Division(division_name, teams, conference_name)
                    division_list.append(division)
    return division_list



if __name__ == '__main__':
    debug = True
    #convert_files()
    #(82.4+80+9+88.7+77.5+79.6+68.8+91.4+95.9+86.8+96.6+78+77.7+61+6+89.7+87+9+70.3+97.5+78.1)/17
    current_league_data = {}
    if(exists(FileUtils.LEAGUE_JSON_PATH)):
        current_league_data = FileUtils.read_json_file(FileUtils.LEAGUE_JSON_PATH)
    is_new_year = check_for_new_year(current_league_data)
    if is_new_year and debug:
        season = create_season()
        season_teams = season.get_teams()

        team_list = current_league_data.get(League.TEAMS, [])
        player_list = current_league_data.get(League.PLAYERS, [])
        seasons = current_league_data.get(League.SEASONS, [])
        hofers = current_league_data.get(League.ALL_TIME_HOF, [])
        current_seasons = current_league_data.get(League.SEASONS, [])
        season_team_to_record = {}
        season_team_to_players = {}
        user_team_players = []
        for team in season_teams:
            #JSON changes it to a string so we need to 
            #So we can update it if the team name changes
            team_id_str = str(team.get_id())
            team_idx = get_team_index(team_list, team.get_id())
            if team_idx != -1:
                team_list[team_idx] = team.to_dict()
            else:
                team_list.append(team.to_dict())
            player_ids = []
            for player in team.get_players():
                player_id = player.get_id()
                player_idx = get_player_index(player_list, player.get_id())
                updated_player = {}
                if(player_idx != -1):
                    current_player_data = player_list[player_idx]
                    current_player_batting = current_player_data.get(Player.BATTING_STATS, [])
                    current_player_pitching = current_player_data.get(Player.PITCHING_STATS, [])
                    current_player_overall = current_player_data.get(Player.OVERALLS, [])
                    current_player_age = current_league_data.get(Player.AGE, 0)
                    updated_player = player.to_dict(season.get_year(), current_player_pitching, current_player_batting, current_player_age, current_player_overall)
                    player_list[player_idx] = updated_player
                else:
                    updated_player = player.to_dict(season.get_year())
                    player_list.append(updated_player)
                
                player_ids.append(player.get_id())
                if team.get_is_user_team():
                    user_team_players.append(updated_player)
            season_team_to_players[team_id_str] = player_ids
            season_team_to_record[team_id_str] = team.get_record().to_dict()
        divisions = create_divisions()
        hof_class = create_hofers(user_team_players)
        season.set_hof_class(hof_class)
        season_dict = season.to_dict()
        hofers.extend(hof_class)
        season_dict[Season.TEAM_PLAYERS] = season_team_to_players
        season_dict[Season.TEAM_RECORD] = season_team_to_record
        current_seasons.append(season_dict)

        leauge_dict = {
            League.DIVISIONS: [division.to_dict() for division in divisions],
            League.TEAMS: team_list,
            League.PLAYERS: player_list,
            League.SEASONS: current_seasons,
            League.ALL_TIME_HOF: hofers,
            

        }
        with open(FileUtils.LEAGUE_JSON_PATH, 'w') as f:
            f.write(json.dumps(leauge_dict))
    else:
        print("No new year skipping import")
    print('done')
    
