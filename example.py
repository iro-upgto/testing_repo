from string import ascii_letters,digits
from random import choice
import os

def generacad(ncad,kcar):
	return ["".join([choice(ascii_letters+digits) for k in range(kcar)]) for n in range(ncad)]

def p(x):
	print(x)
	
if __name__=='__main__':
	[p(x) for x in generacad(10,50)]
