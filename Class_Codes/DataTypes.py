# Numeric DataTypes : 1.int, 2.float, 3.complex
# 1. int:
#       a. it has no upper or lower limit in terms of size in python only depends upon computer memory
#       b. it can contain any number that is not decimal (i.e; Decimals, Binary, Octal, HexaDecimal)
# Examples in code:
print(type(10))
print(type(0b10)) # this is binary (binary prefix is 0b or 0B)
print(type(0o16)) # this is octal (octal prefix is 0o or 0O)
print(type(0x69)) # this is hexadecimal (hexadecimal prefix is 0x or 0X)

# 2. float:
#           a. it contains all the decimal values and any kind of decimal values
#           b. unlike to int in python, float has limit of 308 decimal places to the right in a 64 bit system
#           c. int operations are faster than that of float
#           d. Also in python, for float there even exists a lower limit as well and that is 2.225e-308 which is 308 decimals to the right
#           e. Also anything more than that of upper limit of float in python is inferred by string "inf" - infinity
# Examples in code:
print(type(10.75))
print(type(1.76e307))
print(1.85e308) # exceeds the boundary limit of maximum float thus "inf"



