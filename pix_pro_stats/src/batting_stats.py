from general_stats import GeneralStats
from constants import *
class BattingStats(GeneralStats):

    def __init__(self,strike_outs, at_bats, singles, doubles, triples, home_runs, 
                contact, sacrifice_flys, stolen_bases, walks, plate_apperances,
                num_games, hits, rbis, strikes, balls, hit_by_pitch, runs, team_id) -> None:
        GeneralStats.__init__(self, strike_outs, at_bats, walks, home_runs, num_games, strikes, hits, balls, runs, team_id)
        self.singles = singles
        self.doubles = doubles
        self.triples = triples
        self.contact = contact
        self.sacrifice_flys = sacrifice_flys
        self.stolen_bases = stolen_bases
        self.plate_apperances = plate_apperances
        self.rbis = rbis
        self.hit_by_pitch = hit_by_pitch

    def get_singles(self):
        return self.singles

    def set_singles(self, value):
        self.singles = value

    def get_doubles(self):
        return self.doubles

    def set_doubles(self, value):
        self.doubles = value

    def get_triples(self):
        return self.triples

    def set_triples(self, value):
        self.triples = value

    def get_contact(self):
        return self.contact

    def set_contact(self, value):
        self.contact = value

    def get_sacrifice_flys(self):
        return self.sacrifice_flys

    def set_sacrifice_flys(self, value):
        self.sacrifice_flys = value

    def get_stolen_bases(self):
        return self.stolen_bases

    def set_stolen_bases(self, value):
        self.stolen_bases = value

    def get_plate_apperances(self):
        return self.plate_apperances

    def set_plate_apperances(self, value):
        self.plate_apperances = value

    def get_rbis(self):
        return self.rbis

    def set_rbis(self, value):
        self.rbis = value

    def get_hit_by_pitch(self):
        return self.hit_by_pitch

    def set_hit_by_pitch(self, value):
        self.hit_by_pitch = value

    def to_model(self, player_id, season_id):
        general_stats = super().to_model()
        batting_stats = {
            PYMONGO_PLAYER: player_id,
            PYMONGO_SEASON: season_id,
            PYMONGO_STATS_SINGLES: self.singles,
            PYMONGO_STATS_DOUBLES: self.doubles,
            PYMONGO_STATS_TRIPLES: self.triples,
            PYMONGO_STATS_CONTACT: self.contact,
            PYMONGO_STATS_SACRIFICE_FLYS: self.sacrifice_flys,
            PYMONGO_STATS_STOLEN_BASES: self.stolen_bases,
            PYMONGO_STATS_PLATE_APPERANCES: self.plate_apperances,
            PYMONGO_STATS_RBIS: self.rbis,
            PYMONGO_STATS_HIT_BY_PITCH: self.hit_by_pitch,
            
        }
        #combine the dictionarys
        batting_stats.update(general_stats)
        return batting_stats