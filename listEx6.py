
def sum_of_squares(xs):
	theSquare = []
	for j in xs:
	    new_list = j ** 2
		theSquare.append(new_list)
	return theSquare

print(sum_of_squares([2,3,4]))