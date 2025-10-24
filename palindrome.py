def palindrome_checker():
    pal = input("Enter the string : ")
    cleanpal = pal.replace(" ","")
    cleanpal = cleanpal.lower()
    reversedpal = cleanpal[::-1]
    if reversedpal == cleanpal:
        print(f"{pal} is a palindrome")
    else:
        print(f"{pal} is not a palindrome")

palindrome_checker()