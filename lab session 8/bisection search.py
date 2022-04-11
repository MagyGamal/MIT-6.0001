low=int(input("please enter the lowest bounder: "))
high=int(input("please enter the highest bounder: "))

while low != high:
    mid = (high+low)/2
    print("the new mid is :" , mid)
    guess = int(input("Is your guess smaller, bigger, or equal to the new mid? (1) smaller (2) bigger (3) equal: "))
    if guess == 1:
        high = mid
    elif guess == 2:
        low = mid     
    elif guess == 3:
        print("your guess is:" , mid)
        break
    else:
        print("invalid entry")
        