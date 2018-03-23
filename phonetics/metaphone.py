# -*- coding: utf-8 -*-
from . import utils

__ALL__ = [
    'metaphone',
    'dmetaphone']

SILENT_LETTERS = {'KN', 'GN', 'PN', 'PS', 'WR'}


def metaphone(source):
    return dmetaphone(source)[0]


def check_start(s):
    if s[:2] in SILENT_LETTERS:
        return ('', '', 1)
    elif s.get(0) == 'X':
        return ('S', 'S', 1)
    return ('', '', 0)


def process_B(s, idx, last, slavogermanic):
    return ('P', 'P', (s.get(idx + 1) == 'B') + 1)


def process_C(s, idx, last, slavogermanic):
    if (idx > 1 and
        not utils.isvowel(s.get(idx - 2)) and
        s.get(idx - 1, 3) == "ACH" and
        (s.get(idx + 2) != 'I' and
         (s.get(idx + 2) != 'E' or
          s.get(idx - 2, 6) in {"BACHER", "MACHER"}))):
        return ('K', 'K', 2)
    elif idx == 0 and s.get(0, 6) == 'CAESAR':
        return ('S', 'S', 2)
    elif s.get(idx, 4) == 'CHIA':
        return ('K', 'K', 2)
    elif s.get(idx, 2) == 'CH':
        if idx > 0 and s.get(idx, 4) == 'CHAE':
            return ('K', 'X', 2)
        elif (idx == 0 and
              (s.get(idx + 1, 5) in {'HARAC', 'HARIS'} or
               s.get(idx + 1, 3) in {"HOR", "HYM", "HIA", "HEM"}) and
              s.get(idx, 5) != "CHORE"):
            return ('K', 'K', 2)
        elif ((s.get(0, 4) in {'VAN ', 'VON '} or s.get(0, 3) == 'SCH') or
              s.get(idx - 2, 6) in {'ORCHES', 'ARCHIT', 'ORCHID'} or
              s.get(idx + 2) in {'T', 'S'} or
              ((s.get(idx - 1) in {'A', 'O', 'U', 'E'} or idx == 0) and
               s.get(idx + 2) in {'L', 'R', 'N', 'M', 'B', 'H', 'F', 'V', 'W'})):
            return ('K', 'K', 2)
        else:
            if idx > 0:
                if s.get(0, 2) == 'MC':
                    return ('K', 'K', 2)
                else:
                    return ('X', 'K', 2)
            else:
                return ('X', 'X', 2)
    elif s.get(idx, 2) == 'CZ' and not s.get(idx - 2, 4) == 'WICZ':
        return ('S', 'X', 2)
    elif s.get(idx + 1, 3) == 'CIA':
        return ('X', 'X', 3)
    elif s.get(idx, 2) == 'CC' and not (idx == 1 and s.get(0) == 'M'):
        if (s.get(idx + 2) in {'I', 'E', 'H'} and
           not s.get(idx + 2, 2) == 'HU'):
            if ((idx == 1 and s.get(idx - 1) == 'A') or
               s.get(idx - 1, 5) in {'UCCEE', 'UCCES'}):
                return ('KS', 'KS', 3)
            else:
                return ('X', 'X', 3)
        else:
            return ('K', 'K', 2)
    elif s.get(idx, 2) in {'CK', 'CG', 'CQ'}:
        return ('K', 'K', 2)
    elif s.get(idx, 2) in {'CI', 'CE', 'CY'}:
        if s.get(idx, 3) in {'CIO', 'CIE', 'CIA'}:
            return ('S', 'X', 2)
        else:
            return ('S', 'S', 2)
    else:
        if s.get(idx + 1, 2) in {' C', ' K', ' Q', ' G'}:
            return ('K', 'K', 3)
        elif (s.get(idx + 1) in {'C', 'K', 'Q'} and
              s.get(idx + 1, 2) not in {'CE', 'CI'}):
            return ('K', 'K', 2)
        else:
            return ('K', 'K', 1)


