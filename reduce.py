from enumerate import Abs, App, string

def lift(term, offset, depth=0):
  if isinstance(term, Abs):
    return Abs(lift(term.body, offset, depth + 1))
  elif isinstance(term, App):
    return App(
      lift(term.function, offset, depth), 
      lift(term.argument, offset, depth)
    )
  else:
    if term < depth:
      return term
    else:
      return term + offset

def substitute(term, replacement, variable=0):
  if isinstance(term, Abs):
    return Abs(substitute(term.body, replacement, variable + 1))
  elif isinstance(term, App):
    return App(
      substitute(term.function, replacement, variable), 
      substitute(term.argument, replacement, variable)
    )
  else:
    if term < variable:
      return term
    elif term == variable:
      return lift(replacement, variable)
    else:
      return term - 1

def occurs(variable, term):
  if isinstance(term, Abs):
    return occurs(variable + 1, term.body)
  elif isinstance(term, App):
    return occurs(variable, term.function) \
        or occurs(variable, term.argument)
  else:
    return variable == term




def eta_reducible(term):
  return isinstance(term, Abs) \
    and isinstance(term.body, App) \
    and term.body.argument == 0 \
    and not occurs(0, term.body.function)

def eta_reduce(term):
  return lift(term.body.function, -1)




def beta_reducible(term):
  return isinstance(term, App) \
    and isinstance(term.function, Abs)

def beta_reduce(term):
  return substitute(term.function.body, term.argument)






def reduce(term):
  if beta_reducible(term):
    return beta_reduce(term)
  elif eta_reducible(term):
    return eta_reduce(term)
  else:
    if isinstance(term, Abs):
      return Abs(reduce(term.body))
    elif isinstance(term, App):
      return App(reduce(term.function), reduce(term.argument))
    else:
      return term

def normalize(term, max_steps=None):
  if max_steps is None:
    while True:
      next_term = reduce(term)
      if next_term == term:
        return term
      term = next_term
  else:
    for step in range(max_steps):
      next_term = reduce(term)
      if next_term == term:
        return term
      term = next_term
    else:
      return None


def trace(term):
  while True:
    yield term
    term = reduce(term)





if __name__ == '__main__':
  K = Abs(Abs(1))
  S = Abs(Abs(Abs(App(App(2, 0), App(1, 0)))))
  I = App(App(S, K), K)
  ι = Abs(App(App(0, S), K))
  ω = App(App(S, I), I)
  ωω = App(ω, ω)
  Ω = App(ω, Abs(App(App(0, 0), 0)))

  assert normalize(App(ι, ι)) == normalize(I)
  assert normalize(App(ι, App(ι, App(ι, ι)))) == K
  assert normalize(App(ι, App(ι, App(ι, App(ι, ι))))) == S

  print('K = {}'.format(string(K)))
  print('S = {}'.format(string(S)))
  print('I = {} = {}'.format(string(I), string(normalize(I))))
  print('ι = {}'.format(string(ι)))
  print('ω = {} = {}'.format(string(ω), string(normalize(ω))))
  print('ωω = {} = {}'.format(string(ωω), string(normalize(ωω))))
  print('Ω = {}'.format(string(Ω)))

  while True:
    input(string(Ω))
    Ω = reduce(Ω)







