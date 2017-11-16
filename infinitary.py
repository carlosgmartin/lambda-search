from itertools import product
from collections import deque

def alternate(*iterables):
	iterators = deque(map(iter, iterables))
	while len(iterators) > 0:
		iterator = iterators.popleft()
		try:
			yield next(iterator)
			iterators.append(iterator)
		except StopIteration:
			pass

def union(indices, function):
	iterators = deque()
	for index in indices:
		iterators.append(iter(function(index)))

		iterator = iterators.popleft()
		try:
			yield next(iterator)
			iterators.append(iterator)
		except StopIteration:
			pass
			
	yield from alternate(*iterators)

def disjoint_union(indices, function):
	yield from union(indices, lambda index: map(lambda element: (index, element), function(index)))

def tuples(*iterables):
	iterators = deque(map(iter, iterables))
	buffers = tuple([] for iterator in iterators)
	indices = deque(range(len(iterators)))
	while len(indices) > 0:
		index = indices.popleft()
		try:
			element = next(iterators[index])
			yield from product(*buffers[:index] + ((element,),) + buffers[index+1:])
			buffers[index].append(element)
			indices.append(index)
		except StopIteration:
			pass
