
#!Using match keyword
#?It's similar to switch statement 

name = input("What's your name? ")

match name:
    # case "Harry":
    #     print("Gryffindor")
    # case "Hermione":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    #? -> OR
    case "Harry" |  "Hermione" | "Ron":
        print("Gryffindor")
        
    case "Draco":
        print("Slytherin")
        
    case _:
        print("Not recognized")