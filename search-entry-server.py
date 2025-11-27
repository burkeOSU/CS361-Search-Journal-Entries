import time
import zmq
import os
import json

# folder containing files to be searched
searchFolder = "searchFolder"


def folderSearch(keyword, searchFolder):
    # List to store names of files containing keyword
    foundFiles = []

    # navigate into folder
    # search file contents for keyword (use a for loop)
    for file in os.listdir(searchFolder):
        filePath = os.path.join(searchFolder, file)
        with open(filePath) as f:
            if keyword in f.read():
                # if keyword is found, append list
                foundFiles.append(file)

    return foundFiles


def main():

    print("Awaiting message from client…\n")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        #  Waits for message from client
        receivedClient = socket.recv_string()
        print(f"{receivedClient}")

        client = json.loads(receivedClient)

        # receive parameters
        keyword = client.get("keyword")
        searchFolder = client.get("filePath")

        searchResults = folderSearch(keyword, searchFolder)
        #  Pause
        time.sleep(1)

        sentMessage = f"{searchResults}"

        #  Sends reply back to client
        socket.send_string(sentMessage)
        print(f"Sent {sentMessage} message back to client.")
        break


if __name__ == "__main__":
    main()
