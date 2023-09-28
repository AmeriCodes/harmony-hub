from harmony_hub.scales import NOTES, scale


def _minor(cipher):
    note, _ = cipher.split('m')

    if '+' in cipher:
        root, third, fifth = triads(note, 'minor')
        notes = [root, third, semitone(fifth, interval=1)]
        degrees = ['I', 'III-', 'V+']

    else:
        notes = triads(note, 'minor')
        degrees = ['I', 'III-', 'V']

    return notes, degrees


def semitone(note, *, interval):
    pos = NOTES.index(note) + interval

    return NOTES[pos % 12]


def triads(note, tonic):
    degrees = (0, 2, 4)
    scale_notes, _ = scale(note, tonic).values()

    return [scale_notes[degree] for degree in degrees]


def chord(cipher: str) -> dict[str, list[str]]:
    """
    Generates the notes of a chord based on a chord.

    Parameters:
        cipher: A chord in the form of a cipher

    Returns:
        A dictionary with the notes and degrees corresponding to the major scale.

    Examples:
        >>> chord('C')
        {'notes': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}

        >>> chord('Cm')
        {'notes': ['C', 'Eb', 'G'], 'degrees': ['I', 'III-', 'V']}

        >>> chord('Cº')
        {'notes': ['C', 'Eb', 'Gb'], 'degrees': ['I', 'III-', 'V-']}

        >>> chord('C+')
        {'notes': ['C', 'E', 'Ab'], 'degrees': ['I', 'III', 'V+']}

        >>> chord('Cm+')
        {'notes': ['C', 'Eb', 'Ab'], 'degrees': ['I', 'III-', 'V+']}
    """
    if 'm' in cipher:
        notes, degrees = _minor(cipher)

    elif 'º' in cipher:
        note, _ = cipher.split('º')
        root, third, fifth = triads(note, 'minor')
        notes = [root, third, semitone(fifth, interval=-1)]
        degrees = ['I', 'III-', 'V-']

    elif '+' in cipher:
        note, _ = cipher
        root, third, fifth = triads(note, 'major')
        notes = [root, third, semitone(fifth, interval=+1)]
        degrees = ['I', 'III', 'V+']

    else:
        notes = triads(cipher, 'major')
        degrees = ['I', 'III', 'V']

    return {'notes': notes, 'degrees': degrees}
