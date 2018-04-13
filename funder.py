import socket
import blockchain

from messages import *

SOCK = None

def execute():
    blockchain.init()
    print("Funder executed.\nInsert host IP:")
    ip = input()
    print("Stabilising connection...", end='')
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.connect((ip, 9735))
    print(" Ready!")

    #send init message
    SOCK.send(init_message())

    #receive init message
    data = SOCK.recv(MAX_LENGTH)
    data = parse_message(data)

    funding_satoshis = generate_byte_array_string(8)

    #ask to open a channel
    SOCK.send(open_channel_message(
        blockchain.HASH,
        funding_satoshis
    ))
    #Receiving accept_channel message
    data = SOCK.recv(MAX_LENGTH)
    data = parse_message(data)
    #Sending funding_created message
    SOCK.send(funding_created_message())
    #receiving funding_signed message
    data = SOCK.recv(MAX_LENGTH)
    data = parse_message(data)
    channel_id = data["channel_id"]
    #sending funding_locked message
    SOCK.send(funding_locked_message(channel_id))
    #receiving funding_locked message
    data = SOCK.recv(MAX_LENGTH)
    data = parse_message(data)
    print(" closed")