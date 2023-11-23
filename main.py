print("Hello, this is your program!\nYou can name me and make up mage, and I'll say hi to you :)")

user_name = input("What is my name?: ")
user_age = int(input("How old am I?: "))

def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old :)"

result_message = say_hi(user_name, user_age)
print(result_message)
