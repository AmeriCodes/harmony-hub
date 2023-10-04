from harmony_hub.chords import triads
from harmony_hub.scales import scale


def _scale_triads(note, scale_notes):
    """
    Knowing if the notes of a chord are in the scale.

    Examples:
        >>> _scale_triads('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
        >>> _scale_triads('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
        >>> _scale_triads('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Bº'
    """
    root, third, fifth = triads(note, 'major')

    match third in scale_notes, fifth in scale_notes:
        case True, True:
            return root
        case False, True:
            return f'{root}m'
        case False, False:
            return f'{root}º'


def _convert_degrees(cipher, degree):
    """
    Converts relative degrees to cipher.

    Parameters:
        cipher: A chord figure
        degree: Degree in major form

    Examples:
        >>> _convert_degrees('C', 'I')
        'I'
        >>> _convert_degrees('Cm', 'I')
        'i'
        >>> _convert_degrees('Cº', 'I')
        'iº'
    """
    if 'm' in cipher:
        return degree.lower()

    elif 'º' in cipher:

        return f'{degree.lower()}º'

    return degree


def harmonic_field(root: str, mode: str) -> dict[str, list[str]]:
    """
    Generates a harmonic field based on a root note and a mode

    Parameters:
        root: Fundamental note of the harmonic field
        mode: Tone for the field. Ex: major, minor, etc. . .

    Returns:
        A harmônic field, a chord progression.

    Examples:
        >>> harmonic_field('c', 'major')
        {'chords': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bº'], 'degrees': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'viiº']}
        >>> harmonic_field('c', 'minor')
        {'chords': ['Cm', 'Dº', 'Eb', 'Fm', 'Gm', 'Ab', 'Bb'], 'degrees': ['i', 'iiº', 'III', 'iv', 'v', 'VI', 'VII']}
    """
    notes, _degrees = scale(root, mode).values()
    chords = [_scale_triads(note, notes) for note in notes]
    degrees = [
        _convert_degrees(chord, degree)
        for chord, degree in zip(chords, _degrees)
    ]

    return {'chords': chords, 'degrees': degrees}
