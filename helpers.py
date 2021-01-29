from nltk.tokenize import sent_tokenize


def lines(a, b):
    a = set(a.split('\n'))
    b = set(b.split('\n'))
    u = a.intersection(b)
    c = list(u)
    return c


def sentences(a, b):
    a = sent_tokenize(a)
    b = sent_tokenize(b)
    c = set(a)
    d = set(b)
    e = c.intersection(d)
    f = list(e)
    return f


def substrings(a, b, n):
    c = []
    d = []
    x = len(a)
    y = len(b)
    nn = n
    for i in range(x):
        if n <= x:
            c.append(a[i:n])
            n += 1
        else:
            break

    for j in range(y):
        if nn <= y:
            d.append(b[j:nn])
            nn += 1
        else:
            break

    e = set(c)
    f = set(d)
    g = e.intersection(f)
    h = list(g)
    return h
