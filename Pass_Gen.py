import string
import random

alpha = string.ascii_letters + string.ascii_lowercase+ string.ascii_uppercase + string.digits
pass_len = int(input("Enter password length: "))
password =''
for x in range(pass_len):
  password += ''.join(random.choice(alpha))

print(password)