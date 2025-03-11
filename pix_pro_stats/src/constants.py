class League:
    MAJOR_LEAGUE_NAME='Major League'
    NAME='name'
    CONFERENCES='conferences'
    CONFERENCE='conference'
    LEAGUES='leagues'
    DIVISIONS='divisions'
    DIVISIONS_NAME='name'
    DIVISIONS_TEAMS='teamIdInts'
    YEAR=2023
    MAJOR_LEAGUE=0
    LEAGUE_TYPE='l'
    FIXTURES='fixtures'
    SEASONS='seasons'
    SEASON='season'
    ALL_TIME_HOF='hofers'
    TEAMS='teams'
    TEAM='team'
    PLAYERS='players'
    PLAYER='player'

class PitchingAttributes:
    KEY='pitching'
    ENGERGY='baseEnergy'
    SPEED='speed'
    INTELIGENCE='inteligence'
    STAMINA='stamina'
    ACCURACY='accuracy'
    MOVEMENT='movement'
    NUM_ATTRIBUTES=6
    ALL=[ENGERGY, SPEED, INTELIGENCE, STAMINA, ACCURACY, MOVEMENT]

class BattingAttributes:
    KEY='batting'
    SKILL='skill'
    POWER='power'
    REACTIONS='reactions'
    INTELIGENCE='inteligence'
    NUM_ATTRIBUTES=4
    ALL=[SKILL, POWER, REACTIONS, INTELIGENCE]

class FieldingAttributes:
    KEY='fielding'
    POWER='power'
    SPEED='speed'
    REACTIONS='reactions'
    ACCURACY='accuracy'
    CATCHING='catching'
    NUM_ATTRIBUTES=5
    ALL=[POWER, SPEED, REACTIONS, ACCURACY, CATCHING]

class BaseRunningAttributes:
    KEY='running'
    SPEED='speed'
    REACTIONS='reactions'
    NUM_ATTRIBUTES=2
    ALL=[SPEED, REACTIONS]

class HallOfFame:
    BATTING_HOF_MIN=9
    PITCHING_HOF_MIN=5

class BaseballReference:
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
