# Project Euler 42 problem
# https://projecteuler.net/problem=42
#
# High level solution is as follows:
# Read the words from the file into a string list
# Map the string list into the corresponding word score
# Map the word score list into the corresponding N by 
#	inverting the equation
#Count the items which are natural numbers
#	(the others do not correspond to triangle words
#	as there isn't an N that satisfies the equation)
#
# Execute in Python 3. Not tested in 2!
#
# Tiago Almeida, 2016

def words_list():
	"""
	Return a strings list read from file input.txt  
	"""
	return ['sky']


def word_value_list( words_list ):
	"""
	Given a list of strings, maps
	to their score based on the following:
	By converting each letter in a word 
	to a number corresponding to its
	alphabetical position and adding these
	values we form a word value. 
	For example, the word value for SKY is
	19 + 11 + 25 = 55
	"""
	def upper_chars_list( word ): 
		# e.g.: 'abc' -> ['A','B','C']
		return list(word.upper())
	def numerical_chars_list( uchars_lst ):
		# e.g.: ['A','B','C'] -> [0, 1, 2]
		return map(lambda c: ord(c)-ord('A')+1, uchars_lst)
	def sum_list( int_list ):
		# e.g.: [0, 1, 2] -> 3
		import functools
		return functools.reduce(lambda x,y: x+y, int_list)
	return map(lambda word: sum_list(
								numerical_chars_list(
									upper_chars_list(word))), 
				words_list )


def solve_equation( word_value ):
	"""
	Solves the equation word_value = (1/2) * n(n+1)
	for n. This is done using the quadratic solution 
	formula.

	Let P = 2 * word_value 
	Then we have: 
	P = n (n+1) (=)
	0 = n^2 + n - P

	Which is easily solvable with a known formula. 
	It has 2 solutions and we return both in a list.
	"""
	import math
	P = 2 * word_value
	return [(-1 + math.sqrt(1+4*P))/2, 
			(-1 - math.sqrt(1+4*P))/2]



def has_real_solutions( solutions ):
	"""
	Given a list with 2 possible solutions for N,
	returns True if at least one of them is a natural
	number
	"""
	import functools 
	return functools.reduce(lambda x,y: x or y, 
							map(lambda x:x.is_integer(), 
								solutions))



def solution():
	"""
	High level solution is as follows:
	Read the words from the file into a string list
	Map the string list into the corresponding word score
	Map the word score list into the corresponding N by 
		inverting the equation
	Count the items which are natural numbers
		(the others do not correspond to triangle words
		as there isn't an N that satisfies the equation)
	"""
	from collections import Counter
	word_values = word_value_list( words_list() )
	solvables = map(lambda x: has_real_solutions(solve_equation(x)),
		word_values)
	# count Trues and Falses, return only number of True occurrences
	return Counter(solvables)[True]


if __name__ == '__main__':
	print( solution() )