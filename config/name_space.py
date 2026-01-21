from types import SimpleNamespace
import os
from dotenv import dotenv_values
from yaml import safe_load
from string import Template

class ConfigFactory:
    def __init__(self,yaml_path):
        self.yaml_path = yaml_path

    def dict_to_namespace(self,map_obj):
        if isinstance(map_obj,dict):
            return SimpleNamespace(**{key: self.dict_to_namespace(value) for key,value in map_obj.items()})
        else:
            return map_obj

    def initialize(self):
        with open(self.yaml_path,'r') as yaml_file:
            yaml_dict = safe_load(stream=yaml_file)

        col_dict = {}
        schema_dict = {}

        for sheet_name, schema_df in pd.read_excel(io=r'data/config/schema.xlsx', sheet_name=None, index_col='Variable').items():
            schema_dict['_'.join(word.upper() for word in sheet_name.split())] = schema_df      #NOTE: Table Name will be in this Casing "Table Name" like "Account Name"
            col_dict['_'.join(word.capitalize() for word in sheet_name.split())] = schema_df.loc[schema_df['IS Derived?'] | schema_df['Is Read?'], 'Name'].to_dict()

        ns_dict = {
            'Schema' : schema_dict,
            'Col' : col_dict,
            'Path': yaml_dict['Path'],
            'Secret': dotenv_values(dotenv_path = yaml_dict['Path']['ENV']),
            'Param': yaml_dict['Param'],
        }
        return self.dict_to_namespace(map_obj=ns_dict)

if __name__ == '__main__':
    import os
    os.chdir(path = '..')
    cfg = ConfigFactory()
    print('End')