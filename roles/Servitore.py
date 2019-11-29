from .Role import Role
from .SignoreDelCaos import SignoreDelCaos
import strings as s


class Servitore(Role):
    icon = s.chaos_servant_icon
    team = 'Chaos'
    name = s.chaos_servant_name
    powerdesc = s.chaos_servant_power_description

    def __repr__(self) -> str:
        return "<Role: Слуга Хаоса>"

    def onendday(self):
        for chaoslord in self.player.game.playersinrole["SignoreDelCaos"]:
            if chaoslord.alive:
                break
        else:
            self.player.game.changerole(self.player, SignoreDelCaos)
            self.player.game.message(s.chaos_servant_inherited)
