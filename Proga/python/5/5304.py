def only_positive_even_sum(x, y):
	if not isinstance(x, int) or not isinstance(y, int):
		raise TypeError()

	if x < 0 or x % 2 != 0 or y < 0 or y % 2 != 0:
		raise ValueError()

	return x + y