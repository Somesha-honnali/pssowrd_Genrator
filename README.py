# pssowrd_Genrator
import random
lower = "abcdefghijklmnopqrsstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%&*({)[}"

all = lower+upper+numbers+symbols
length = 10
password = "".join(random.sample(all,length))
print(password)
