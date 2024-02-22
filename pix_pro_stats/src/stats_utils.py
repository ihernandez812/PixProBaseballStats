from pitching_stats import PitchingStats
from general_stats import GeneralStats
from batting_stats import BattingStats
from player import Player
import pandas as pd
from constants import *

class StatsUtils:

    @staticmethod
    def calculate_average_cy_young_stats(cy_young_csv: str) -> dict:
        cy_young_all_time_stats = pd.read_csv(cy_young_csv, keep_default_na=False)
        cy_young_all_time_stats.fillna(EMPTY_STRING)
        row_count = 0
        era = 0 
        strike_outs_per_inning = 0
        for _, cy_young_stats in cy_young_all_time_stats.iterrows():
            if cy_young_stats[CSV_NAME] != EMPTY_STRING:
                era += float(cy_young_stats[CSV_ERA])
                innings_pitched = float(cy_young_stats[CSV_INNINGS_PITCHED])
                strike_outs = float(cy_young_stats[CSV_STRIKE_OUTS])
                strike_outs_per_inning += (strike_outs / innings_pitched)
                row_count+=1
        era /= row_count
        strike_outs_per_inning /= row_count
        return {
            CSV_ERA: round(era, 3), 
            CSV_STRIKE_OUTS: round(strike_outs_per_inning, 3)
        }
    

    @staticmethod
    def calculate_average_mvp_stats(mvp_csv: str) -> dict:
        mvp_all_time_stats = pd.read_csv(mvp_csv)
        mvp_all_time_stats.fillna(EMPTY_STRING)
        row_count = 0 
        batting_avg = 0
        obp = 0
        slug = 0
        home_runs = 0
        rbis = 0
        stolen_bases = 0
        for _, mvp_stats in mvp_all_time_stats.iterrows():
            if mvp_stats[CSV_BATTING_AVERAGE] != EMPTY_STRING:
                batting_avg += float(mvp_stats[CSV_BATTING_AVERAGE])
                obp += float(mvp_stats[CSV_OBP])
                slug += float(mvp_stats[CSV_SLUG])
                home_runs += float(mvp_stats[CSV_HOME_RUNS])
                rbis += float(mvp_stats[CSV_RBIS])
                stolen_bases += float(mvp_stats[CSV_STOLEN_BASES])
                row_count+=1
        batting_avg /= row_count
        obp /= row_count
        slug /= row_count
        home_runs /= row_count
        rbis /= row_count
        stolen_bases /= stolen_bases

        return {
            CSV_BATTING_AVERAGE: round(batting_avg, 3),
            CSV_OBP: round(obp, 3),
            CSV_SLUG: round(slug, 3),
            CSV_HOME_RUNS: round(home_runs, 3),
            CSV_RBIS: round(rbis, 3),
            CSV_STOLEN_BASES: round(stolen_bases, 3)
        }
    
    @staticmethod
    def calculate_cy_young_tie_breaker(player_one: Player, player_two: Player):
        player_one_points = 0
        player_two_points = 0
        player_one_pitching = player_one.get_season_pitching()
        player_two_pitching = player_two.get_season_pitching()

        player_one_era = StatsUtils.calculate_era(player_one_pitching)
        player_two_era = StatsUtils.calculate_era(player_two_pitching)
        player_one_strike_outs_per_inning = StatsUtils.calculate_strikes_outs_per_inning(player_one_pitching)
        player_two_strike_outs_per_inning = StatsUtils.calculate_strikes_outs_per_inning(player_two_pitching)
        player_one_whip = StatsUtils.calculate_whip(player_one_pitching)
        player_two_whip = StatsUtils.calculate_whip(player_two_pitching)

        if player_one_era != player_two_era:
            if player_one_era < player_two_era:
                player_one_points+=1
            else:
                player_two_points+=1
        if player_one_strike_outs_per_inning != player_two_strike_outs_per_inning:
            if player_one_strike_outs_per_inning > player_two_strike_outs_per_inning:
                player_one_points+=1
            else:
                player_two_points+=1
        if player_one_whip != player_two_whip:
            if player_one_whip < player_two_whip:
                player_one_points+=1
            else:
                player_two_points+=1
        winner = None
        if player_one_points > player_two_points:
            winner = player_one
        elif player_two_points > player_one_points:
            winner = player_two
        return winner
    

    @staticmethod
    def get_cy_young_winner(player: Player, curr_winner: Player, stats: dict):
        if curr_winner is None:
            curr_winner = player
        else:
            player_pitching = player.get_season_pitching()
            curr_winner_pitching = player.get_season_pitching()
            player_points = StatsUtils.calculate_cy_young_points(player_pitching, stats)
            curr_winner_points = StatsUtils.calculate_cy_young_points(curr_winner_pitching, stats)
            if player_points > curr_winner_points:
                curr_winner = player
            elif player_points == curr_winner_points:
                curr_winner = StatsUtils.calculate_cy_young_tie_breaker(player, curr_winner)
                if not curr_winner:
                    raise ValueError('Could not calculate a cy young winner possible tie')
        return curr_winner
    
    @staticmethod
    def calculate_cy_young_points(player_pitching: PitchingStats, stats: dict) -> int:
        points = 0
        era = StatsUtils.calculate_era(player_pitching)
        strikes_per_inning = StatsUtils.calculate_strikes_outs_per_inning(player_pitching)

        if era <= stats[CSV_ERA]:
            points += 1
        if strikes_per_inning >= stats[CSV_STRIKE_OUTS]:
            points += 1
        return points

    @staticmethod
    def is_cy_young_canidate(player: Player, stats: dict):
        is_canidate = False
        if player.get_position() == PITCHER:
            player_pitching = player.get_season_pitching()
            points = StatsUtils.calculate_cy_young_points(player_pitching, stats)
            print(points, player.get_name())
            if points >= CY_YOUNG_MIN:
                is_canidate = True
        return is_canidate

    @staticmethod
    def calculate_mvp_tie_breaker(player_one: Player, player_two: Player):
        player_one_points = 0
        player_two_points = 0
        player_one_batting = player_one.get_season_batting()
        player_two_batting = player_two.get_season_batting()

        player_one_avg = StatsUtils.calculate_average(player_one_batting)
        player_two_avg = StatsUtils.calculate_average(player_two_batting)
        player_one_obp = StatsUtils.calculate_obp(player_one_batting)
        player_two_obp = StatsUtils.calculate_obp(player_two_batting)
        player_one_slug = StatsUtils.calculate_slug(player_one_batting)
        player_two_slug = StatsUtils.calculate_slug(player_two_batting)
        player_one_home_runs = player_one_batting.get_home_runs()
        player_two_home_runs = player_two_batting.get_home_runs()
        player_one_rbis = player_one_batting.get_rbis()
        player_two_rbis = player_two_batting.get_rbis()
        player_one_stolen_bases = player_one_batting.get_stolen_bases()
        player_two_stolen_bases = player_two_batting.get_stolen_bases()
        
        if player_one_avg != player_two_avg:
            if player_one_avg > player_two_avg:
                player_one_points+=1
            else:
                player_two_points+=1
        if player_one_obp != player_two_obp:
            if player_one_obp > player_two_obp:
                player_one_points+=1
            else:
                player_two_points+=1
        if player_one_slug != player_two_slug:
            if player_one_slug > player_two_slug:
                player_one_points+=1
            else: 
                player_two_points+=1
        if player_one_home_runs != player_two_home_runs:
            if player_one_home_runs > player_two_home_runs:
                player_one_points+=1
            else:
                player_two_points+=1
        if player_one_rbis != player_two_rbis:
            if player_one_rbis > player_two_rbis:
                player_one_points+=1
            else:
                player_two_points+=1
        if player_one_stolen_bases != player_two_stolen_bases:
            if player_one_stolen_bases > player_two_stolen_bases:
                player_one_points+=1
            else:
                player_two_points+=1
        winner = None
        if player_one_points > player_two_points:
            winner = player_one
        elif player_two_points > player_one_points:
            winner = player_two

        return winner
    
    @staticmethod
    def get_mvp_winner(player: Player, curr_winner: Player, stats: dict):
        if curr_winner is None:
            curr_winner = player
        else:
            player_batting = player.get_season_batting()
            curr_winner_batting = player.get_season_batting()
            player_points = StatsUtils.calculate_mvp_points(player_batting, stats)
            curr_winner_points = StatsUtils.calculate_mvp_points(curr_winner_batting, stats)
            if player_points > curr_winner_points:
                curr_winner = player
            elif player_points == curr_winner_points:
                curr_winner = StatsUtils.calculate_mvp_tie_breaker(player, curr_winner)
                if not curr_winner:
                    raise ValueError('Could not calculate a mvp winner possible tie')
        return curr_winner
    
    @staticmethod
    def calculate_mvp_points(player_batting: BattingStats, stats: dict):
        points = 0
        batting_average = StatsUtils.calculate_average(player_batting)
        obp = StatsUtils.calculate_obp(player_batting)
        slug = StatsUtils.calculate_slug(player_batting)
        home_runs = player_batting.get_home_runs()
        rbis = player_batting.get_rbis()
        stolen_bases = player_batting.get_stolen_bases()

        if batting_average >= stats[CSV_BATTING_AVERAGE]:
            point+=1
        if obp >= stats[CSV_OBP]:
            points+=1
        if slug >= stats[CSV_SLUG]:
            points+=1
        if home_runs >= stats[CSV_HOME_RUNS] or abs(home_runs - stats[CSV_HOME_RUNS]) <= 10:
            points+=1
        if rbis >= stats[CSV_RBIS] or abs(rbis - stats[CSV_RBIS]) <= 25:
            points+=1
        if stolen_bases >= stats[CSV_STOLEN_BASES]:
            points+=1
        return points

    @staticmethod
    def is_mvp_canidate(player: Player, stats: dict):
        is_canidate = False
        if player.get_position() != PITCHER:
            player_batting = player.get_season_batting()
            points = StatsUtils.calculate_mvp_points(player_batting, stats)
            if points >= MVP_MIN:
                is_canidate = True
        return is_canidate

    @staticmethod
    def calculate_average(general_stats: GeneralStats) -> float:
        hits = general_stats.get_hits()
        at_bats = general_stats.get_at_bats()
        avg = -1
        if at_bats > 0:
            avg = hits / at_bats

        return round(avg, 3)

    @staticmethod
    def calculate_era(pitching_stats: PitchingStats) -> float:
        earned_runs = pitching_stats.get_earned_runs()
        innings_outs = pitching_stats.get_innings_outs()
        #total numbers of outs divided by 3 outs per inning is number of innings pitched
        innings_pitched = innings_outs / 3
        #should technically be 3 since each game is 3 innings but they use 9 I dunno why
        #could have a true era stat lates 
        era = (earned_runs/innings_pitched) * 9

        return round(era, 3)

    @staticmethod
    def calculate_strikes_outs_per_inning(pitching_stats: PitchingStats) -> float:
        strike_outs = pitching_stats.get_strike_outs()
        innings_outs = pitching_stats.get_innings_outs()
        #total numbers of outs divided by 3 outs per inning is number of innings pitched
        innings_pitched = innings_outs / 3

        strike_outs_per_inning = strike_outs / innings_pitched
        return round(strike_outs_per_inning, 3)

    @staticmethod
    def calculate_whip(pitching_stats: PitchingStats) -> float:
        hits = pitching_stats.get_hits()
        walks = pitching_stats.get_walks()
        innings_outs = pitching_stats.get_innings_outs()
        #total numbers of outs divided by 3 outs per inning is number of innings pitched
        innings_pitched = innings_outs / 3

        whip = (hits + walks) / innings_pitched

        return round(whip, 3)

    @staticmethod
    def calculate_obp(batting_stats: BattingStats) -> float:
        hits = batting_stats.get_hits()
        hits_by_pitch = batting_stats.get_hit_by_pitch()
        walks = batting_stats.get_walks()

        at_bats = batting_stats.get_at_bats()
        sacrifice_flys = batting_stats.get_sacrifice_flys()
        obp = -1
        if at_bats > 0:
            obp = (hits + hits_by_pitch + walks) / (at_bats + hits_by_pitch + walks + sacrifice_flys)

        return round(obp, 3)

    @staticmethod
    def calculate_slug(batting_stats: BattingStats) -> float:
        singles = batting_stats.get_singles()
        doubles = batting_stats.get_doubles()
        triples = batting_stats.get_triples()
        home_runs = batting_stats.get_home_runs()

        at_bats = batting_stats.get_at_bats()
        slg = -1
        if at_bats > 0:
            slg = (singles + (doubles * 2) + (triples * 3) + (home_runs * 4)) / at_bats

        return round(slg, 3)

    @staticmethod
    def calculate_ops(batting_stats: BattingStats) -> float:
        obp = StatsUtils.calculate_obp(batting_stats)
        slg = StatsUtils.calculate_slug(batting_stats)

        ops = obp + slg

        return ops