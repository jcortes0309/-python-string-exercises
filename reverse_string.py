string1 = raw_input("Provide a string to reverse ")
string2 = raw_input("Provide another string to reverse ")
# Based on information found in stack overflow - http://stackoverflow.com/questions/931092/reverse-a-string-in-python
# The first method works by using slice [begin:end:step] - This leaves the
# begin and end off and specifies a step of -1 and it reverses a string.

# First method for reversing a string
print "\n"
print "First string is: %s.  This string reversed is: %s" % (string1, (string1[::-1]))

# Second method for reversing a string
# reversed returns an instance of <type 'reversed'>, not a string
print "Second string is: %s.  This string reversed is: %s" % (string2, ("".join(reversed(string2))))
print "\n"
