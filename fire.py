import decorator

class Fire(decorator.Decorator):
    """Fire ability for a character"""

    def abilities(self):
        """add the Fire ability to the character"""
        a_list = super().abilities()
        a_list[2] += 1
        return a_list

    def constitution(self):
        """substracts the constitution for an Fire character"""
        return super().constitution() - 3

    def strength(self):
        """substracts the strength for an Fire character"""
        return super().strength() - 1

    def wisdom(self):
        """adds the wisdom for an Fire character"""
        return super().wisdom() + 5