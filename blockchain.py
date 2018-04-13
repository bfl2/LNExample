import random, string

HASH = 'u09oU1E2qMLP8stTTlrCT8GrQaq69zLQ'

def generate_byte_array_string(size):#in string format, to be decoded on the receiver
    bStr =''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return bStr

def hash_depth(hash):
    return random.randint(4,10)

def init():
    return HASH