from .Role import Role
import strings as s
import random


class Disastro(Role):
    icon = s.detective_icon
    team = 'Good'
    name = s.detective_name
    powerdesc = s.detective_power_description

    def __init__(self, player):
        super().__init__(player)
        self.power_was_used = False

    def __repr__(self) -> str:
        return "<Role: Cледователь>"

    def power(self, arg):
        if self.power_was_used:
            self.player.message(s.error_no_uses)
            return
        target = self.player.game.findplayerbyusername(arg)
        if target is None:
            self.player.message(s.error_username)
            return
        self.power_was_used = True
        target_score = random.randrange(0, 25) + 1
        score = random.randrange(0, 100) + 1
        if score < target_score:
            role = target.role
        else:
            role = self.player.game.getrandomrole()
        self.player.message(s.detective_discovery.format(target_score=100-target_score, target=target.tusername, icon=role.icon, role=role.name))

    def onendday(self):
        self.power_was_used = False

    def ondeath(self):
        self.icon = s.disaster_icon
        self.name = s.disaster_name
