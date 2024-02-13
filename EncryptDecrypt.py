from cryptography.fernet import Fernet

# Global variables
user_key = None

# Functions
def generate_key():
    global user_key
    user_key = Fernet.generate_key()

def get_key():
    global user_key
    if user_key is not None:
        return user_key
    
def destroy_key():
    global user_key
    if user_key is not None:
        user_key = None

def encrypt(string, key):
    if key is not None:
        string_bytes = bytes(string, 'utf-8')
        return Fernet(key).encrypt(string_bytes)
    
def decrypt(string_byte, key):
    if key is not None:
        string = Fernet(key).decrypt(string_byte).decode()
        return string
