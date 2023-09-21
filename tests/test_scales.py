"""
AAA - 3A - A3

Arrange - Act -Assets!
Arrumar - Agir - Garantir!
"""
from pytest import mark, raises

from harmony_hub.scales import NOTES, SCALES, scale


def test_should_work_with_lowercase_notes():
    # Arrange
    tonic = 'c'
    mode = 'major'

    # Act
    result = scale(tonic, mode)

    # Assert
    assert result


def test_should_return_an_error_saying_that_the_tonic_does_not_exist():
    tonic = 'X'
    mode = 'major'

    error_message = f'This tonic does not exist, try one of these {NOTES}.'

    with raises(ValueError) as error:
        scale(tonic, mode)

    assert error_message == error.value.args[0]


def test_should_return_an_error_saying_that_the_mode_does_not_exist():
    tonic = 'c'
    mode = 'mode'

    error_message = (
        'This mode does not exist or has not been implemented. '
        f'try one of these {list(SCALES.keys())}.'
    )

    with raises(KeyError) as error:
        scale(tonic, mode)

    assert error_message == error.value.args[0]


@mark.parametrize(
    'tonic, mode, expected',
    [
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C', 'minor', ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']),
        ('Db', 'major', ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C']),
        ('Db', 'minor', ['Db', 'Eb', 'E', 'Gb', 'Ab', 'A', 'B']),
        ('D', 'major', ['D', 'E', 'Gb', 'G', 'A', 'B', 'Db']),
        ('D', 'minor', ['D', 'E', 'F', 'G', 'A', 'Bb', 'C']),
        ('Eb', 'major', ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']),
        ('Eb', 'minor', ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'B', 'Db']),
        ('E', 'major', ['E', 'Gb', 'Ab', 'A', 'B', 'Db', 'Eb']),
        ('E', 'minor', ['E', 'Gb', 'G', 'A', 'B', 'C', 'D']),
        ('F', 'major', ['F', 'G', 'A', 'Bb', 'C', 'D', 'E']),
        ('F', 'minor', ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb']),
        ('Gb', 'major', ['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F']),
        ('Gb', 'minor', ['Gb', 'Ab', 'A', 'B', 'Db', 'D', 'E']),
        ('G', 'major', ['G', 'A', 'B', 'C', 'D', 'E', 'Gb']),
        ('G', 'minor', ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F']),
        ('Ab', 'major', ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']),
        ('Ab', 'minor', ['Ab', 'Bb', 'B', 'Db', 'Eb', 'E', 'Gb']),
        ('A', 'major', ['A', 'B', 'Db', 'D', 'E', 'Gb', 'Ab']),
        ('A', 'minor', ['A', 'B', 'C', 'D', 'E', 'F', 'G']),
        ('Bb', 'major', ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']),
        ('Bb', 'minor', ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab']),
        ('B', 'major', ['B', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'Bb']),
        ('B', 'minor', ['B', 'Db', 'D', 'E', 'Gb', 'G', 'A']),
    ],
)
def test_must_return_to_correct_notes(tonic, mode, expected):
    result = scale(tonic, mode)
    assert result['notes'] == expected


def test_must_return_to_seven_degrees():
    tonic = 'e'
    mode = 'minor'
    expected = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    result = scale(tonic, mode)

    assert result['degrees'] == expected
