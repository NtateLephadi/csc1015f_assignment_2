print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answer = input("Did anyone see you? (yes/no)\n")
if answer == "no":
    answer = input("Was is sticky? (yes/no)\n")
    if answer == "no":
        answer = input("Is it an Emausaurus? (yes/no)\n")
        if answer == "no":
            answer = input("Did the cat lick it? (yes/no) \n")
            if answer == "no":
                print("Decision: Eat it.")
            else:
                answer = input("Is your cat healthy? (yes/no)\n")
                if answer == "no":
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it")
        else:
            answer = input("Are you a Megalosaurus? (yes/no)\n")
            if answer == "no":
                print("Decision: Don't eat it")
            else:
                print("Decision: Eat it")
    else:
        answer = input("Is it a raw steak? (yes/no)\n")
        if answer == "no":
            answer = input("Did the cat lick it? (yes/no) \n")
            if answer == "no":
                print("Decision: Eat it.")
            else:
                answer = input("Is your cat healthy? (yes/no)\n")
                if answer == "no":
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            answer = input("Are you a puma? (yes/no)\n")
            if answer == "no":
                print("Decision: Don't eat it.")
            else:
                print("Decision: Eat it.")
else:
    answer = input("Was it a boss/lover/parent? (yes/no)\n")
    if answer == "no":
        print("Decision: Eat it.")
    else:
        answer = input("Was it expensive? (yes/no)\n")
        if answer == "no":
            answer = input("Was it chocolate? (yes/no)\n")
            if answer == "no":
                print("Decision: Eat it.")
            else:
                print("Decision: Eat it.")
        else:
            answer = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if answer == "no":
                print("Decision: Your call.")
            else:
                print("Decision: Eat it.")