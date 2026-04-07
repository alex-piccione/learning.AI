from typing import Type
from annotated_types import T
from dacite import from_dict

def parse_json (json_string: str, data_class: Type[T])  -> T: 
    return from_dict(data_class, json_string)