print("Hello World!")


# Variable : Container that store values-----------------------------------------------------------------
# Rules while creating variable names
# 1. Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.
# 2. You can’t use Python's reserved words, or "keywords," as variable names.
# 3. The pythonic way to name variables is to use all lowercase letters and underscores to separate words example :my_height = 58

# Datatype : string,integer,Float,boolean------------------------------------------------------------------------
x=12 #integer
y=13.34 #float
p="python" #String is immutable datatype we can declare them by using single or double quotes
b=False #bool type with store boolean value
print("this will result false even they seem to be equal but they are float in which 0.1 is more than 0.1 (.1+.1+.1==.3)",.1+.1+.1==.3)
# Type & typecasting (int(),float(),str())
decimalNum =float(4578)
print("decimalNum :",type(decimalNum))
integerNum =int(2344.4678)
print("integerNum :",type(integerNum))
# ---------------------------------------------Arithmetic Operators-------------------------------
Num1 =4.1
Num2 =5
print("Num1:",Num1,"Num2 :",Num2,"Num1+Num2",Num1+Num2)
print("Num1:",Num1,"Num2 :",Num2,"Num1-Num2",Num1-Num2)
print("Num1:",Num1,"Num2 :",Num2,"NUM1*Num2",Num1*Num2)   
print("Num1:",Num1,"Num2 :",Num2,"Num1/Num2",Num1/Num2)  # Divide and provide result in float
print("Num1:",Num1,"Num2 :",Num2,"Num1%Num2",Num1%Num2)  # Give Reminder
print("Num1:",Num1,"Num2 :",Num2,"Num1**Num2",Num1**Num2) # Exponentiation
print("Num1:,",Num1,"Num2 :",Num2,"Num1//Num2",Num1//Num2) # Divide and round off result

# Quiz1
# My electricity bills for the last three months have been $23, $32 and $64. What is the average monthly electricity bill over the three month period? Write an expression to calculate the mean, and use print() to view the result.
print("Average monthly electricity bill :",(23+32+64)/3)

# Quiz2
# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.
# How many tiles are needed?
# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
#Answere
print("tiles are needed :",(9*7)+(5*7))

# Fill this in with an expression that calculates how many tiles will be left over.
print("left over tiles:",(17*6)-((9*7)+(5*7)))



#-----------------------------------------------Assigment Operators-------------------------------------------------
x=1
print(x)
# x+=3 and x=x+3 are same similarly other =,+=,-=,*=,/=,%=//=,**=
x//=3
print(x)

# Quiz1
# Now it's your turn to work with variables. The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables. After each comment write a line of code that implements the instruction.

# Note that this code uses scientific notation(opens in a new tab) to define large numbers. 4.445e8 is equal to 4.445 *10* * 8 which is equal to 444500000.0.
# Answere based on questions
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
rainfall-=(rainfall/10)
# add the rainfall variable to the reservoir_volume variable
reservoir_volume+=rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume +=(reservoir_volume/20)
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -=(reservoir_volume/20)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -=2.5e5
# print the new value of the reservoir_volume variable
print("reservoir_volume :",reservoir_volume)

# Note: when we divide any number by 0 then python interpreter will give error "ZeroDivisionError: division by zero"
# There are two type of errors 1.Exceptions error :  2.syntax error
# An **Exception** is a problem that occurs when the code is running, but a 'Syntax Error' is a problem detected when Python checks the code before it runs it

# ---------------------------------------------------------Comparision Operator--------------------------------------------------
# Comparision (==,>=,<=,>,<,!=) will always give bool as result.
print(23>45)
print(23>=45)
print(56<656)
print(56<=656)
print(23==34)
print(23==23.0)
print(34!=35)

# ---------------------------------------------------------Logical Operator--------------------------------------------------
# Logical (and, or, not)
print(True and False)  #if all provided statements are True
print(True or False)   #if at least one of many statements is True
print(not(False))      #Flips the Bool Value

# Strings is immutable as we cannot change original string we can create new string from old one.
# 1. we use "+" sign to cancatenate string and "*" to repeat String
# 2. Escape Sequence : \t,\n ,\',\" 
# 3. Python uses 0 indexing 
print("Hello python"+"welcome to my IDE")
print("learn","learn2")
print("learn "*4)
# len(StrVariable) is build in function of string  to calculate length of string.it only work for sequence
print(len("HelloWorld From Python")) 
Namestr ="Python Programming"
print(Namestr[2])
# Operators  : =,>,<,or etc
# Function  : len(),print(),str() etc
# Methods :methods are function that belong to an object.Methods actually are functions that are called using dot notation.
# Example : sample_string.lower(),sample_string.title(),sample_string.count("i"),my_string.find('a')
# One important string method: format()
print("Mohammed has {} balloons".format(27))
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
# f string in python
citypopulation =32456
print(f"hello {citypopulation} people")
# Another important string method: split()
# This function or method returns a data container called a list that contains the words from the input string.
# The split method has two additional arguments (sep and maxsplit). The sep argument stands for "separator".the default separator is whitespace.
# the maxsplit argument provides the maximum number of splits. The argument gives maxsplit + 1 number of elements in the new list,
paragraph ="This function or method returns a data container called a list that"
print(paragraph.split(" ",3))
# to find last occurance print(my_string.rfind(substring))

# -------------------------------------------------Bitwise Operator--------------------------------------------------------------------
 
# Bitwise operators in Python operate on binary representations of integers. They perform operations bit by bit, meaning they apply logical operations to each corresponding bit of two numbers
# 1. Bitwise AND (&)
# Performs a logical AND operation on each bit of two numbers.
# A bit is 1 only if both corresponding bits are 1.
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b
print(result)  # Output: 1 (Binary: 0001)
# 2. Bitwise OR (|)
# Performs a logical OR operation on each bit of two numbers.
# A bit is 1 if at least one of the corresponding bits is 1.
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a | b
print(result)  # Output: 7 (Binary: 0111)
# 3. Bitwise XOR (^)
# Performs a logical XOR operation on each bit of two numbers.
# A bit is 1 if the corresponding bits are different.
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a ^ b
print(result)  # Output: 6 (Binary: 0110)
# 4. Bitwise NOT (~)
# Inverts all the bits of a number.(give 2's complement of real answere number)
# Trick to Equivalent is -(n+1) in Python (two's complement representation).
a=9;
print(~a); # -10
# 5. Left Shift (<<)
# Shifts the bits of the number to the left by a specified number of positions.
# Adds 0 bits on the right. 
# we gain bits in left shift.
# Trick to Equivalent is x<<n then answer will be x*2^n
a = 5  # Binary: 0101
result = a << 2
print(result)  # Output: 20 (Binary: 10100)
# 6. Right Shift (>>)
# Shifts the bits of the number to the right by a specified number of positions.
# Drops bits on the right. For positive numbers, 0 bits are added on the left.
# we lose bits on left shift.
# Trick to Equivalent is x<<n then answer will be x/2^n
a = 5  # Binary: 0101
result = a >> 2
print(result)  # Output: 1 (Binary: 0001)

         