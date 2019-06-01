

def binary(nono):  #converts decimal to binary
	bits_list=[]
	a=nono
	while(a>0):
		num=a
		b=int(num%2)
		bits_list.append(b)
		num=num//2
		a=int(a/2)
	#print(bits_list)
	if(nono<4):
		bits_list.append(0)
	bits_list.reverse()
	return bits_list;


def compliment(value):
	onecomp = []
	twocomp = []
	for i in range(0,len(value)):
		if value[i]==0:
			onecomp.append(1)
		elif value[i]==1:
			onecomp.append(0)
	
	carry=1
	for j in range(len(value)-1,-1,-1):
		
		if(onecomp[j]==0 and carry==1):
			twocomp.append(1)
			carry=0
		elif(onecomp[j]==1 and carry==1):
			twocomp.append(0)
			carry=1
		elif(onecomp[j]==0 and carry==0):
			twocomp.append(0)
			carry=0
		elif(onecomp[j]==1 and carry==0):
			twocomp.append(1)
			carry=0
	twocomp.reverse()
	return twocomp


def AssignSIgn(non,signbit):
	if(non<0):
		signbit.insert(0,0)
		signbit=compliment(signbit)
	else:
		signbit.insert(0,0)
	return signbit


def Add(valA,valM):
	add = []
	ad = valA
	carry = 0
	for i in range(len(ad)-1,-1,-1):
		if(valA[i]==0 and valM[i]==0 and carry==0):
			add.append(0)
			carry=0
		elif(valA[i]==0 and valM[i]==0 and carry==1):
			add.append(1)
			carry=0
		elif(valA[i]==0 and valM[i]==1 and carry==0):
			add.append(1)
			carry=0
		elif(valA[i]==0 and valM[i]==1 and carry==1):
			add.append(0)
			carry=1
		elif(valA[i]==1 and valM[i]==0 and carry==0):
			add.append(1)
			carry=0
		elif(valA[i]==1 and valM[i]==0 and carry==1):
			add.append(0)
			carry=1
		elif(valA[i]==1 and valM[i]==1 and carry==0):
			add.append(0)
			carry=1
		elif(valA[i]==1 and valM[i]==1 and carry==1):
			add.append(1)
			carry=1
	add.reverse()
	return add

def Shift(shiftA,shiftQ,shift_Qneg1):

	val=shiftA+shiftQ+shift_Qneg1
	l = len(val)
	#i=0
	'''while(i<l-1):
		val[i]=val[i+1]
		i=i+1
	val[i]=0
	return val
'''
	for i in range(l-2,-1,-1):
		#val[i]=0
		val[i+1]=val[i]
	#del val[i]
	val[0]=val[i]
	return val


def decimal(bin):
	bin.reverse()
	dec=0
	for i in range(0,len(bin)):
		if(bin[i]==1):
			dec=dec+(bin[i]*(2**i))
		elif(bin[i]==0):
			pass
	bin.reverse()
	return dec	



print("      BOOTH'S ALGORITHM     ")
print("")
multiplicand=int(input("Enter value of Multiplicand -> M : "))
multiplier=int(input("Enter value of Multiplier -> Q : "))
print("")
print("")

m=binary(abs(multiplicand))
q=binary(abs(multiplier))
print(*m)
print(*q)

print("Signed Values")
msign=AssignSIgn(multiplicand,m)
qsign=AssignSIgn(multiplier,q)


print(*msign)
print(*qsign)


ACC = []
for i in range(0,len(msign)):
	ACC.append(0)
print("A : ",*ACC)

qneg1=[0]
print("Q-1 : ",*qneg1)

negM = compliment(msign)
print("-M : ",*negM)
print("")

newA = ACC
newQ = qsign
rr=ACC+qsign
new_Qneg1 = qneg1
posM = msign



print("   A   ","    ","   Q   ","    ","   Q -1   ")

counter = len(msign)
while counter > 0:
	n=len(qsign)-1
	if(newQ[n]==0 and new_Qneg1[0]==1):
		newA = Add(newA,msign)
		a = Shift(newA,newQ,new_Qneg1)
	elif(newQ[n]==1 and new_Qneg1[0]==0):
		newA = Add(newA,negM)
		a = Shift(newA,newQ,new_Qneg1)
	elif(newQ[n]==0 and new_Qneg1[0]==0):
		a = Shift(newA,newQ,new_Qneg1)
	elif(newQ[n]==1 and new_Qneg1[0]==1):
		a = Shift(newA,newQ,new_Qneg1)


	
	#print(*a)
	print("")

	newA=a[0:len(ACC)]
	newQ=a[len(ACC):len(rr)]
	new_Qneg1=a[len(rr):]
	print(*newA,"    ",*newQ,"        ",*new_Qneg1)

	print("-------------------------------------------")

	counter=counter-1


result=newA+newQ
if(result[0]==1):
	result=compliment(result)
	finalans=decimal(result)
	print("Result : -",finalans)
elif(result[0]==0):
	finalans=decimal(result)
	print("Result : ",finalans)





