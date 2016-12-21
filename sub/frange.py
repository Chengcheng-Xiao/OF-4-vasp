def frange(start, end=None, inc=None):
    "A range function, that does accept float increments..."

    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next == end:#+0.000000000000001: #some precision problem, using this 0.000...1 to overcome, not so elegant.
            L.append(next)
            break
        elif inc > 0 and next > end:#+0.000000000000001:
            break
        elif inc < 0 and next == end:#:-0.000000000000001:
            L.append(next)
            break
        elif inc < 0 and next < end:#:-0.000000000000001:
            break
        L.append(next)

    return L

#test this sub
#print frange(2,3,0.01)
