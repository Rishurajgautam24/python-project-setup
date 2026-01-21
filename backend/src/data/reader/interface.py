from abc import ABC, abstractmethod

class IReader(ABC):
    def __init__(self, cfg):
        self.cfg = cfg

    @abstractmethod
    def read(self, path, **kwargs):
        pass