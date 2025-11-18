import time
import zmq

print("Awaiting message from client…\n")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Waits for message from client
    received_message = socket.recv_string()
    print(f"Received message {received_message}.")

    #  Pause
    time.sleep(1)

    #  Sends reply back to client
    sent_message = '"Message received"'
    socket.send_string(sent_message)
    print(f"Sent {sent_message} message back to client.")
    break