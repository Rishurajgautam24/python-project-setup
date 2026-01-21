import pandas as pd
from backend.src.data.reader.interface import IReader

class CSVReader(IReader):
    def read(self, path: str, **kwargs) -> pd.DataFrame:
        df = pd.read_csv(path, **kwargs)