from messages import *
import socket
import json
import time

SIGNATURE = generate_byte_array_string(64)

def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def execute():
    print("Fundee executed, waiting for connection...", end='')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('127.0.0.1', 9735))
    serversocket.listen(5)
    (clientsocket, address) = serversocket.accept()
    print(" Connected!")
    time.sleep(2)
    channel_closed_flag=0
    while(channel_closed_flag==0):

        try:
            buffer = clientsocket.recv(MAX_LENGTH)

        except:
            print("buffer error")
        messageDic = parse_message(buffer)

        type = ord(messageDic['type'])
        print("Type read:",type)
        if (type == 16):#received init_message -> send ini_message reply
            clientsocket.send(init_message())
        elif(type == 32):#received open_channel_message -> send accept_channel_message reply
            temporary_channel_id = messageDic['temporary_channel_id']
            clientsocket.send(accept_channel_message(temporary_channel_id, 4))
        elif(type == 34):#received funding_created_message -> send funding_signed_message reply
            funding_txid = messageDic['funding_txid']
            funding_output_index = messageDic['funding_output_index']
            channel_id = sxor(funding_txid, funding_output_index)
            clientsocket.send(funding_signed_message(channel_id, SIGNATURE))
        elif(type == 36):#received funding_locked_message -> send funding_locked_message reply
            #channel_id = messageDic['channel_id']
            clientsocket.send(funding_locked_message(channel_id))
            channel_closed_flag = 1
            print("funding locked!")
        elif(type == 38):#received shutdown
            clientsocket.send(shutdown_message(channel_id))
        elif(type == 39):#close transaction
            data = clientsocket.recv(MAX_LENGTH)
            data = parse_message(data)
            fee_received = data['fee_satoshis']
            fair_fee = fee_received
            clientsocket.send(closing_signed_message(channel_id, fair_fee, SIGNATURE))
                




