from .Role import Role
import strings as s


class Corrotto(Role):
    icon = s.corrupt_icon
    team = 'Evil'
    name = s.corrupt_name
    powerdesc = s.corrupt_power_description
    refillpoweruses = 1

    def __init__(self, player):
        super().__init__(player)
        self.poweruses = self.refillpoweruses

    def __repr__(self) -> str:
        return "<Role: Корупционер, {uses} использует слева>".format(uses=self.poweruses)

    def power(self, arg):
        if self.poweruses <= 0:
            self.player.message(s.error_no_uses)
            return
        target = self.player.game.findplayerbyusername(arg)
        if target is None:
            self.player.message(s.error_username)
            return
        self.poweruses -= 1
        self.player.message(s.detective_discovery.format(target_score=100, target=target.tusername, icon=target.role.icon, role=target.role.name))

    def onendday(self):
        self.poweruses = self.refillpoweruses
