from abc import ABC, abstractmethod


class Band:
    """
    Parent class
    """

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


class Musician(ABC, Band):
    """
    Subclass of Band
    Abstract class
    """

    def __init__(self, name, instrument, solo):
        self.name = name
        self.instrument = instrument
        self.solo = solo

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def get_instrument(self):
        raise NotImplementedError

    @abstractmethod
    def set_instrument(self, instrument):
        raise NotImplementedError

    @abstractmethod
    def set_solo(self, solo):
        raise NotImplementedError

    @abstractmethod
    def play_solo(self):
        raise NotImplementedError

    @abstractmethod
    def some_method_that_must_be_implemented_in_base_class(self):
        raise NotImplementedError


class Guitarist(Musician):
    """
    Guitarist subclass of Musician and Band
    """

    def __init__(self, name, instrument="guitar", solo="face melting guitar solo"):
        super().__init__(name, instrument, solo)
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def set_instrument(self, instrument):
        self.solo = instrument

    def set_solo(self, solo):
        self.solo = solo

    def play_solo(self):
        return self.solo

    def some_method_that_must_be_implemented_in_base_class(self):
        pass


class Bassist(Musician):
    """
    Subclass of Musician and Band
    """

    def __init__(self, name, instrument="bass", solo="bom bom buh bom"):
        super().__init__(name, instrument, solo)

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def set_instrument(self, instrument):
        self.solo = instrument

    def set_solo(self, solo):
        self.solo = solo

    def play_solo(self):
        return self.solo

    def some_method_that_must_be_implemented_in_base_class(self):
        pass


class Drummer(Musician):
    """
    Subclass of Musician and Band
    """

    def __init__(self, name, instrument="drums", solo="rattle boom crash"):
        super().__init__(name, instrument, solo)

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def set_instrument(self, instrument):
        self.solo = instrument

    def set_solo(self, solo):
        self.solo = solo

    def play_solo(self):
        return self.solo

    def some_method_that_must_be_implemented_in_base_class(self):
        pass


class Keyboardist(Musician):
    """
    Subclass of Musician
    some_method_that_must_be_implemented_in_base_class() from Musician class is not implemented
    """

    def __init__(self, name, instrument="keyboard", solo="lah lah lah"):
        super().__init__(name, instrument, solo)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_instrument(self):
        pass

    def set_instrument(self, instrument):
        pass

    def set_solo(self, solo):
        pass

    def play_solo(self):
        pass


if __name__ == "__main__":
    jonas = Band("Jonas Brothers", [Drummer("Nick"), Guitarist("Joe"), Bassist("Kevin")])
    print(str(jonas))
    print(repr(jonas))
    print(jonas.play_solos())
