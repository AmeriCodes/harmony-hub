from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from harmony_hub.scales import scale

console = Console()
app = Typer()


@app.command()
def scales(
    tonic: str =Argument('c', help='Tonic of the scale'),
    mode: str =Argument('major', help='Scale character'),
):
    table = Table()
    notes, degrees = scale(tonic, mode).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)

    console.print(table)
