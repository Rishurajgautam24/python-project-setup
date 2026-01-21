from config.name_space import ConfigFactory
class AppManager:
    def __init__(self):
        self.cfg = ConfigFactory().initialize()

    def run(self):
        pass