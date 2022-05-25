from random import randint

name = input("Hi! What is your name? ")

# Guess 1

guesses = range(1, 6)
for x in guesses:
    month_number = randint(1, 12)
    year_number = randint(1924, 2004)

    print("Guess", x,":", name, "were you born in", month_number, "/", year_number, "?")
    response = input("yes or no? ")
    if response == "yes":
        print("I knew it!")
        exit()
    elif x == 5:
            print("I have other things to do. Good bye.")    
            exit()
    else: 
            print("Drat! Lemme try again!") 
        
            
