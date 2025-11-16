from typing import Optional, List
import typer
from rptodo import __app_name__, __version__, ERRORS, config, database, rptodo
from pathlib import Path
app = typer.Typer()
@app.command()
def init(
    db_path:str=typer.Option(
        str(database.DEF_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="to-do database location?",
    ),
)->None:
    app_init_error=config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f'Creating config file with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    db_init_error = database.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f'Creating database failed with "{ERRORS[db_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The to-do database is {db_path}", fg=typer.colors.GREEN)


def get_todoer()->rptodo.Todoer:
    if config.CONFIG_FILE_PATH.exists():
        db_path=database.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "rptodo init"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    if db_path.exists():
        return rptodo.Todoer(db_path)
    else:
        typer.secho('Database not found. Please run "rptodo init"',
                    fg=typer.colors.RED)
        raise typer.Exit(1)


def _version_callback(value:bool)->None:
    if value:
        typer.echo(f" SHUBH ASHISH's {__app_name__} v{__version__}")
        raise typer.Exit()
    
@app.callback()
def main(version: Optional[bool]=typer.Option(
    None,
    "--version",
    "-v",
    help="Show the applications version and exit",
    callback=_version_callback,
    is_eager=True
)
)->None:
    return 