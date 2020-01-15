def ft_reduce(function_to_apply, list_of_inputs):
	if not hasattr(list_of_inputs, '__iter__'):
		raise TypeError("not a iterable input")
	enum = list(list_of_inputs)
	for i, elem in enumerate(enum):
		if (i+1 < len(list_of_inputs)):
			enum[i+1] = function_to_apply(elem, enum[i+1])
	return enum[i]
