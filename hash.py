import hashlib
import random

def create_hash(password):
    password_hash = hashlib.sha512(password.encode()).hexdigest()
    return password_hash

def verify_hash(password, stored_password_hash):
    password_hash = hashlib.sha512(password.encode()).hexdigest()
    if password_hash == stored_password_hash:
        return True
    return False

def generate_password():
    password = []
    pass_len = random.randint(8, 31)
    num = "0123456789"
    low_alp = "abcdefghijklmnopqrstuvwxyz"
    upp_alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spec_char = r"!@#$%^&*_-+=:;<>?/.,"

    for i in range(pass_len):
        r = random.randint(1, 4)
        if r == 1:
            password.append(num[random.randint(0, len(num) - 1)])
        elif r == 2:
            password.append(low_alp[random.randint(0, len(low_alp) - 1)])
        elif r == 3:
            password.append(upp_alp[random.randint(0, len(upp_alp) - 1)])
        else:
            password.append(spec_char[random.randint(0, len(spec_char) - 1)])

    return "".join(password[::-1])

# Example usage:
# person1_password = generate_password()
# person1_hashed_password = create_hash(person1_password)
# person2_password = generate_password()
# person2_hashed_password = create_hash(person2_password)
