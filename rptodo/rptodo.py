from typing import Any,Dict,NamedTuple
from rptodo.database import DatabaseHandler
from pathlib import Path

class CurrentTodo(NamedTuple):
    todo:Dict[str,Any]
    error:int
    

class Todoer:
    def __init__(self,db_path:Path)->None:
        self._db_handler=DatabaseHandler(db_path)
