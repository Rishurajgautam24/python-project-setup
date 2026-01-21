


class DataWriterFactory:
    def __init__(self, cfg):
        self.cfg = cfg

    def write(self, source, df, path, **kwargs):
        writers_dict = {

        }
        return writers_dict[source.lower()](cfg = self.cfg).write(df, path, **kwargs)