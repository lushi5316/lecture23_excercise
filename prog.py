import random

def num_vowels(str):
	a = ['a', 'o', 'e', 'u', 'i']
	num = 0
	for s in str:
		if s in a:
			num += 1

	return num
