import configparser
from pathlib import Path

from rptodo import DB_WRITE_ERROR,SUCCESS

DEF_DB_FILE_PATH=Path.home().joinpath(
    "."+Path.home().stem+"_todo.json"
)

def get_database_path(config_file:str)->Path:
    config_parser=config_parser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path:Path)->int:
    try:
        db_path.write_text("[]")
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR