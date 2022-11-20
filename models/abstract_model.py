from abc import ABCMeta


class Abstract_model(metaclass=ABCMeta):

    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)
