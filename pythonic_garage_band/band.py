from abc import ABC, abstractmethod


class Band:
    instances = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return Band.instances


class Musician(ABC, Band):
    def __init__(self, name):
        self.name = name

    @property
    def __str__(self):
        pass

    @property
    def __repr__(self):
        pass

    @abstractmethod
    def some_method_that_must_be_implemented_in_base_class(self):
        raise NotImplementedError


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"


class Keyboardist(Musician):
    pass


if __name__ == "__main__":
    help(Drummer)
