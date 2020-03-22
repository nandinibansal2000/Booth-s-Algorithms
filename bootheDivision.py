from helperFunctions import *
number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))
if(number2 == 0):
	print("Division by Zero Error")
else:
	padding = max(len(decimal_to_binary(abs(number1),False)),len(decimal_to_binary(abs(number2),False)))
	dividend = decimal_to_binary_padded(abs(number1),padding,False)
	divisor = decimal_to_binary_padded(abs(number2),padding+1,False)
	divisorCompliment = twos_complement(divisor)
	Rq = 0
	Rp = 0
	if (number1*number2) < 0:
		Rq = 1
	if(number1 < 0 and number2 < 0):
		Rp = 1

	tracingTable = {"count":padding, "A":"0"*(padding+1),  "Q": dividend, "M": divisor, "M_":divisorCompliment,"b_n-1":"0"}
	
	while tracingTable["count"] > 0:

		if(tracingTable["b_n-1"] == "1"):
			tracingTable["A"],tracingTable["Q"] = arithmetic_left_shift_partial(tracingTable["A"],tracingTable["Q"])
			tracingTable["A"] = addition_binary(tracingTable["A"],tracingTable["M"])

		else:
			tracingTable["A"],tracingTable["Q"] = arithmetic_left_shift_partial(tracingTable["A"],tracingTable["Q"])
			tracingTable["A"] = addition_binary(tracingTable["A"],tracingTable["M_"])

		tracingTable["b_n-1"] = tracingTable["A"][0]
		
		if(tracingTable["b_n-1"] == "0"):
			
			tracingTable["Q"] = tracingTable["Q"][:-1]+"1"
			
		else:
			tracingTable["Q"] = tracingTable["Q"][:-1]+"0"
		
		tracingTable["count"] -= 1

	if(tracingTable["b_n-1"] == "1"):
		tracingTable["A"] = addition_binary(tracingTable["A"],tracingTable["M"])
	decimalQuotient = binary_to_decimal(tracingTable["Q"])
	decimalRemainder = binary_to_decimal(tracingTable["A"])
	binaryQuotientCompliment = tracingTable["Q"]

	if Rq == 1:
		tracingTable["Q"] = twos_complement(tracingTable["Q"])
		decimalQuotient = (-1) * decimalQuotient
		
		tracingTable["A"] =  twos_complement(tracingTable["A"])
		decimalRemainder = (-1) * decimalRemainder
	if Rp == 1:
		
		tracingTable["A"] =  twos_complement(tracingTable["A"])
		decimalRemainder = (-1) * decimalRemainder


	binaryQuotient = tracingTable["Q"]
	binaryRemainder = tracingTable["A"]
	print("Quotient in Decimal Representation: ",decimalQuotient)
	print("Quotient in Binary Representation: ",binaryQuotient)
	print("2's compliment of Quotient in Binary Representation: "+ binaryQuotientCompliment)
	print("Remainder in Decimal Representation: ",decimalRemainder)
	print("Remainder in Binary Representation: ",binaryRemainder)
