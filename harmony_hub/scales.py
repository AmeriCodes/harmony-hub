NOTES = 'C Db D Eb E F Gb G Ab A Bb B'.split()
SCALES = {
    'major': (0, 2, 4, 5, 7, 9, 11),
    'minor': (0, 2, 3, 5, 7, 8, 10),
}


def scales(tonic: str, mode: str) -> dict[str, list[str]]:
    """
    Generates a scale from a tonic and a mode.

    Parameters:
        tonic: The fundamental note of the scale.
        mode: Scale character.


    Returns:
        A dictionary with scale notes and degrees.

    Examples:
        >>> scales('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scales('A', 'minor')
        {'notes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervals = SCALES[mode]
    tonic_pos = NOTES.index(tonic)

    temp = []

    for interval in intervals:
        note = (tonic_pos + interval) % 12
        temp.append(NOTES[note])

    return {
        'notes': temp,
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
