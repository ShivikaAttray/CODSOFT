import random
chars = "abc123$@"
length = int(input("Enter password length: "))
password = ""
for i in range(length):
    password += random.choice(chars)
print("Password:", password)
