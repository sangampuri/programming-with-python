# print("Hello, World!")

#!Taking input from users
# name=input("What is your name:")
# print(f"My name is {name}")
# print("My name is", name)

#Learn about parameters inside print->end="\n",sep=' '
#!end
# print("Hello" ,end=" ")
# print("world!")
#!sep
# name="sangam"
# print("My name is",name, sep='???')

#!strip() -> Removes the mentioned things from left and right , by default removes spaces
# name=input("What is your name:")
# name=name.strip()
#name=name.title() #*Capitalizes every words starting letter
#OR name= name.strip().title()
# print(f"My name is {name}")

#!split() spliting a persons name into first and last name
name="sangam puri"
first_name,last_name=name.split("")
print(last_name)
