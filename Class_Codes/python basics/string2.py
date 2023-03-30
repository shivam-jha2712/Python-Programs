# To print a string like C:\Users\temp\new.pdf
print("C:\\Users\\temp\\new.pdf")
# To avoide the escape sequences wala issue what we do is we add another back slash to remove the problem.

# The problem of these can also be solved by adding a r in front of it and making it as a raw string.
print(r"C:\Users\temp\new.pdf")

# \n \t - Escape Sequences
# \a - was used to create a bell sound in python - now it is obselete

# \v - vertical tab -Obsolete
# \f - feed format - Obsolete

# But to print the data using the octal values we can use
# \ooo
print("\110\145\154\154\157")

# for hexadecimal, it will be
# \xhh that is x followed by two digits
print("\x48\x65\x6c\x6c\x6f")

# \b - backspace
#  The work of \b is the same as backspace
print("Hello \b\b\b\b World")

# \r - carriage return
# Whereas the work of \r is to return to the very first part as the placeholder and the rest of the elements are printed
print("Hello \r World")