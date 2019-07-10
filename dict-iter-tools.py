D1={1: {2: {3: 4, 5: 6}, 3: {4: 5, 6: 7}}, 2: {3: {4: 5}, 4: {6: 7}}}
print(D1)

acc = []

def testitem(i):
    return i % 2 == 0

def infoquantifier(p):
    return p % 5


def iterdict(d):
    global acc
    for k, v in d.items():
        if isinstance(v, dict):
            iterdict(v)
        else:
            if testitem(v):
                acc.append((k, infoquantifier(v)))
            else:
                acc.append((k, infoquantifier(v)))

iterdict(D1)

print(acc)
