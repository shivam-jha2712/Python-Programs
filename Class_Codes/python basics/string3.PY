#          012345678901234     
string1 = "Prepinsta Prime"

# Directly printing the string
print(string1)

# Since indexing is relevant in python string thus we can use for loop to print the data 
for i in string1:
    print(i)
print()
# If you wish to print "Pit Pie" using indexing
# You can do it in two ways 
# 1. Positive indexing from  0 to  n
# 2. Negative Indexing from -1 to -n-1 

# Positive Indexing
print(string1[0 - 15])
print(string1[4 - 15])
print(string1[7 - 15])
print()
print(string1[10 - 15])
print(string1[12 - 15])
print(string1[14 - 15])
print()


# Negative Indexing
print(string1[-15])
print(string1[-11])
print(string1[-8])
print()
print(string1[-5])
print(string1[-3])
print(string1[-1])