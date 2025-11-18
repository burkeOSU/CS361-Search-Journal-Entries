import zmq

context = zmq.Context()

#  Socket talks to server
print("Connecting to server…\n")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Sends message
sent_message = '"This is a message from CS361"'
socket.send_string(sent_message)
print(f"Sent message {sent_message}.")

while True:
    #  Receives reply
    received_message = socket.recv_string()
    print(f"Server response: {received_message}.")
    break