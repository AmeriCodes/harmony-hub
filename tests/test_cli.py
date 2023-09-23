from pytest import mark
from typer.testing import CliRunner

from harmony_hub.cli import app

runner = CliRunner()


def test_scale_cli_must_return_0_to_stdout():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_cli_scale_must_contain_the_notes_in_the_response(note):
    result = runner.invoke(app)
    assert note in result.stdout


@mark.parametrize('note', ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'])
def test_cli_scale_must_contain_the_notes_in_the_f_response_scale(note):
    result = runner.invoke(app, ['F'])
    assert note in result.stdout


@mark.parametrize('degree', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_cli_scale_must_contain_the_all_degrees(degree):
    result = runner.invoke(app, ['F'])
    assert degree in result.stdout
