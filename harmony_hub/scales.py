NOTES = 'C Db D Eb E F Gb G Ab A Bb B'.split()
SCALES = {
    'major': (0, 2, 4, 5, 7, 9, 11),
    'minor': (0, 2, 3, 5, 7, 8, 10),
}


def scale(tonic: str, mode: str) -> dict[str, list[str]]:
    """
    Generates a scale from a tonic and a mode.

    Parameters:
        tonic: The fundamental note of the scale.
        mode: Scale character.


    Returns:
        A dictionary with scale notes and degrees.

    Raises:
        ValueError: If the tonic is not valid note.
        KeyError: If the scale does not exist or has not been implemented.

    Examples:
        >>> scale('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('a', 'minor')
        {'notes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonic = tonic.capitalize()
    try:
        intervals = SCALES[mode]
        tonic_pos = NOTES.index(tonic)
    except ValueError:
        raise ValueError(
            f'This tonic does not exist, try one of these {NOTES}.'
        )
    except KeyError:
        raise KeyError(
            'This mode does not exist or has not been implemented. '
            f'try one of these {list(SCALES.keys())}.'
        )

    temp = []

    for interval in intervals:
        note = (tonic_pos + interval) % 12
        temp.append(NOTES[note])

    return {
        'notes': temp,
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
