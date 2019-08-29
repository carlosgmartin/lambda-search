# https://web.ics.purdue.edu/~dulrich/C-pure-intuitionism-page.htm

def parse(string):
    stack = []
    for char in reversed(string):
        if char == 'C':
            a = stack.pop()
            b = stack.pop()
            stack.append((a, b))
        else:
            stack.append(char)
    return stack.pop()

def stringify(tree):
    if isinstance(tree, tuple):
        return '({} -> {})'.format(*map(stringify, tree))
    else:
        return tree

assert stringify(parse('CpCqp')) == '(p -> (q -> p))'
assert stringify(parse('CCpCqrCCpqCpr')) == '((p -> (q -> r)) -> ((p -> q) -> (p -> r)))'

# https://www.hedonisticlearning.com/djinn/

candidates = '''\
CCCpqrCCCpqCrsCqs
CCCpqrCCCprCrsCqs
CCCpqrCCqCrCrsCqs
CCCpqrCCqCrsCpCqs
CCCpqrCCrCrsCpCqs
CCCCpqrsCCsCspCrp
CCCCpqrsCCsCsqCrq
CCCpqCrsCCqrCpCqs
CCCpqCrsCpCCqrCqs
CCCpqCrsCCCpqrCqs
CCCpqrCpCCqCrsCqs
CCCpqrCpCCrCrsCqs
CCpCqrCCCsCspqCpr
CCpCqrCCCspCpqCpr
CCpCqrCCCspqCsCpr
CCpCqrCsCCCspqCpr
CCpqCCCrCrpCqsCps
CCpqCCCrpCqCpsCps
CCpqCCCrpCqCqsCps
CCpqCCqCCrpsCrCps
CCpqCrCCCrpCqsCps
CpCCCpqrCCrCrsCqs\
'''.split('\n')

for candidate in candidates:
    print('x::' + stringify(parse(candidate)))

# CCCpqrCsCCqCrtCqt
# x :: ((p -> q) -> r) -> s -> (q -> r -> t) -> q -> t
# x a _ b c = b c (a (\ _ -> c))

# CCCpqrCCqCrsCpCqs
# x :: ((p -> q) -> r) -> (q -> r -> s) -> p -> q -> s
# x a b _ c = b c (a (\ _ -> c))
