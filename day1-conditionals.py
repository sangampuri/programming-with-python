
#!if statement
# x = int(input("What's x?"))
# y = int(input("What's y?"))

# if x<y :
#     print("X is less than y")

# if x>y :
#     print("X is greater than y")

# if x==y:
#     print("X is equal to y")



# x = int(input("What's x?"))
# y = int(input("What's y?"))

# if x<y :
#      print("X is less than y")

# elif x>y :
#      print("X is greater than y")

# else:
#      print("X is equal to y")



# x = int(input("What's x?"))
# y = int(input("What's y?"))

# if x==y:
#     print("X is equal to y")

# else:
#     print("X is not equal to y")


#!  and operator

# score = int(input("Score:"))
# if score>=90  and score <= 100:
#     print("Grade A")

# elif score >=80  and  score<90:
#     print("Grade B")

# elif score>=70  and  score<80:
#     print("Grade C")

# elif score >=60  and  score <70:
#     print("Grade D")

# else:
#     print(("Grade F"))

# score = int(input("Score:"))
# if 90<=score<= 100:
#     print("Grade A")

# elif 80<=score<90:
#     print("Grade B")

# elif 70<=score<80:
#     print("Grade C")

# elif 60<=score<70:
#     print("Grade D")

# else:
#     print(("Grade F"))

   
# score = int(input("Score:"))
# if score>=90:
#     print("Grade A")

# elif score>=80:
#     print("Grade B")

# elif score>=70:
#     print("Grade C")

# elif score>=60:
#     print("Grade D")

# else:
#     print(("Grade F"))

#!Odd or Even program
def main():
   x= int(input("Enter a number: "))
   if is_even(x):
      print("Even")
   else:
    print("Odd")
    
def is_even(x):
   return x % 2 == 0
   
main()