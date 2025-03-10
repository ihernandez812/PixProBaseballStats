from player import Player
from constants import *

class Awards:
    CY_YOUNG_MIN=2
    MVP_MIN=3
    MIN_GAMES=80
    CY_YOUNG='cy_young'
    MVP='mvp'
    BATTING_TITLE='batting_title'
    HOME_RUN_LEADER='home_run_leader'

    def __init__(self, cy_young: Player, mvp: Player, batting_title: Player, home_run_leader: Player) -> None:
        self.cy_young = cy_young
        self.mvp = mvp
        self.batting_title = batting_title
        self.home_run_leader = home_run_leader

    def get_cy_young(self) -> Player:
        return self.cy_young

    def set_cy_young(self, value: Player):
        self.cy_young = value

    def get_mvp(self) -> Player:
        return self.mvp

    def set_mvp(self, value: Player):
        self.mvp = value
    
    def set_batting_title(self, value: Player) -> None:
        self.batting_title = value

    def get_batting_title(self) -> Player:
        return self.batting_title
    
    def set_home_run_leader(self, value: Player) -> Player:
        self.home_run_leader = value

    def get_home_run_leader(self) -> None:
        return self.home_run_leader

    @DeprecationWarning
    def to_model(self) -> dict[str, str]:
        model = {}
        if self.cy_young and self.mvp:
            cy_young_id = self.cy_young.get_id()
            mvp_id = self.mvp.get_id()
            model =  {
                self.CY_YOUNG: cy_young_id,
                self.MVP: mvp_id
            }
        else:
            raise ValueError('Cy Young or MVP is None')

        return model
    
    def to_dict(self) -> dict[str,]:
        model = {}
        if self.cy_young and self.mvp:
            cy_young_id = self.cy_young.get_id()
            mvp_id = self.mvp.get_id()
            batting_title_id = self.batting_title.get_id()
            home_run_leader_id = self.home_run_leader.get_id()
            model =  {
                self.CY_YOUNG: cy_young_id,
                self.MVP: mvp_id,
                self.BATTING_TITLE: batting_title_id,
                self.HOME_RUN_LEADER: home_run_leader_id

            }
        else:
            raise ValueError('Cy Young or MVP is None')

        return model