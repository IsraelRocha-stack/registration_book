def double(n):
    out = n * 2
    return out


def half(p):
    out = p / 2
    return out


def percent(p, t):
    out = p * (t / 100)
    return out


def rmpercent(p, t):
    out = p - (p * t / 100)
    return out


def addpercent(p, t):
    out = p + (p * t / 100)
    return out


def coin(p=0, coins='R$'):
    if p == 0:
        return f'{coins} '.replace('.', ',')
    if p != 0:
        return f'{coins}{p} '.replace('.', ',')
