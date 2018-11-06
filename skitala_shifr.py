import os,sys,math,enchant,numpy
d = enchant.Dict("en_US") #dictionary
#encoder=decoder
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

def encoder(string,m): 
	"""
	encode string with key (key must be integer) 
	use: numbers
	"""
	n,k=numbers(string,m)
	new_string=[' ']*k
	for i in range(k):
		new_string[int(math.fabs(m * (i % n)) + math.fabs(i // n))] = string[i]
	return ''.join(new_string)

def decoder(string,m):
	"""
	decode string with key (key must be integer) 
	"""
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
	d={}
	for i in range(mini,maxi):
		new_string = (decoder(string,i).split(' '))
		#print(new_string)
		flag = False
		for j in new_string:
			try:
				flag = d.check(j)
			except: 
				pass
		if flag: 
			print("Find!!!")
			return  ' '.join(new_string),i
			

if __name__=="__main__":
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
	if sys.argv[1]=='-e':	
		try:
			n = initial_n()
			print(encoder(string,n))
		except:
			print("Something wrong, try -h parameter")
	elif sys.argv[1]=='-d':
		try:
			n = initial_n()
			print(decoder(string,n))
		except:
			print("Something wrong, try -h parameter")
	elif sys.argv[1]=='-a':
		try:
			n = initial_n()
			m = initial_m()
			string,key=(attack(string,n,m))
			print("Key =",key)
			print("your string: ",string)
		except:
			print("Something wrong, try -h parameter")
	else:
		print(open("README.md",'r').read())
