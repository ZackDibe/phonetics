from . import utils

__ALL__ = [
    'nysiis']


def nysiis(source):
    start_map = {
        'MAC': 'MCC', 'KN': 'N', 'K': 'C',
        'PH': 'FF', 'PF': 'FF', 'SCH': 'SSS'
    }
    end_map = {
        'EE': 'Y', 'IE': 'Y', 'DT': 'D', 'RT': 'D',
        'RD': 'D', 'NT': 'D', 'ND': 'D'
    }
    tr_map = {
        'Q': 'G', 'Z': 'S', 'M': 'N', 'A': 'A',
        'E': 'A', 'I': 'A', 'O': 'A', 'U': 'A',
        'KN': 'N', 'SCH': 'SSS', 'PH': 'FF', 'EV': 'AF'
    }

    source = list(source.upper())

    for key in start_map:
        if utils.startswith(source, key):
            source = list(start_map[key]) + source[len(key):]

    for key in end_map:
        if utils.endswith(source, key):
            source = source[:len(key)] + list(end_map[key])

    phonetic = [source[0]]

    for i, c in enumerate(source):
        next_c = i + 1 < len(source) and source[i + 1]
        prev_c = i - 1 >= 0 and source[i - 1]

        next_two = ''.join(source[i:i+1]) if i + 1 < len(source) else None
        next_three = ''.join(source[i:i+2]) if i + 2 < len(source) else None

        current = None

        if next_two in tr_map:
            current = tr_map[next_two]
        elif next_three in tr_map:
            current = tr_map[next_three]
        elif c in tr_map:
            current = tr_map[c]
        elif (c == 'H' and
              prev_c and
              not utils.isvowel(prev_c) and
              next_c and
              not utils.isvowel(next_c)):
            current = prev_c
        elif c == 'W' and utils.isvowel(prev_c):
            current = 'A'

        if current and current != phonetic[-1]:
            phonetic.append(current)

    if phonetic[-1] == 'S':
        phonetic.pop(-1)
    if phonetic[-2:] == 'AY':
        phonetic.pop(-2)
    if phonetic[-1] == 'S':
        phonetic.pop(-1)

    return ''.join(phonetic)
