def ft_filter(function_to_apply, list_of_inputs):
	if not hasattr(list_of_inputs, '__iter__'):
		raise TypeError("not a iterable input")
	new = []
	for elem in list_of_inputs:
		if function_to_apply(elem):
			new.append(elem)
	return new
