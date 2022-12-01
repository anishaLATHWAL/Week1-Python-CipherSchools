winning_num = 3
guess_num = int(input("Enter any number between 1 and 10: "))
if guess_num==winning_num:
    print("You win ")
else:
    if guess_num < winning_num:
        print("low num")
    else:
        print("high num ")