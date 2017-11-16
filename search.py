from enumerate import string, Abs, App
from reduce import normalize, trace
from itertools import count
from infinitary import disjoint_union

K = Abs(Abs(1))
S = Abs(Abs(Abs(App(App(2, 0), App(1, 0)))))
ι = Abs(App(App(App(0, K), S), K))
# ι = Abs(Abs(Abs(Abs(App(App(1, 0), App(3, Abs(1)))))))
ι = Abs(App(App(0, K), S))
ι = Abs(App(App(0, S), K))

U = Abs(App(App(App(0, K), S), K))
U = normalize(U)


ι = Abs(Abs(Abs(Abs(App(App(1, 0), App(3, Abs(1)))))))
ι = Abs(App(App(0, K), S))
ι = App(K, K)
U = K


def tree_constructors():
  def trees(size):
    if size == 0:
      yield 0
    else:
      for subsize in range(size):
        for a in trees(subsize):
          for b in trees(size - 1 - subsize):
            yield App(a, b)
  for size in count():
    yield from map(Abs, trees(size))

def dim(string):
  return '\033[2m{}\033[0m'.format(string)





block = normalize(Abs(App(App(0, S), K))) # Abs(Abs(Abs(Abs(App(App(1, 0), App(3, Abs(1)))))))
target = Abs(Abs(App(0, 1)))
# ((A (A (A A))) (((A (A (A (A A)))) (A A)) (A A))) → B


block = Abs(Abs(Abs(Abs(App(App(1, 0), App(3, Abs(1)))))))
target = S
# (((A (((A (((A A) A) (A A))) A) (A A))) A) (A A)) → K
# last ((((ι (ι ((ι (ι ((ι ι) (ι ι)))) (ι ι)))) (ι ι)) (ι ι)) ((ι ι) ι))



for constructor in tree_constructors():
  normal = normalize(App(constructor, block), max_steps=100)
  if normal == target:
    print('{} → {}'.format(string(constructor.body).replace('0', 'A'), 'B'))
    break
  else:
    print(dim(string(constructor.body).replace('0', 'ι')))

exit()




print('ι = {}'.format(string(ι)))
print('U = {}\n'.format(string(U)))

indices = tree_constructors()
function = lambda constructor: trace(App(constructor, ι))
for constructor, value in disjoint_union(indices, function):
  print(dim(string(constructor.body).replace('0', 'ι')))
  #print(string(value))
  #print()
  if value == K:
    exit()




'''
K_complete = False
S_complete = False
for constructor in applications():
  normal = normalize(App(constructor, ι))
  if not K_complete and normal == K:
    print('{} → {}'.format(string(constructor.body).replace('0', 'ι'), 'K'))
    K_complete = True
    if S_complete:
      exit()
  elif not S_complete and normal == S:
    print('{} → {}'.format(string(constructor.body).replace('0', 'ι'), 'S'))
    S_complete = True
    if K_complete:
      exit()
  else:
    print(dim(string(constructor.body).replace('0', 'ι')))
'''


'''
K_complete = False
S_complete = False
for size in count():
  for tree in trees(size):
    constructor = Abs(tree)
    term = App(constructor, ι)
    normal = normalize(term)
    print(dim(string(tree).replace('0', 'ι')))
    if normal == K:
      print('{} → {}'.format(string(tree).replace('0', 'ι'), 'K'))
      K_complete = True
      if S_complete:
        exit()
    elif normal == S:
      print('{} → {}'.format(string(tree).replace('0', 'ι'), 'S'))
      S_complete = True
      if K_complete:
        exit()
'''