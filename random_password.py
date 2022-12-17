#Ask user if they want to generate a password for 
#if yes, ask for length
#generate password and print  
#exit if answer is no 

import string 
import random 

characters = (string.ascii_letters + string.digits + "!@#$%^&*")

def generate_password():
  password_length = int(input("Enter password length: "))

  random.shuffle(characters)
  password = [] 

  for x in range(password_length):
    password.append(random.choice(characters))

  random.shuffle(password)

  password = "".join(password)
  print(password)
  
option = input(" Do you want to generate a password? (Yes/No")
if option == "Yes":
  generate_password()
elif option == "No":
  print("Program ended")
  quit()