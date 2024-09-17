import random
import string 
def create_password(length):
    characters=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
    if length<8:
        print("password length must be greater than 8")
        return None
    else:
         password = ''.join(random.choice(characters) for i in range(length))
    return password
length=int(input("Enter the length of password you need : "))
print("Generated password is : ",create_password(length))