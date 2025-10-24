#Task: String Reversal
#   Create a Python function that takes string as input and returns the reverse ofthat string.

#using slice method
inputstring = input("Enter your string : ")
reversedstring = inputstring[::-1]
print("Reversed Stirng : ",reversedstring)

#using reversed() method
inputstring1 = input("Enter your string : ")
reversedstring1 = "".join(reversed(inputstring1))
print("Reversed Stirng is : ",reversedstring1)