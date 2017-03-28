__ALL__ = [
    'LazyString',
    'startswith',
    'endswith',
    'isvowel',
    'isslavogermanic']


class LazyString(str):
    def get(self, idx, dist=None):
        if not self:
            return None
        if idx < 0 or idx >= len(self):
            return None
        if dist:
            if idx + dist > len(self):
                return None
            return self[idx:idx+dist]
        return self[idx]


def startswith(source, matchwith):
    return all(map(lambda x: x[0] == x[1], zip(source, matchwith)))


def endswith(source, matchwith):
    return all(map(lambda x: x[0] == x[1], zip(source[::-1], matchwith[::-1])))


def isvowel(c):
    return c and c.upper() in {'A', 'E', 'I', 'O', 'U', 'Y'}


def isslavogermanic(s):
    if not s:
        return False
    s = s.upper()
    return "W" in s or "K" in s or "CZ" in s or "WITZ" in s
