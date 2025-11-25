# This is the base file for search/tag journal entries
# Expected input for ZeroMQ will be the search term. We cannot take in user input directly or have a menu, so this will only be the search functionality.
import time
import zmq
import os

# What do we want the outcome to be?
# How are each of our entries stored?
# may need separate functions for functionality
# tags will arguably be the hardest part. We need somewhere to store tags, and store tags on individual entries
# The only way I can think to do this is hardcoding dictionary file names individually, which we cannot alter otherwise, or using a text file to store the values, either way, lots of work. I don't think I will be using tagging, just searching keywords

def folderSearch(keyword, folder):
  # this will be for terminal-based, just in case
  # folder = directory path /path/example/folder
  print("The following files contain the keyword: {keyword} \n")
  # navigate into folder
  # search file contents for keyword (use a for loop)
  for file in os.listdir(folder):
    with open(file) as f:
        if (keyword in f.read()):
          filePath = os.path.join(folder, file) 
          print(filePath)
  # if keyword is found, print in a list

    

def main():
  print("Awaiting message from client…\n")
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:5555")

  while True:
      #  Waits for message from client
      receivedMessage = socket.recv_string()
      print(f"Received message {receivedMessage}.")

      # Potentially strip the first letter to determine which function to use (mode)
      # Potential modes: Tag versus search mode, and a mode for how the entries are stored.
      if (terminalMode): #filler variable to be changed
        folderSearch(receivedMessage, folder) #variables will likely need to be altered too
      #  Pause
      time.sleep(1)

      #  Sends reply back to client
      sentMessage = '"Message received"'
      socket.send_string(sentMessage)
      print(f"Sent {sentMessage} message back to client.")
      break

if __name__ == "__main__":
    main()

