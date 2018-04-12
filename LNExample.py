import json
import random
import os
import secrets
import string

def initMessage():
    type = str(chr(16))
    messageDict = {"type":type} #{key:value,key:value...}
    parsed_json = json.dumps(messageDict)
    return parsed_json


def generateByteArrayString(size):#in string format, to be decoded on the receiver
    bStr =''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return bStr

def openChannelMessage():##campos sao passados como char
    type = str(chr(32)) ##convertendo os campos para char
    chain_hash = generateByteArrayString(32)
    temporary_channel_id = generateByteArrayString(32)
    funding_satoshis = generateByteArrayString(8)
    messageDict = {"type": type,"chain_hash":chain_hash, "temporary_channel_id":temporary_channel_id,"funding_satoshis":funding_satoshis}
    parsed_json = json.dumps(messageDict)
    #aux = json.loads(parsed_json)
    #print (dict(aux))
    return parsed_json

def main():


    return
main()
openChannelMessage()