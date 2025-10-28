import random
genarated_number = random.randint(1,100)

while True:
    guess = int(input("Guess the number : "))
    
    if guess == genarated_number:
        print(f"Your guessed number is correct : {genarated_number} ")
        break
    elif guess > genarated_number:
        print("Too high!!!!")
    else :
        print("Too low!!!!")