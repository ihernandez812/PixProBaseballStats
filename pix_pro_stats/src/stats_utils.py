import PitchingStats
import GeneralStats
import BattingStats

class StatsUtils:

    @staticmethod
    def calculate_average(general_stats: GeneralStatsStats) -> float:
        hits = general_stats.get_hits()
        at_bats = general_stats.get_at_bats()
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
        era = (earnedRuns/innings_pitched) * 9

        return round(era, 3)

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

        obp = (hits + hits_by_pitch + walks) / (at_bats + hits_by_pitch + walks + sacrifice_flys)

        return round(obp, 3)

    @staticmethod
    def calculate_slug(batting_stats: BattingStats) -> float:
        singles = batting_stats.get_singles()
        doubles = batting_stats.get_doubles()
        triples = batting_stats.get_triples()
        home_runs = batting_stats.get_home_runs()

        at_bats = batting_stats.get_at_bats()

        slg = (singles + (doubles * 2) + (triples * 3) + (home_runs * 4)) / at_bats

        return round(slg, 3)

    @staticmethod
    def calculate_ops(batting_stats: BattingStats) -> float:
        obp = calculate_obp()
        slg = calculate_slug()

        ops = obp + slg

        return ops