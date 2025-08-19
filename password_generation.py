#1-import string module (to_get_the component of password[letters and digits])
import string
import random
#2-store it in variables.
capital_letters=list(string.ascii_uppercase)
small_letters=list(string.ascii_lowercase)
numbers=list(string.digits)
punctuations=list(string.punctuation)
#3-take the length of password from user.
password_length=input("what is the length of password would you want to create it: ")
#4-handle the input errors(try-except)
while True:
    try:
        password_length=int(password_length)
        if password_length <6:
            print("Enter 6 or more for making a strong password")
            password_length=input("please enter the number again: ")
        else:
            break
    except:
        print("please enter numbers only.")
        password_length=input("what is the length of password would you want to create it: ")
#5-make sure the number of character is more than 6(strong password)
#6-shuffle all lists
random.shuffle(capital_letters) #30%
random.shuffle(small_letters) #30%
random.shuffle(numbers) #20%
random.shuffle(punctuations) #20%
part1= round(password_length * 30/100)
part2=round(password_length*20/100)
#7-generate the password with 60%letters,20%digits and 20% punctuations.
password=[]
for i in range(part1):
    password.append(capital_letters[i])
    password.append(small_letters[i])
for i in range(part2):
    password.append(punctuations[i])
    password.append(numbers[i])
random.shuffle(password)   
password="".join(password)
print(f"your password is : {password}")