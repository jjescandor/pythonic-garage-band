from abc import ABC, abstractmethod


class Band:
    instances = []
    solos = []

    @classmethod
    def to_list(cls):
        return cls.instances

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        for member in self.members:
            print(member)
            Band.solos.append(member.play_solo())
        return Band.solos


class Musician(ABC):
    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def some_method_that_must_be_implemented_in_base_class(self):
        raise NotImplementedError

    @abstractmethod
    def get_instrument(self):
        raise NotImplementedError

    @abstractmethod
    def play_solo(self):
        raise NotImplementedError


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name, "guitar", "face melting guitar solo")
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name, "bass", "bom bom buh bom")

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def some_method_that_must_be_implemented_in_base_class(self):
        pass

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name, "drums", "rattle boom crash")

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo

    def some_method_that_must_be_implemented_in_base_class(self):
        pass


class Keyboardist(Musician):

    def __init__(self, name):
        super().__init__(name, "keyboard", "lah lah lah")

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_instrument(self):
        pass

    def play_solo(self):
        pass


if __name__ == "__main__":
    jonas = Band("Jonas Brothers", [Drummer("Nick"), Guitarist("Joe"), Bassist("Kevin")])
    print(str(jonas))
    print(repr(jonas))
    print(jonas.play_solos())
