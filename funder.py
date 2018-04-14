import socket
import blockchain

from messages import *

FUNDEE_SOCKET = None
SIGNATURE = generate_byte_array_string(64)

def execute():
    blockchain.init()
    print("Funder executed.\nInsert host IP:")
    ip = input()
    print("Stabilising connection...", end='')
    FUNDEE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    FUNDEE_SOCKET.connect((ip, 9735))
    print(" Ready!")

    #send init message
    FUNDEE_SOCKET.send(init_message())

    #receive init message
    data = FUNDEE_SOCKET.recv(MAX_LENGTH)
    data = parse_message(data)

    funding_satoshis = generate_byte_array_string(8)

    #ask to open a channel
    hash = blockchain.HASH
    FUNDEE_SOCKET.send(open_channel_message(
        hash,
        funding_satoshis
    ))
    #Receiving accept_channel message
    data = FUNDEE_SOCKET.recv(MAX_LENGTH)
    data = parse_message(data)
    temporary_channel_id = data['temporary_channel_id']
    minimum_depth = data["minimum_depth"]
    #Sending funding_created message
    FUNDEE_SOCKET.send(funding_created_message(temporary_channel_id, SIGNATURE))
    #receiving funding_signed message
    data = FUNDEE_SOCKET.recv(MAX_LENGTH)
    data = parse_message(data)
    channel_id = data["channel_id"]
    #sending funding_locked message
    while(minimum_depth < blockchain.hash_depth(hash)): pass
    FUNDEE_SOCKET.send(funding_locked_message(channel_id))
    #receiving funding_locked message
    data = FUNDEE_SOCKET.recv(MAX_LENGTH)
    data = parse_message(data)
    print("Funding locked!")

    ####################
    ### transactions ###
    ####################

    #send shutdown message
    print("Preparing shutdown...", end=''),
    shutdown_received = False
    while(not shutdown_received):
        FUNDEE_SOCKET.send(shutdown_message(channel_id))
        data = FUNDEE_SOCKET.recv(MAX_LENGTH)
        data = parse_message(data)
        type = ord(data['type'])
        if(type == 38):
            shutdown_received = True
            
    print(" Closing transaction...")
    #close transaction
    fair_fee = generate_byte_array_string(2)
    fee_received = 0
    while(not fair_fee == fee_received):
        FUNDEE_SOCKET.send(closing_signed_message(channel_id, fair_fee, SIGNATURE))
        data = FUNDEE_SOCKET.recv(MAX_LENGTH)
        data = parse_message(data)
        fee_received = data['fee_satoshis']

    print("Transaction ended, thank you.")
    FUNDEE_SOCKET.close()