
TEAM_SEASON='season'
TEAM_GAMES_PLAYED='gamesPlayed'
TEAM_GAMES_WON='gamesWon'
TEAM_IS_USER_TEAM='isUserTeam'
TEAM_PLAYERS='players'
TEAM_NAMES='names'
TEAM_NO_ID=-1

PLAYER_STATS='stats'
PLAYER_NAME='name'
PLAYER_ID='id'
PLAYER_HANDEDNESS='handed'
PLAYER_SEASON_BATTING='seasonBatting'
PLAYER_TEAM_BATTING='teamCareerBatting'
PLAYER_SEASON_PITCHING='seasonPitching'
PLAYER_TEAM_PITCHING='teamCareerPitching'
PLAYER_POSITION='fieldingPosition'
PLAYER_DESIGNATED_HITTER='designatedHitter'
PLAYER_PITCHING='pitching'
PLAYER_PITCHING_TYPE='pitcherType'

LEFT_HANDED=-1
RIGHT_HANDED=1

YEAR=2023
MAJOR_LEAGUE=0
LEAGUE_TYPE='l'
TEAM_ONE_ID='t0id'
TEAM_ONE_SCORE='t0score'
TEAM_TWO_ID='t1id'
TEAM_TWO_SCORE='t2score'
POST_SEASON_LEAGUES='postSeasonLeagues'
FIXTURES='fixtures'
WINNER_ID='winner'
WORLD_SERIES='final'
AL_CHAMPIONSHIP='confOneFinal'
NL_CHAMPIONSHIP='confTwoFinal'
AL_DIVISIONAL='confOneSemi{series}'
NL_DIVISONAL='confTwoSemi{series}'
AL_WILDCARD='confOneWildcard'
NL_WILDCARD='confTwoWildcard'
SERIES_LENGTH='seriesLength'
PLAYOFFS_TEAM_ONE_ID='team0id'
PLAYOFFS_TEAM_TWO_ID='team1id'
PLAYOFFS_TEAM_ONE_SCORE='score0'
PLAYOFFS_TEAM_TWO_SCORE='score1'
CY_YOUNG_MIN=2
MVP_MIN=3
BATTING_HOF_MIN=9
PITCHING_HOF_MIN=5
MIN_GAMES=80


STRIKE_OUTS='strikeOuts'
AT_BATS='atBats'
SINGLES='base1'
DOUBLES='base2'
TRIPLES='base3'
HOME_RUNS='homeRuns'
CONTACT='contact'
SACRIFICE_FLYS='sacrifices'
STOLEN_BASES='stolen'
WALKS='walks'
PLATE_APPERANCES='plateApp'
NUMBER_OF_GAMES='numGames'
HITS='hits'
RBIS='runsBattedIn'
STRIKES='strikes'
BALLS='balls'
HIT_BY_PITCH='hitByPitch'
RUNS='runs'
GAMES_WON='gamesWon'
GAMES_PLAYED='gamesPlayed'

INNINGS_OUTS='inningsOuts'
PITCHES='pitches'
EARNED_RUNS='earnedRuns'

PITCHER=0
CATCHER=1
FIRST_BASE=2
SECOND_BASE=3
THIRD_BASE=4
SHORT_STOP=5
LEFT_FIELD=6
CENTER_FIELD=7
RIGHT_FIELD=8

NOT_PITCHER=-1
PITCHER_STATER=0
PTICHER_RELIEVER=1
PITCHER_CLOSER=2

PERIOD='.'
PLIST_FILE_EXT='.plist'
JSON_FILE_EXT='.json'
READ_FILE_BYTES='rb'
READ_FILE='r'
WRITE_FILE='w'
PLAIN_TXT_FILES_PATH='./app_data'

TEAM_NAMES_FILE='/UserTeamNames.json'
TEAM_FILE='/Team_{team_id}.json'
REGULAR_SEASON_DATA_FILE='/RegularSeasonData.json'
POST_SEASON_DATA_FILE='/PostSeasonData.json'
CY_YOUNG_STATS='./current_mlb_stats/cy_young_winner_stats.csv'
MVP_STATS='./current_mlb_stats/mvp_stats.csv'
BATTING_HOF_STATS='./current_mlb_stats/hof_batting.json'
PITCHING_HOF_STATS='./current_mlb_stats/hof_pitching.json'
PYMONGO_CONFIG='./config/password.json'

CSV_WAR='WAR'
CSV_NAME='Name'
CSV_WIN='W'
CSV_LOSS='L'
CSV_SAVES='SV'
CSV_ERA='ERA'
CSV_INNINGS_PITCHED='IP'
CSV_STRIKE_OUTS='SO'
CSV_BATTING_AVERAGE='BA'
CSV_OBP='OBP'
CSV_SLUG='SLG'
CSV_HOME_RUNS='HR'
CSV_RBIS='RBI'
CSV_STOLEN_BASES='SB'
CSV_YEARS_PLAYED='Y'
CSV_NUM_GAMES='G'
CSV_HITS='H'
CSV_RUNS='R'
CSV_WALKS='BB'
CSV_PLATE_APPERANCES='PA'
CSV_AT_BATS='AB'
CSV_DOUBLES='2B'
CSV_TRIPLES='3B'
CSV_SACRIFICE_FLYS='SF'
CSV_OPS='OPS'
EMPTY_STRING=''

