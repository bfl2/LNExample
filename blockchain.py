import random, string

HASH = None

def generate_byte_array_string(size):#in string format, to be decoded on the receiver
    bStr =''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return bStr

def init():
    HASH = generate_byte_array_string(32)
    return HASH