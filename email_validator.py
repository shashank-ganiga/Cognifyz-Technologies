#Task: Email Validator
#   Develop a Python function that validates whether a given string is a valid email address. 
#   Implement checks for the format, including the presence of an "@" symbol and a domain name

import re
inputemail = input("Enter the email : ")

def emailvalidator(inputemail):
    pattern = r"^[a-zA-Z0-9._\-+%]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$"
    match = re.fullmatch(pattern,inputemail)
    if match:
        print(f"{inputemail} is a valid email")
    else:
        print(f"{inputemail} is not a valid email")

emailvalidator(inputemail)