from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from harmony_hub.chords import chord as _chord
from harmony_hub.harmonic_field import harmonic_field as _harmonic_field
from harmony_hub.scales import scale as _scale

console = Console()
app = Typer()


@app.command()
def scale(
    tonic: str = Argument('c', help='Tonic of the scale'),
    mode: str = Argument('major', help='Scale character'),
):
    table = Table()
    notes, degrees = _scale(tonic, mode).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)

    console.print(table)


@app.command()
def chord(
    cipher: str = Argument('C', help='Chord notation'),
):
    table = Table()

    notes, degrees = _chord(cipher).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*notes)

    console.print(table)


@app.command()
def harmonic_field(
    root: str = Argument('c', help='Root of the harmonic field'),
    mode: str = Argument('major', help='Mode of the harmonic field'),
):
    table = Table()

    chords, degrees = _harmonic_field(root, mode).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*chords)

    console.print(table)
