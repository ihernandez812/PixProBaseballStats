import GeneralStats

class BattingStats(GeneralStats):

    def __init__(self,strike_outs, at_bats, singles, doubles, triples, home_runs, 
                contact, sacrifice_flys, stolen_bases, walkes, plate_apperances,
                num_games, hits, rbis, strikes, balls, hit_by_pitch, runs) -> None:
        GeneralStats.__init__(self, strike_outs, at_bats, walks, home_runs, strikes, hits, balls, runs)
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


   