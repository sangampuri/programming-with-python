
#!Exception handeling 
#?Exercise 1
# try:
#     x=int(input("Enter a number:"))
    
# except ValueError:
#     print("Please enter an integer")
    
# else:
#     print(f"The number is {x}")

#?Exercise 2
# while True:
#     try:
#         x=int(input("What's x?"))
#     except ValueError:
#         print("x is not a number")
#     else:
#         break
# print(f"X is {x}")


#?Exercise 3

def main():
    x=get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x=int(input("What's x?"))
            return x

        except ValueError:
            pass
                           
main()