#coding:utf8
import sys

def naive_gen(ascii):
	code = ''
	for x in ascii:
		code += '>' + '+' * ord(x) + '.'
	return code

def greedy_gen(ascii):
	current = []
	code = ''
	ptr = -1
	for x in ascii:
		if len(current) == 0:
			code += '+' * ord(x) + '.'
			ptr += 1
			current.append(x)
		else:
			min_dist = 256
			min_index = 0
			for (index, y) in zip(range(len(current)), current):
				if abs(ord(y)-ord(x)) < min_dist:
					min_dist, min_index = abs(ord(y)-ord(x)), index
			print "min_index",min_index,"min_dist", min_dist, "current",current
			if min_dist < ord('A'):
				print "case 1"
				if min_dist >= ord(x):
					ptr_delta = '+' * ( ord(current[min_index]) - ord(x) )
				else:
					ptr_delta = '-' * ( ord(x) - ord(current[min_index]) )

				if min_index >= ptr:
					ptr_move = '>' * ( min_index - ptr )
				else:
					ptr_move = '<' * ( ptr - min_index )

				code += ptr_move + ptr_delta + '.'
				print "((((",ptr_move + ptr_delta + '.'
				ptr = min_index
				current[min_index] = y
			else:
				print "case 2"
				code += '>' + '+' * ord(x) + '.'
				current.append(x)
				ptr = len(current) - 1
	return code
if __name__ == '__main__':
	ascii = raw_input()
	print greedy_gen(ascii)