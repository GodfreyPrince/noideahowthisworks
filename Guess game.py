# Total newbie at python
# How lousy is this? Please comment with how you'll code this better. Want to see beautiful code!
print("This is a word guessing game")
secret = "none"
i = 0
while i < 3:
    guess = input("Enter your guess: ")
    if guess == secret:
        print("You win!")
        i += 4
    else:
        i += 1
        if i < 3:
            print("Try again")

if i == 3:
 print("you lose")



