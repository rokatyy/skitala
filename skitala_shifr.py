#!/usr/bin/python3
import os,sys
import math
import enchant
import numpy

#English dictionary
d = enchant.Dict("en_US") 
dict_most_common_words={}

def initial_n():
	"""
	returns parameter argv = '-n'
	"""
	return int(sys.argv[sys.argv.index('-n')+1])
def initial_m():
	"""
	returns parameter argv = '-m'
	"""
	return int(sys.argv[sys.argv.index('-m')+1])
def numbers(string,m):
	"""
	returns size of matrix and string length
	"""
	return int(math.fabs((len(string)-1) // m)) + 1,len(string)
def exception():
	"""
	exit in case incorrect input
	"""
	print("Something wrong, try -h parameter")
	exit(0)
def delete_indent(string):
	"""
	function that replaces indent to space
	"""
	return string.replace('\n',' ')
def find_max_in_dict(dictionary):
	"""
	returns max value from dictionary
	"""
	return max([dictionary[j] for j in [i for i in dictionary]])
def encoder(string,m): 
	"""
	encode string with key (key must be integer) 
	use: numbers
	"""
	string = delete_indent(string)
	n,k=numbers(string,m)
	new_string=[' ']*k
	for i in range(k):
		new_string[int(math.fabs(m * (i % n)) + math.fabs(i // n))] = string[i]
	return ''.join(new_string)
def decoder(string,m):
	"""
	decode string with key (key must be integer) 
	"""
	string = delete_indent(string)
	n,k=numbers(string,m)
	arr=[string[x:x+m] for x in range (0, k, m)]
	new_arr=[];	new_str=''
	for i in range(len(arr)):new_arr.append(list(arr[i]))
	for i in range(m):
		for j in range(n):
			try:
				new_str+=new_arr[j][i]
			except: pass
	return new_str


def attack(string,mini,maxi):   
	"""
	attack with using decode function (maxi-mini) times
	then check text with English dictionary and try to find the best variant
	"""
	print("Begin attack..")
	for i in range(mini,maxi):
		dict_most_common_words[i] = 0
		new_string = (decoder(string,i).split(' '))
		for j in new_string:
			try:
				if d.check(j):
					dict_most_common_words[i]+=1
			except: 
				pass
		find_max_in_dict(dict_most_common_words)
		return  ' '.join(new_string),i
			

if __name__=="__main__":
	"""
	it is really bad code but it works
	"""
	if len(sys.argv)<2:
		exception()
	
	if '-f' in sys.argv:
		try:
			string = open(sys.argv[sys.argv.index('-f')+1],'r').read()
		except:
			print("No file there")
			exit(0)
	else: 
		try:
			string = sys.argv[2]
		except: 
			pass
	try:
		if sys.argv[1]=='-e':
			n = initial_n()
			print(encoder(string,n))
		elif sys.argv[1]=='-d':
			n = initial_n()
			print(decoder(string,n))
		elif sys.argv[1]=='-a':
			n = initial_n()
			m = initial_m()
			new_string,key=(attack(string,n,m))
			print("Key =",key)
			print("your string: ",string)
	except:
		exception()
			
	if sys.argv=='-h':
		print(open("README.md",'r').read())