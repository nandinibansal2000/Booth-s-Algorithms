from helperFunctions import *
number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))
padding = max(len(decimal_to_binary(abs(number1),True)),len(decimal_to_binary(abs(number2),True)))
multiplicand = decimal_to_binary_padded(abs(number1),padding,True)
multiplicandCompliment = multiplicand
multiplier = decimal_to_binary_padded(abs(number2),padding,True)
if number1<0:
    multiplicand = twos_complement(multiplicand)
else:
    multiplicandCompliment = twos_complement(multiplicand)
if number2<0:
    multiplier = twos_complement(multiplier)

tracingTable = {"n":padding, "A":"0"*padding, "qo":"0", "Q": multiplier, "q1": multiplier[-1]}
while tracingTable["n"]>0:
    q1qo = tracingTable["q1"]+tracingTable["qo"]
    if q1qo=="10":
      
        tracingTable["A"] = addition_binary(tracingTable["A"],multiplicandCompliment)
       
    elif q1qo=="01":
        tracingTable["A"] = addition_binary(tracingTable["A"],multiplicand)
   
    tracingTable["A"],tracingTable["Q"],tracingTable["qo"] = arithmetic_right_shift(tracingTable["A"],tracingTable["Q"],tracingTable["qo"])
  
    tracingTable["q1"] = tracingTable["Q"][-1]
    tracingTable["n"]-=1

answer = tracingTable["A"]+tracingTable["Q"]
answerSign = tracingTable["A"][0]
answerCompliment = answer
decimalAnswer = binary_to_decimal(answer)
if answerSign=="1":
    answerCompliment = twos_complement(answer)
    decimalAnswer = binary_to_decimal(answerCompliment)*-1

print("Product in Decimal Representation: ", decimalAnswer)
print("Product in Binary Representation: ", answer)
print("2's Compliment of Product in Binary Representation: ", answerCompliment)

    