def process_D(s, idx, last, slavogermanic):
    if s.get(idx, 2) == 'DG':
        if s.get(idx + 2) in {'I', 'E', 'Y'}:
            return ('J', 'J', 3)
        else:
            return ('TK', 'TK', 2)
    else:
        if s.get(idx, 2) in {'DT', 'DD'}:
            return ('T', 'T', 2)
        return ('T', 'T', 1)


def process_G(s, idx, last, slavogermanic):
    if s.get(idx + 1) == 'H':
        if idx > 0 and not utils.isvowel(s[idx - 1]):
            return ('K',  'K', 2)
        elif idx == 0:
            if s.get(idx + 2) == 'I':
                return ('J',  'J', 2)
            else:
                return ('K',  'K', 2)
        elif ((idx > 1 and s.get(idx - 2) in {'B', 'H', 'D'}) or
              (idx > 2 and s.get(idx - 3) in {'B', 'H', 'D'}) or
              (idx > 3 and s.get(idx - 4) in {'B', 'H'})):
            return ('', '', 2)
        else:
            if (idx > 2 and s.get(idx - 1) == 'U' and
               s.get(idx - 3) in {'C', 'G', 'L', 'R', 'T'}):
                return ('F',  'F', 2)
            elif idx > 0 and s.get(idx - 1) != 'I':
                return ('K',  'K', 2)
    elif s.get(idx + 1) == 'N':
        if idx == 1 and utils.isvowel(s[0]) and not slavogermanic:
            return ('KN',  'K', 2)
        elif (s.get(idx + 2, 2) != 'EY' and
              s.get(idx + 1) != 'Y' and
              not slavogermanic):
            return ('N',  'KN', 2)
        else:
            return ('KN',  'KN', 2)
    elif s.get(idx + 1, 2) == 'LI' and not slavogermanic:
        return ('KL',  'L', 2)
    elif (idx == 0 and
          (s.get(idx + 1) == 'Y' or
           s.get(idx + 1, 2) in {'ES', 'EP', 'EB', 'EL', 'EY', 'IB', 'IL', 'IN', 'IE', 'EI', 'ER'})):
        return ('K',  'J', 2)
    elif ((s.get(idx + 1, 2) == 'ER' or s.get(idx + 1) == 'Y') and
          s.get(0, 6) not in {'DANGER', 'RANGER', 'MANGER'} and
          s.get(idx - 1) not in {'E', 'I'} and
          s.get(idx - 1, 3) not in {'RGY', 'OGY'}):
        return ('K',  'J', 2)
    elif (s.get(idx + 1) in {'E', 'I', 'Y'} or
          s.get(idx - 1, 4) in {'AGGI', 'OGGI'}):
        if ((s.get(0, 4) in {'VAN ', 'VON '} or
             s.get(0, 3) == 'SCH') or
           s.get(idx + 1, 2) == 'ET'):
            return ('K', 'K', 2)
        else:
            if s.get(idx + 1, 4) == 'IER ':
                return ('J', 'J', 2)
            else:
                return ('J', 'K', 2)
    else:
        if s.get(idx + 1) == 'G':
            return ('K', 'K', 2)
        return ('K', 'K', 1)


def process_H(s, idx, last, slavogermanic):
    if ((idx == 0 or utils.isvowel(s.get(idx-1))) and
       utils.isvowel(s.get(idx + 1))):
        return ('H', 'H', 2)
    else:
        return ('', '', 1)


