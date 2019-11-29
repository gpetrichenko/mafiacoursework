class Role:
    icon = "-"
    team = 'None'
    name = "UNDEFINED"
    powerdesc = None

    def __init__(self, player):
        self.player = player

    def __repr__(self) -> str:
        return "<undefined Role>"

    def __str__(self) -> str:
        return "{} {}".format(self.icon, self.name)

    def power(self, arg):
        pass

    def onendday(self):
        pass

    def ondeath(self):
        pass

    def onstartgame(self):
        pass