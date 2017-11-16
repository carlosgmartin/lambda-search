from collections import namedtuple
from itertools import count

Abs = namedtuple('Abs', ['body'])
App = namedtuple('App', ['function', 'argument'])

def terms(size, depth=0):
  if size == 0:
    yield from range(depth)
  else:
    yield from map(Abs, terms(size - 1, depth + 1))
    for subsize in range(size):
      for a in terms(subsize, depth):
        for b in terms(size - 1 - subsize, depth):
          yield App(a, b)

def string(term):
  if isinstance(term, Abs):
    return '(λ {})'.format(string(term.body))
  elif isinstance(term, App):
    return '({} {})'.format(string(term.function), string(term.argument))
  else:
    return '{}'.format(term)

if __name__ == '__main__':
  for size in count():
    for term in terms(size):
      print(string(term))
