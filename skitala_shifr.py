import os,sys,math,enchant,numpy
d = enchant.Dict("en_US") #dictionary
#encoder=decoder
def numbers(string,m):
	return int(math.fabs((len(string)-1) // m)) + 1,len(string)

def encoder(string,m): 
	n,k=numbers(string,m)
	new_string=[' ']*k
	for i in range(k):
		new_string[int(math.fabs(m * (i % n)) + math.fabs(i // n))] = string[i]
	return ''.join(new_string)

def decoder(string,m):
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
	
	
#attack,expecting 2 numbers	
def attack(string,mini,maxi):   
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
			
		
		#print(i,encoder(string,i),sep=': ')
if __name__=="__main__":
	if sys.argv[1]=='-e':
		
		try:
			print(encoder(sys.argv[2],int(sys.argv[3])))
		except:
			print("Something wrong, try -h parameter")
	elif sys.argv[1]=='-d':
		try:
			print(decoder(sys.argv[2],int(sys.argv[3])))
		except:
			print("Something wrong, try -h parameter")
	elif sys.argv[1]=='-a':
		try:
			string,key=(attack((sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])))
			print("Key =",key)
			print("your string: ",string)
		except:
			print("Something wrong, try -h parameter")
	else:
		print("USAGE:")
		print("      encoding: -e <string> <n>")
		print("      decoding: -d <string> <n>")
		print("      attack: -a <string> <minimum n> <maximum n>")