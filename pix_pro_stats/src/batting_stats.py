from general_stats import GeneralStats
from constants import *


class BattingStats(GeneralStats):
    SINGLES='base1'
    DOUBLES='base2'
    TRIPLES='base3'
    CONTACT='contact'
    SACRIFICE_FLYS='sacrifices'
    STOLEN_BASES='stolen'
    PLATE_APPERANCES='plateApp'
    RBIS='runsBattedIn'
    HIT_BY_PITCH='hitByPitch'
    def __init__(self,strike_outs: int=None, at_bats: int=None, singles: int=None, doubles: int=None, triples: int=None, home_runs: int=None, 
                contact: int=None, sacrifice_flys: int=None, stolen_bases: int=None, walks: int=None, plate_apperances: int=None,
                num_games: int=None, hits: int=None, rbis: int=None, strikes: int=None, balls: int=None, hit_by_pitch: int=None,
                runs: int=None, team_id: int=None) -> None:
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

    def get_singles(self) -> int:
        return self.singles

    def set_singles(self, value: int):
        self.singles = value

    def get_doubles(self) -> int:
        return self.doubles

    def set_doubles(self, value: int):
        self.doubles = value

    def get_triples(self) -> int:
        return self.triples

    def set_triples(self, value: int):
        self.triples = value

    def get_contact(self) -> int:
        return self.contact

    def set_contact(self, value: int):
        self.contact = value

    def get_sacrifice_flys(self) -> int:
        return self.sacrifice_flys

    def set_sacrifice_flys(self, value: int):
        self.sacrifice_flys = value

    def get_stolen_bases(self) -> int:
        return self.stolen_bases

    def set_stolen_bases(self, value: int):
        self.stolen_bases = value

    def get_plate_apperances(self) -> int:
        return self.plate_apperances

    def set_plate_apperances(self, value: int):
        self.plate_apperances = value

    def get_rbis(self) -> int:
        return self.rbis

    def set_rbis(self, value: int):
        self.rbis = value

    def get_hit_by_pitch(self) -> int:
        return self.hit_by_pitch

    def set_hit_by_pitch(self, value: int):
        self.hit_by_pitch = value

    @DeprecationWarning
    def to_model(self, player_id: str, season_id: str) -> dict[str,]:
        general_stats = super().to_model()
        batting_stats = {
            League.PLAYER: player_id,
            League.SEASON: season_id,
            self.SINGLES: self.singles,
            self.DOUBLES: self.doubles,
            self.TRIPLES: self.triples,
            self.CONTACT: self.contact,
            self.SACRIFICE_FLYS: self.sacrifice_flys,
            self.STOLEN_BASES: self.stolen_bases,
            self.PLATE_APPERANCES: self.plate_apperances,
            self.RBIS: self.rbis,
            self.HIT_BY_PITCH: self.hit_by_pitch,
            
        }
        #combine the dictionarys
        batting_stats.update(general_stats)
        return batting_stats
    
    def to_dict(self, season_year: int) -> dict[str,]:
        general_stats = super().to_dict(season_year)
        batting_stats = {
            self.SINGLES: self.singles,
            self.DOUBLES: self.doubles,
            self.TRIPLES: self.triples,
            self.CONTACT: self.contact,
            self.SACRIFICE_FLYS: self.sacrifice_flys,
            self.STOLEN_BASES: self.stolen_bases,
            self.PLATE_APPERANCES: self.plate_apperances,
            self.RBIS: self.rbis,
            self.HIT_BY_PITCH: self.hit_by_pitch,
        }
        #combine the dictionarys
        batting_stats.update(general_stats)
        return batting_stats