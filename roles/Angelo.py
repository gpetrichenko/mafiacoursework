from .Role import Role
import strings as s


class Angelo(Role):
    icon = s.angel_icon
    team = 'Good'
    name = s.angel_name
    powerdesc = s.angel_power_description

    def __init__(self, player):
        super().__init__(player)
        self.protecting = None

    def __repr__(self) -> str:
        if self.protecting is None:
            return "<Role: Ангел-хранитель>"
        else:
            return "<Role: Ангел-хранитель, защищает {target}>".format(target=self.protecting.tusername)

    def power(self, arg):
        selected = self.player.game.findplayerbyusername(arg)
        if selected is None:
            self.player.message(s.error_username)
            return

        if selected is not self.player:
            if self.protecting is not None:
                self.protecting.protectedby = None
            selected.protectedby = self.player
            self.protecting = selected
            self.player.message(s.angel_target_selected.format(target=self.protecting.tusername))
        else:
            self.player.message(s.error_no_selfpower)

    def onendday(self):
        if self.protecting is not None:
            self.protecting.protectedby = None
        self.protecting = None

    def ondeath(self):
        if self.protecting is not None:
            self.protecting.protectedby = None
        self.protecting = None