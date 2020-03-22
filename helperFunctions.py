def binary_to_decimal(binaryNumber):
	return int(str(binaryNumber),2)

def decimal_to_binary(decimalNumber,flag):
    binary=str(bin(decimalNumber))
    if flag==True:
    	return "0"+binary[2:]
    return binary[2:]


def decimal_to_binary_padded(decimalNumber,padding,flag):
	binary=decimal_to_binary(decimalNumber,flag)
	binary=((padding-len(binary))*'0')+binary
	return binary

def invert_bits(binaryNumber):
	invertedBinary=""
	for i in binaryNumber:
		if i=='1':
			invertedBinary+="0"
		else:
			invertedBinary+="1"
	return invertedBinary

def pad_binary_number(binaryNumber,length):
    binaryNumber=("0"*(length-len(binaryNumber)))+binaryNumber
    return binaryNumber

def addition_binary(binaryNumber1,binaryNumber2):
    sumBinary=str(bin(int(binaryNumber1,2) + int(binaryNumber2,2)))[2:]
    length=max(len(binaryNumber1),len(binaryNumber2))
    sumBinary=pad_binary_number(sumBinary,length)
    length=len(sumBinary)-length
    return sumBinary[length:]

def twos_complement(binaryNumber):
	binaryNumber=invert_bits(binaryNumber)
	return addition_binary(binaryNumber,'1')

def arithmetic_right_shift(A,Q,Qo):
	temp=A+Q+Qo
	ans=temp[0]
	for i in range(0,len(temp)-1):
		ans+=temp[i]
	return ans[0:len(A)],ans[len(A):len(Q)+len(A)],ans[-1]

def arithmetic_left_shift_partial(A,Q):
	temp=A+Q
	return temp[1:len(A)+1],temp[len(A)+1:]+"?"