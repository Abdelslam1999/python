name = input("Type your name: ")
print("Welcome", name, "to your mysterious destiny!")

answer = input("You have a choice to make and it's either left or right that will determine your destiny, choose wisely? (left/right) ").lower()

if answer == "left":
    answer = input(
        "You're a villain, you have two choices steal or redeem your reputation. What do you choose? (steal/redeem) ").lower()

    if answer == "steal":
        print("You have been caught by a hero and you lost the game .")
    elif answer == "redeem":
        print("you have gained the society's trust and you win!")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You're a hero, you have two choices fly or swim? (fly/swim) ")

    if answer == "swim":
        print("water is your weakness and is fatal element to you and you lost? ")
    else: 
        answer == "fly"
        answer = input("You have discovered your true identity and you're own your way to defeat the villain! choose kill/prison: ")

if answer == "prison":
    answer = input("The villain escaped the prison and is now on the run and you lost")
elif answer == "kill":
        print("you have freed the world from the horror of the villain and you win!")
    
else:
        print('Not a valid option. You lose.')
    

print("Thank you for trying", name)