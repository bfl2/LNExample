import json
import random
import os
import secrets
import string

def init_message():
    type = str(chr(16))
    messageDict = {"type":type} #{key:value,key:value...}
    parsed_json = json.dumps(messageDict)
    return parsed_json


def generate_byte_array_string(size):#in string format, to be decoded on the receiver
    bStr =''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return bStr

def open_channel_message():##campos sao passados como char
    type = str(chr(32)) ##convertendo os campos para char
    chain_hash = generate_byte_array_string(32)
    temporary_channel_id = generate_byte_array_string(32)
    funding_satoshis = generate_byte_array_string(8)
    messageDict = {"type": type,"chain_hash":chain_hash, "temporary_channel_id":temporary_channel_id,"funding_satoshis":funding_satoshis}
    parsed_json = json.dumps(messageDict)
    #aux = json.loads(parsed_json)
    #print (dict(aux))
    return parsed_json

def accept_channel_message():
    type = str(chr(33))
    temporary_channel_id = generate_byte_array_string(32)
    funding_pubkey = generate_byte_array_string(33)
    shutdown_len = chr(32)  # 0-255^2 #  usando um valor fixo qualquer # para gerar uma len aleatoria: generate_byte_array_string(2)
    shutdown_len_B = shutdown_len.encode()
    shutdown_len_int = int.from_bytes(shutdown_len_B, byteorder='little')
    shutdown_scriptpubkey = generate_byte_array_string(shutdown_len_int)
    messageDict = {"type": type, "temporary_channel_id": temporary_channel_id,
                   "funding_pubkey": funding_pubkey, "shutdown_len": shutdown_len,
                   "shutdown_scriptpubkey": shutdown_scriptpubkey}
    parsed_json = json.dumps(messageDict)
    #print(shutdown_len, shutdown_len_B, shutdown_len_int, shutdown_scriptpubkey)

    return

def main():


    return
main()
open_channel_message()
accept_channel_message()