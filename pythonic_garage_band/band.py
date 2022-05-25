class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        Band.instances.append(repr(self))

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        for member in self.members:
            return member.play_solo()

    @classmethod
    def to_list(cls):
        print("band", cls.instances)
        return Band.instances


class Musician(Band):
    def __init__(self, name):
        super().__init__(name)


class Guitarist(Band):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"



class Bassist(Band):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Band):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"


if __name__ == "__main__":
    pass