from .Role import Role
import strings as s


class Vigilante(Role):
    icon = s.vigilante_icon
    team = 'Good'
    name = s.vigilante_name
    powerdesc = s.vigilante_power_description

    def __init__(self, player):
        super().__init__(player)
        self.target = None
        self.power_was_used = False

    def __repr__(self) -> str:
        if self.target is None:
            return "<Role: Ангел-хранитель>"
        else:
            return "<Role: Ангел-хранитель, защитил {target}>".format(target=self.target.tusername)

    def power(self, arg):
        selected = self.player.game.findplayerbyusername(arg)
        if self.power_was_used:
            self.player.message(s.error_no_uses)
            return
        if selected is None:
            self.player.message(s.error_username)
            return
        selected.protectedby = self.player
        self.target = selected
        self.player.message(s.vigilante_target_selected.format(target=self.target.tusername))

    def onendday(self):
        if self.target is not None:
            self.target.kill()
            self.player.game.message(s.vigilante_execution.format(target=self.target.tusername, icon=self.target.role.icon, role=self.target.role.name))
            self.power_was_used = True
            self.target = None
