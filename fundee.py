from messages import *
import socket
import json


def sxor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def execute():
    print("Fundee executed, waiting for connection...", end='')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('127.0.0.1', 9735))
    serversocket.listen(5)
    (clientsocket, address) = serversocket.accept()
    print(" Connected!")

    while(1):
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
        buffer = clientsocket.recv(MAX_LENGTH)
        messageDic = json.loads(buffer.decode('utf-8'))
        type = ord(messageDic['type'])
        if (type == 16):
            clientsocket.send(init_message())
        elif(type == 32):
            temporary_channel_id = messageDic['temporary_channel_id']
            clientsocket.send(accept_channel_message(temporary_channel_id, 4))
        elif(type == 34):
            funding_txid = messageDic['funding_txid']
            funding_output_index =messageDic['funding_output_index']
            channel_id = sxor(funding_txid, funding_output_index)
            signature = messageDic['signature']
            clientsocket.send(funding_signed_message(channel_id, signature))
        elif(type == 36):
            channel_id = messageDic['channel_id']
            clientsocket.send(funding_locked_message(channel_id))



