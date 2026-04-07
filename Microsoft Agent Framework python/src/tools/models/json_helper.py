from typing import Type, Dict, Any
from annotated_types import T
from dacite import from_dict

def parse_json (data: Dict[str, Any], data_class: Type[T])  -> T: 
    return from_dict(data_class=data_class, data=data)