PYMONGO_PASS='mongodb_password'
PYMONGO_URI='mongodb+srv://pix_pro_stats_user:{password}@cluster0.gbymskz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
PYMONGO_IP='localhost'
PYMONGO_PORT=27017
PYMONGO_SET='$set'
PYMONGO_DATABASE_NAME='pix_pro_stats'
PYMONGO_TEAM_NAME='name'
PYMONGO_TEAM_ID='id'
PYMONGO_TEAM_IS_USER_TEAM='is_user_team'
PYMONGO_PLAYER_ID='id'
PYMONGO_PLAYER_NAME='name'
PYMONGO_PLAYER_HANDEDNESS='handedness'
PYMONGO_PLAYER_POSISTION='posistion'
PYMONGO_PLAYER_PITCHER_TYPE='pitcher_type'
PYMONGO_PLAYER_DESIGNATED_HITTER='designated_hitter'
PYMONGO_PLAYER_IS_HOF='is_hof'
PYMONGO_STATS_STRIKE_OUTS='strike_outs'
PYMONGO_STATS_AT_BATS='at_bats'
PYMONGO_STATS_SINGLES='singles'
PYMONGO_STATS_DOUBLES='doubles'
PYMONGO_STATS_TRIPLES='triples'
PYMONGO_STATS_HOME_RUNS='home_runs'
PYMONGO_STATS_CONTACT='contact'
PYMONGO_STATS_SACRIFICE_FLYS='sacrifice_flys'
PYMONGO_STATS_STOLEN_BASES='stolen_bases'
PYMONGO_STATS_WALKS='walks'
PYMONGO_STATS_PLATE_APPERANCES='plate_apperances'
PYMONGO_STATS_NUMBER_OF_GAMES='num_games'
PYMONGO_STATS_HITS='hits'
PYMONGO_STATS_RBIS='rbis'
PYMONGO_STATS_STRIKES='strikes'
PYMONGO_STATS_BALLS='balls'
PYMONGO_STATS_HIT_BY_PITCH='hit_by_pitch'
PYMONGO_STATS_RUNS='runs'
PYMONGO_STATS_INNINGS_OUTS='innings_outs'
PYMONGO_STATS_PITCHES='pitches'
PYMONGO_STATS_EARNED_RUNS='earned_runs'
PYMONGO_YEAR='year'
PYMONGO_PLAYOFFS='playoffs'
PYMONGO_REGULAR_SEASON='regular_season'
PYMONGO_TEAM_ONE='team_one'
PYMONGO_TEAM_TWO='team_two'
PYMONGO_TEAM_ONE_SCORE='team_one_score'
PYMONGO_TEAM_TWO_SCORE='team_two_score'
PYMONGO_WINNER='winner'
PYMONGO_GAMES='games'
PYMONGO_SERIES_LENGTH='series_length'
PYMONGO_NL_WILDCARD='nl_wildcard'
PYMONGO_AL_WILDCARD='al_wildcard'
PYMONGO_NL_DIVISIONAL_ONE='nl_divisional_one'
PYMONGO_AL_DIVISIONAL_ONE='al_divisional_one'
PYMONGO_NL_DIVISIONAL_TWO='nl_divisional_two'
PYMONGO_AL_DIVISIONAL_TWO='al_divisional_two'
PYMONGO_NL_CHAMPIONSHIP='nl_championship'
PYMONGO_AL_CHAMPIONSHIP='al_championship'
PYMONGO_WORLD_SERIES='world_series'
PYMONGO_GAMES_WON='games_won'
PYMONGO_GAMES_PLAYED='games_played'
PYMONGO_CY_YOUNG='cy_young'
PYMONGO_MVP='mvp'
PYMONGO_TEAM='team'
PYMONGO_SEASON='season'
PYMONGO_RECORD='record'
PYMONGO_PLAYER='player'
PYMONGO_AWARDS='awards'

PYMONGO_GAME_COLLECTION='games'
PYMONGO_SERIES_COLLECTION='series'
PYMONGO_PLAYOFFS_COLLECTION='playoffs'
PYMONGO_RECORD_COLLECTION='records'
PYMONGO_TEAM_RECORD_COLLECTION='team_records'
PYMONGO_TEAM_SEASON_PLAYERS_COLLECTION='team_season_players'
PYMONGO_TEAM_COLLECTION='teams'
PYMONGO_PLAYER_COLLECTION='players'
PYMONGO_BATTING_STATS_COLLECTION='batting_stats'
PYMONGO_PITCHING_STATS_COLLECTION='pitching_stats'
PYMONGO_SEASON_COLLECTION='seasons'
PYMONGO_AWARDS_COLLECTION='awards'
PYMONGO_SEASON_AWARDS_COLLECTION='season_awards'
PYMONGO_HOF_CLASS_COLLECTION='hof_class'

