print('I am "Loving" it')
print("I am 'Loving' it")

# How to concatenate and take input
# It is important to note that input in python by default is of type string
variable = "Your name is:"
name = input("Enter your name: ")

print(variable + " " + name)
# Space is provided in the output of the above code and no space is there in the output of the below code
print(variable + name)

# \n gives a new line
string1 = "I am a \n string \n in multiple lines"
print(string1)

# \t gives a tab space
string2 = "1. Oil \t 2. Flour \t 3. Eggs \t 4. Oven\n"
print(string2)

print("Donald Trump said \"It's going to be huge\"")
print('Donald Trump said "It\'s going to be huge')
# Triple inverted commas neglect all other commas in between and removes usage of "\"
print("""Donald Trump said "It's going to be huge""")

string3 = """ I am a string
which is spanning over
multiple lines"""
print(string3)

#  Here the usage of \ has enables us to remove the spanning of a single string throughout diffrent lines
string4 = """ I am a string \
which is spanning over \
multiple lines\n"""
print(string4)

