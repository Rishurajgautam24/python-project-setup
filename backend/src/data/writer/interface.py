from abc import ABC, abstractmethod

class IWriter(ABC):
    def __init__(self, cfg):
        self.cfg = cfg

    @abstractmethod
    def write(self, df, path, **kwargs):
        pass