import random
import string

length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + "!@#$%^&*"

password = "".join(random.choice(chars) for i in range(length))
print("Generated Password:", password)
