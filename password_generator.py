import random
import string

str_digit = string.ascii_letters
num_digit = string.digits
special_digit = '!@#$%&*.?:'


def password_generator(digits=8, wgt_str=1, wgt_else=2):
    space = str_digit + num_digit + special_digit
    needed = list(random.choice(string.ascii_uppercase) + random.choice(num_digit) + random.choice(special_digit))
    wgt = [wgt_str for i in range(52)] + [wgt_else for i in range(20)]
    password = random.choices(space, weights=wgt, k=digits - 3) + needed
    random.shuffle(password)
    password = "".join(password)
    return password


print(password_generator(digits=15))