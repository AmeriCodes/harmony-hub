from pytest import mark

from harmony_hub.chords import chord

"""
Entry
chord Cm

Expected:
I - III - V
C    Eb    G

{'notas': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}
"""


@mark.parametrize(
    'note, expected',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'Eb', 'G']),
        ('Cº', ['C', 'Eb', 'Gb']),
        ('C+', ['C', 'E', 'Ab']),
        ('Cm+', ['C', 'Eb', 'Ab']),
    ],
)
def test_chord_must_return_the_corresponding_notes(note, expected):
    notes, _ = chord(note).values()

    assert expected == notes


@mark.parametrize(
    'cipher, expected',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('Cº', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)
def test_chord_must_return_the_corresponding_degrees(cipher, expected):
    _, degrees = chord(cipher).values()

    assert expected == degrees
