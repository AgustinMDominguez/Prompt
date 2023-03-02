


class Model:

    @property
    def as_str(self) -> str:
        return str(self)

    def __str__(self) -> str:
        raise NotImplemented("Abstract class Model does not implement str")


class Ada(Model):
    def __str__(self) -> str:
        return "ada"


class Davinci(Model):
    def __str__(self) -> str:
        return "text-davinci-003"


class ModelFinder:
    _strongest = Davinci()
    _cheapest = Ada()

    @classmethod
    def get_strongest(cls):
        return cls._strongest

    @classmethod
    def get_cheapest(cls):
        return cls._cheapest
