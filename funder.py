import socket
import messages, blockchain

SOCK = None

def execute():
    blockchain.init()
    print("Funder executed. Stabilising connection...", end='')
    ip = input()
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.connect((ip, 9735))

    #send init message
    SOCK.send(messages.init_message())

    #receive init message
    data = SOCK.recv(messages.MAX_LENGTH)
    data = messages.parse_message(data)

    #ask to open a channel
    SOCK.send(messages.open_channel_message(
        blockchain.HASH,
        messages.generate_byte_array_string(8)
    ))