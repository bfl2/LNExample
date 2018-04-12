import json

def initMessage():
    type = bytes(16)
    messageDict = {"type":type} #{key:value,key:value...}
    parsed_json = json.dumps(messageDict)
    return parsed_json

def main():


    return
