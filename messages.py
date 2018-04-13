import json
import random
import os
import secrets
import string

MAX_LENGTH = 65535

def init_message():
    type = str(chr(16))

    messageDict = {
        "type":type
        } #{key:value,key:value...}
        
    parsed_json = json.dumps(messageDict)
    return parsed_json

def generate_byte_array_string(size):#in string format, to be decoded on the receiver
    bStr =''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return bStr

def parse_message(data):
    return json.loads(data)

def open_channel_message(chain_hash, funding_satoshis):##campos sao passados como char
    type = str(chr(32)) ##convertendo os campos para char
    temporary_channel_id = generate_byte_array_string(32)

    messageDict = {
        "type": type,"chain_hash":chain_hash, 
        "temporary_channel_id":temporary_channel_id,
        "funding_satoshis":funding_satoshis
        }

    parsed_json = json.dumps(messageDict)
    #aux = json.loads(parsed_json)
    #print (dict(aux))
    return parsed_json

def accept_channel_message(temporary_channel_id): ##valores aleatorios por enquanto
    type = str(chr(33))
    funding_pubkey = "GsKAJGmwAbxJGM9qgJKJhc12L2k9P0E6Q"
    #funding_pubkey = generate_byte_array_string(33)
    shutdown_len = chr(32)  # 0-255^2 #  usando um valor fixo qualquer # para gerar uma len aleatoria: generate_byte_array_string(2)
    shutdown_len_B = shutdown_len.encode()
    shutdown_len_int = int.from_bytes(shutdown_len_B, byteorder='little')
    shutdown_scriptpubkey = "j7d8rmvjJquyRDVm5E9bofMRl3FLAk1s"
    #shutdown_scriptpubkey = generate_byte_array_string(shutdown_len_int)

    messageDict = {
        "type": type, 
        "temporary_channel_id": temporary_channel_id,
        "funding_pubkey": funding_pubkey,
        "shutdown_len": shutdown_len,
        "shutdown_scriptpubkey": shutdown_scriptpubkey
        }

    parsed_json = json.dumps(messageDict)
    #print(shutdown_len, shutdown_len_B, shutdown_len_int, shutdown_scriptpubkey)

    return parsed_json

def funding_created_message(): ##funding aleatorio por enquanto
    type = str(chr(34))
    temporary_channel_id = generate_byte_array_string(32)
    funding_txid = generate_byte_array_string(32)
    funding_output_index = generate_byte_array_string(2)
    signature = generate_byte_array_string(64)

    messageDict = {
        "type": type,
        "temporary_channel_id": temporary_channel_id,
        "funding_txid":funding_txid,
        "funding_output_index":funding_output_index,
        "signature":signature
        }

    parsed_json = json.dumps(messageDict)
    #print(parsed_json)
    return parsed_json

def funding_signed_message(channel_id, signature):
    type = chr(35)

    messageDict = {
        "type": type,
        "channel_id": channel_id,
        "signature": signature
        }

    parsed_json = json.dumps(messageDict)
    #print(parsed_json)
    return parsed_json

def funding_locked_message():
    type = chr(36)
    channel_id = generate_byte_array_string(32)

    messageDict = {
        "type": type,
        "channel_id": channel_id
        }

    parsed_json = json.dumps(messageDict)
    #print(parsed_json)
    return parsed_json

def shutdown_message():
    type = chr(38)
    channel_id = generate_byte_array_string(32)
    len = chr(32)  # 0-255^2 #  usando um valor fixo qualquer # para gerar uma len aleatoria: generate_byte_array_string(2)
    len_B = len.encode()
    len_int = int.from_bytes(len_B, byteorder='little')
    scriptpubkey = generate_byte_array_string(len_int)

    messageDict = {
        "type": type,
        "channel_id": channel_id,
        "len":len,
        "scriptpubkey":scriptpubkey
        }

    parsed_json = json.dumps(messageDict)
    #print(parsed_json)
    return parsed_json

def closing_signed_message():
    type = str(chr(39))
    channel_id = generate_byte_array_string(32)
    fee_satoshis = generate_byte_array_string(2)
    signature = generate_byte_array_string(64)

    messageDict = {
        "type": type,
        "channel_id": channel_id,
        "fee_satoshis": fee_satoshis,
        "signature": signature
        }

    parsed_json = json.dumps(messageDict)
    print(parsed_json)
    return parsed_json