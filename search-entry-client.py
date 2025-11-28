import zmq
import json

context = zmq.Context()

#  Socket talks to server
print("Connecting to server…\n")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5524")

# Parameters: keyword and file path
keyword = "test"
filePath = "searchFolder"

# Dictionary for keyword and filePath
searchClient = {"keyword": keyword, "filePath": filePath}

# send dictionary in json format
socket.send_string(json.dumps(searchClient))

while True:
    #  Receives reply
    receivedMessage = socket.recv_string()
    print(f"{receivedMessage}")
    break
