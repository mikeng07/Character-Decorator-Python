import decorator

class Fighting(decorator.Decorator):
    """fighting ability for a character"""

    def abilities(self):
        """add the fighting ability to the character"""
        a_list = super().abilities()
        a_list[1] += 1
        return a_list

    def constitution(self):
        """adds the constitution for an fighter character"""
        return super().constitution() + 2

    def strength(self):
        """adds the strength for an fighter character"""
        return super().strength() + 2

    def wisdom(self):
        """subtracts the wisdom for an fighter character"""
        return super().wisdom() - 3