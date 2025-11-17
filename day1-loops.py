#------------------------------------------------Loops-----------------------------------------------------------#
# i=3
#!while i != 0 :
#     print("Meow")
#     i=i-1

# while True:
#     n=int(input("Enter a number"))
#     if n>0:
#         break

#!For loop
# for i in range(10):
#     print(f"{i}-> meow")
    
# for _ in range(10):
#     print(" meow")

#!Printing meow multiple times using function

def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n=int(input("Enter a positive number:"))
        if n>0:
            return n
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main()