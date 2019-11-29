from .Role import Role
import strings as s
import random

class Mamma(Role):
    icon = s.mom_icon
    team = 'Good'
    name = s.mom_name
    powerdesc = s.mom_power_description

    def __repr__(self) -> str:
        return "<Role: Мама>"

    def onstartgame(self):
        possibletargets = self.player.game.players.copy()
        possibletargets.remove(self.player)
        target = random.sample(possibletargets, 1)[0]
        self.player.message(s.mom_discovery.format(target=target.tusername, icon=target.role.icon, role=target.role.name))

    def onendday(self):
        if random.randrange(0, 10) > 5:
            possibletargets = self.player.game.players.copy()
            possibletargets.remove(self.player)
            target = random.sample(possibletargets, 1)[0]
            self.player.message(
                s.mom_discovery.format(target=target.tusername, icon=target.role.icon, role=target.role.name))