from .Role import Role
import strings as s


class Terrorista(Role):
    icon = s.terrorist_icon
    team = "Evil"
    name = s.terrorist_name
    powerdesc = s.terrorist_power_description

    def __repr__(self) -> str:
        return "<Role: Терорист>"

    def ondeath(self):
        if self.player == self.player.game.lastlynch:
            self.player.game.message(s.terrorist_kaboom)
            for selectedplayer in self.player.game.players:
                if selectedplayer.votingfor == self.player and selectedplayer.alive and selectedplayer is not self.player:
                    self.player.game.message(s.terrorist_target_killed.format(target=selectedplayer.tusername, icon=selectedplayer.role.icon, role=selectedplayer.role.name))
                    selectedplayer.kill()