def process_J(s, idx, last, slavogermanic):
    if s.get(idx, 4) == 'JOSE' or s.get(0, 4) == 'SAN ':
        if (idx == 0 and s.get(idx+4) == ' ') or s.get(0, 4) == 'SAN ':
            return ('H', 'H', 1)
        else:
            return ('J', 'H', 1)
    else:
        primary = ''
        secondary = ''
        if idx == 0 and not s.get(idx, 4) == 'JOSE':
            primary = 'J'
            secondary = 'A'
        else:
            if (utils.isvowel(s.get(idx - 1)) and
                not slavogermanic and
               (s.get(idx + 1) == 'A' or s.get(idx + 1) == 'O')):
                primary = 'J'
                secondary = 'H'
            else:
                if idx == last:
                    primary = 'J'
                elif (s.get(idx + 1) not in {'L', 'T', 'K', 'S', 'N', 'M', 'B', 'Z'} and
                      s.get(idx - 1) not in {'S', 'K', 'L'}):
                    primary = 'J'
                    secondary = 'J'
        if s.get(idx + 1) == 'J':
            return (primary, secondary, 2)
        return (primary, secondary, 1)


def process_F(s, idx, last, slavogermanic):
    return (s[idx], s[idx], (s.get(idx + 1) == s[idx]) + 1)

process_K = process_F
process_N = process_F


def process_L(s, idx, last, slavogermanic):
    primary = 'L'
    secondary = ''
    if s.get(idx + 1) == 'L':
        if not ((idx == len(s) - 3 and
                 s.get(idx - 1, 4) in {'ILLO', 'ILLA', 'ALLE'}) or
                ((s.get(len(s) - 2, 2) in {'AS', 'OS'} or
                  s.get(last) in {'A', 'O'}) and
                 s.get(idx - 1, 4) == 'ALLE')):
            secondary = 'L'
        return (primary, secondary, 2)
    else:
        return (primary, 'L', 1)


def process_M(s, idx, last, slavogermanic):
    if ((s.get(idx - 1, 3) == 'UMB' and
         (idx + 1 == last or s.get(idx + 2, 2) == 'ER')) or
       s.get(idx + 1) == 'M'):
        return ('M', 'M', 2)
    return ('M', 'M', 1)


def process_P(s, idx, last, slavogermanic):
    if s.get(idx + 1) == 'H':
        return ('F', 'F', 2)
    else:
        if s.get(idx + 1) in {'P', 'B'}:
            return ('P', 'P', 3)
        return ('P', 'P', 1)


def process_Q(s, idx, last, slavogermanic):
    return ('K', 'K', (s.get(idx + 1) == s[idx]) + 1)


def process_R(s, idx, last, slavogermanic):
    primary = ''
    secondary = 'R'
    if not (idx == last and
            not slavogermanic and
            s.get(idx - 2, 2) == 'IE' and
            not s.get(idx - 4, 2) in {'ME', 'MA'}):
        primary = 'R'
    return (primary, secondary, (s.get(idx+1) == 'R') + 1)


def process_S(s, idx, last, slavogermanic):
    if s.get(idx - 1, 3) in {'ISL', 'YSL'}:
        idx += 1
    elif idx == 0 and s.get(idx, 5) == 'SUGAR':
        return ('X', 'S', 1)
    elif s.get(idx, 2) == 'SH':
        if s.get(idx + 1, 4) in {'HEIM', 'HOEK', 'HOLM', 'HOLZ'}:
            return ('S', 'S', 2)
        else:
            return ('X', 'X', 2)
    elif s.get(idx, 3) in {'SIO', 'SIA'} or s.get(idx, 4) in {'SIAN'}:
        if not slavogermanic:
            return ('S', 'X', 3)
        else:
            return ('S', 'S', 3)
    elif ((idx == 0 and s.get(idx + 1) in {'M', 'N', 'L', 'W'}) or
          s.get(idx + 1) == 'Z'):
        return ('S', 'X', (s.get(idx + 1) == 'Z') + 1)
    elif s.get(idx, 2) == 'SC':
        if s.get(idx + 2) == 'H':
            if s.get(idx + 3, 2) in {'OO', 'ER', 'EN', 'UY', 'ED', 'EM'}:
                if s.get(idx + 3, 2) in {'ER', 'EN'}:
                    return ('X', 'SK', 3)
                else:
                    return ('SK', 'SK', 3)
            else:
                if (idx == 0 and not utils.isvowel(s.get(3)) and s.get(3) != 'W'):
                    return ('X', 'S', 3)
                else:
                    return ('X', 'X', 3)
        elif s.get(idx + 2) in {'I', 'E', 'Y'}:
            return ('S', 'S', 3)
        else:
            return ('SK', 'SK', 3)
    else:
        if idx == last and s.get(idx - 2, 2) in {'AI', 'OI'}:
            return ('', 'S', (s.get(idx + 1) in {'S', 'Z'}) + 1)
        return ('S', 'S', (s.get(idx + 1) in {'S', 'Z'}) + 1)


