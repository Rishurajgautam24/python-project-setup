from backend.src.data.reader.csv import CSVReader
from backend.src.data.reader.excel import ExcelReader


class DataReaderFactory:
    def __init__(self, cfg):
        self.cfg = cfg

    def read(self,source, path, **kwargs):
        reader_dict = {
            'csv': CSVReader,
            'excel': ExcelReader,
        }
        return reader_dict[source.lower()](cfg = self.cfg).read(path, **kwargs)