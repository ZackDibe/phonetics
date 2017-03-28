__ALL__ = [
    'soundex']


def soundex(source, size=4):
    letter_to_digit = "01230120022455012623010202"
    t = [source[0]]

    for c in source[1:]:
        digit = letter_to_digit[ord(c)-ord('a')]
        if digit and digit != t[-1]:
            t.append(digit)

    for _ in range(size - len(t)):
        t.append('0')

    return ''.join(t)
