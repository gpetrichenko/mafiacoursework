from .Role import Role
import strings as s


class Royal(Role):
    icon = s.royal_icon
    team = 'Good'
    name = s.royal_name

    def __init__(self, player):
        super().__init__(player)

    def __repr__(self) -> str:
        return "<Role: Мирный житель>"
