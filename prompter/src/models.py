
class Model:

    @property
    def as_str(self) -> str:
        return str(self)

    def __str__(self) -> str:
        raise NotImplemented("Abstract class Model does not implement str")


class Ada(Model):
    def __str__(self) -> str:
        return "ada"


class ChatTurbo(Model):
    def __str__(self) -> str:
        return "gpt-3.5-turbo"


class Davinci(Model):
    def __str__(self) -> str:
        return "text-davinci-003"


class CodeDavinci(Model):
    def __str__(self) -> str:
        return "code-davinci-002"


class EditDavinci(Model):
    def __str__(self) -> str:
        return "text-davinci-edit-001"


class ModelFinder:
    _strongest = Davinci()
    _cheapest = Ada()
    _code = CodeDavinci()
    _edit = EditDavinci()
    _chat = ChatTurbo()

    @classmethod
    def get_chat_model(cls):
        return cls._chat

    @classmethod
    def get_strongest(cls):
        return cls._strongest

    @classmethod
    def get_edit_model(cls):
        return cls._edit

    @classmethod
    def get_cheapest(cls):
        return cls._cheapest

    @classmethod
    def get_best_for_code(cls):
        return cls._code
