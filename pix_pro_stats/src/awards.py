from player import Player
from constants import *

class Awards:

    def __init__(self, cy_young: Player, mvp: Player) -> None:
        self.cy_young = cy_young
        self.mvp = mvp

    def get_cy_young(self) -> Player:
        return self.cy_young

    def set_cy_young(self, value: Player):
        self.cy_young = value

    def get_mvp(self) -> Player:
        return self.mvp

    def set_mvp(self, value: Player):
        self.mvp = value
    
    def to_model(self) -> dict[str, str]:
        model = {}
        if self.cy_young and self.mvp:
            cy_young_id = self.cy_young.get_id()
            mvp_id = self.mvp.get_id()
            model =  {
                PYMONGO_CY_YOUNG: cy_young_id,
                PYMONGO_MVP: mvp_id
            }
        else:
            raise ValueError('Cy Young or MVP is None')

        return model