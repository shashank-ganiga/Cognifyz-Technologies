import random
start_range = int(input("Enter your starting range : "))
end_range = int(input("Enter your ending range : "))

generate = random.randint(start_range,end_range)

attempt = 0

while True:
    attempt+=1
    guess = int(input("Guess the number : "))

    if guess > generate :
        print("Too High !!!")
    elif guess < generate : 
        print("Too Low !!!")
    else :
        print(f"Congrats you guessed it correctly in {attempt} attempts.")
        break