def process_T(s, idx, last, slavogermanic):
    if s.get(idx, 4) == 'TION' or s.get(idx, 3) in {'TIA', 'TCH'}:
        return ('X', 'X', 3)
    elif s.get(idx, 2) == 'TH' or s.get(idx, 3) == 'TTH':
        if (s.get(idx + 2, 2) in {'OM', 'AM'} or
           s.get(0, 4) in {'VAN ', 'VON '} or
           s.get(0, 3) == 'SCH'):
            return ('T', 'T', 2)
        else:
            return ('0', 'T', 2)
    else:
        return ('T', 'T', (s.get(idx + 1) in {'T', 'D'}) + 1)


def process_V(s, idx, last, slavogermanic):
    return ('F', 'F', (s.get(idx + 1) == s[idx]) + 1)


def process_W(s, idx, last, slavogermanic):
    if s.get(idx, 2) == 'WR':
        return ('R', 'R', 2)
    elif ((idx == last and utils.isvowel(s.get(idx - 1))) or
          s.get(idx - 1, 5) in {'EWSKI', 'EWSKY', 'OWSKI', 'OWSKY'} or
          s.get(0, 3) == 'SCH'):
        return ('', 'F', 1)
    elif s.get(idx, 4) in {'WICZ', 'WITZ'}:
        return ('TS', 'FX', 4)
    elif (idx == 0 and
          (utils.isvowel(s.get(idx + 1)) or s.get(idx, 2) == 'WH')):
        if utils.isvowel(s.get(idx + 1)):
            return ('A', 'F', 1)
        else:
            return ('A', 'A', 1)
    else:
        return ('', '', 1)


def process_X(s, idx, last, slavogermanic):
    primary = ''
    secondary = ''
    if not (idx == last and (s.get(idx - 3, 3) in {'IAU', 'EAU'} or
                             s.get(idx - 2, 2) in {'AU', 'OU'})):
        primary = 'KS'
        secondary = 'KS'
    return (primary, secondary, (s.get(idx + 1) in {'C', 'X'}) + 1)


def process_Z(s, idx, last, slavogermanic):
    if s.get(idx + 1) == 'H':
        return ('J', 'J', 2)
    else:
        if (s.get(idx + 1, 2) in {'ZO', 'ZO', 'ZA'} or
           (slavogermanic and idx > 0 and s.get(idx - 1) != 'T')):
            return ('S', 'TS', (s.get(idx + 1) == 'Z') + 1)
        else:
            return ('S', 'S', (s.get(idx + 1) == 'Z') + 1)


def process_vowel(s, idx, last, slavogermanic):
    if idx == 0:
        return ('A', 'A', 1)
    return ('', '', 1)

process_A = process_vowel
process_E = process_vowel
process_I = process_vowel
process_O = process_vowel
process_U = process_vowel
process_Y = process_vowel


def dmetaphone(source):
    source = utils.LazyString(source.upper())
    slavogermanic = utils.isslavogermanic(source)
    last = len(source) - 1
    primary, secondary, index = check_start(source)

    while index < len(source):
        func = globals().get('process_{}'.format(source[index]))
        if func:
            result = func(source, index, last, slavogermanic)
            if not result:
                index += 1
                continue
            if result[0]:
                primary += result[0]
            if result[1]:
                secondary += result[1]
            index += result[2]
        else:
            index += 1

    if primary == secondary:
        secondary = ""

    return (primary, secondary)
