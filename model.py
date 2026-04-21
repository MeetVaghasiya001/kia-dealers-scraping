from pydantic import BaseModel
from typing import List,Dict,Optional

class Store(BaseModel):
    id : str
    store_name : str 
    url : Optional[str]
    full_address : str
    phone1 : Optional[str]
    phone2 : Optional[str]
    dealer_type : str


class City(BaseModel):
    city : str
    stores : List[Store]

class State(BaseModel):
    state_name : str 
    state_code : str 
    all_stores : List[City]