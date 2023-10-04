from pytest import mark
from typer.testing import CliRunner

from harmony_hub.cli import app

runner = CliRunner()


def test_scale_cli_must_return_0_to_stdout():
    result = runner.invoke(app, ['scale'])
    assert result.exit_code == 0


@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_cli_scale_must_contain_the_notes_in_the_response(note):
    result = runner.invoke(app, ['scale'])
    assert note in result.stdout


@mark.parametrize('note', ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'])
def test_cli_scale_must_contain_the_notes_in_the_f_response_scale(note):
    result = runner.invoke(app, ['scale', 'F'])
    assert note in result.stdout


@mark.parametrize('degree', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_cli_scale_must_contain_the_all_degrees(degree):
    result = runner.invoke(app, ['scale', 'F'])
    assert degree in result.stdout


@mark.parametrize('note', ['C', 'E', 'G'])
def test_cli_chords_must_contain_the_notes_in_the_response(note):
    result = runner.invoke(app, ['chord'])
    assert note in result.stdout


@mark.parametrize('degree', ['I', 'III', 'V'])
def test_cli_chords_must_contain_the_all_degrees(degree):
    result = runner.invoke(app, ['chord'])
    assert degree in result.stdout


@mark.parametrize('cipher', ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bº'])
def test_cli_harmonic_field_must_contain_the_all_degrees(cipher):
    result = runner.invoke(app, ['harmonic-field', 'C'])
    assert cipher in result.stdout


@mark.parametrize('degree', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viiº'])
def test_cli_harmonic_field_must_contain_the_all_degrees(degree):
    result = runner.invoke(app, ['harmonic-field', 'C'])
    assert degree in result.stdout
