# asks for how many times a player wants to play
def count():
    a = input("How many times would you like to play?? --> ")
    if a.isnumeric() == True and int(a) > 0:
        return int(a)
    elif a.startswith("exit"):
        exit()
    else:
        print("\nKindly choose only positive integers above 0")
        count()

t = count()    # Why does it return 'None' instead of the correct value from the second input??
print("you will play for %s times" % t)

