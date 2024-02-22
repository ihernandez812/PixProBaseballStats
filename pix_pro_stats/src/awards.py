
class Awards:

    def __init__(self, cy_young, mvp) -> None:
        self.cy_young = cy_young
        self.mvp = mvp

    def get_cy_young(self):
        return self.cy_young

    def set_cy_young(self, value):
        self.cy_young = value

    def get_mvp(self):
        return self.mvp

    def set_mvp(self, value):
        self.mvp = value
